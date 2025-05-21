import re
import random
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from matplotlib import rcParams

def codon_calculator(target_sequence):
    
    # Find the start codon (AUG)
    RNA_initiation = target_sequence.find('AUG')
    if RNA_initiation == -1:
        return None  # Return None if no start codon is found

    else:    
        # Find the first stop codon (UAA, UAG, UGA)
        RNA_termination = len(target_sequence)
        stop_codons = ['UAA', 'UAG', 'UGA']
        for i in range(RNA_initiation, len(target_sequence) - 2, 3):
            if target_sequence[i:i+3] in stop_codons:
                RNA_termination = i + 3
                break
    
    # Count codon frequencies
    codon_frequencies = {}
    for i in range(RNA_initiation, RNA_termination, 3):
        if i + 3 <= RNA_termination:
            codon = target_sequence[i:i+3]
            if codon in codon_frequencies:
                codon_frequencies[codon] += 1
            else:
                codon_frequencies[codon] = 1
    
    # Find the most frequent codon
    if codon_frequencies:
        highest_frequency1 = max(codon_frequencies.values()) # find the highest frequency first
        most_frequent_codon = [codon for codon, freq in codon_frequencies.items() if freq == highest_frequency1] # ensure all the codon appear as frequent
        
      # Convert the most frequent RNA codon to DNA      
        rna_to_dna = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}
        corresponding_DNA = []
        
        for codon in most_frequent_codon:
            dna_codon = ''.join(rna_to_dna[base] for base in codon)
            corresponding_DNA.append(dna_codon)

        dna_str = ', '.join(''.join(rna_to_dna[base] for base in codon) for codon in most_frequent_codon)
        print('The corresponding DNA:', dna_str)    
        #print(f"The corresponding DNA sequence: {dna_codon}")
    else:
        print("No valid codons found in the sequence.")

    return codon_frequencies  # Return the codon frequencies

class PolyAAnalyzer:       

    def __init__(self, seq: str):
        self.sequence = seq.upper()
        self.utr3 = ""               
        self.cds = ""                
        self._preprocess_sequence()  

        self.SIGNAL_WEIGHTS = {
            'AAUAAA': 2.0,    # Typical signal
            'AUUAAA': 1.5,    # Common variable signal
            'AGUAAA': 1.2, 'UAUAAA': 1.2,  # Low frequency active signal
            'OTHERS': 0.8 # Other matching modes
        }

    def _preprocess_sequence(self):
        #Find the start codon, cds and 3' utr，if there is end codon
        start_codon = re.search(r'AUG', self.sequence)
        if not start_codon:
            raise ValueError("can't find the start code AUG")

        cds_start = start_codon.start()
        cds_candidate = self.sequence[cds_start:]
        for i in range(0, len(cds_candidate)-2, 3):
            codon = cds_candidate[i:i+3]
            if codon in {'UAA', 'UAG', 'UGA'}:
                self.cds = cds_candidate[:i]
                self.utr3 = cds_candidate[i+3:]
                return

        #if there isn't end codon, let the following sequence be cds
        self.cds = self.sequence[cds_start:]
        self.utr3 = ""

    #Find all polyA signals and its position
    def find_polyA_signals(self):
        signals = []
        pattern = r'(AAUAAA|AUUAAA|AGUAAA|UAUAAA)'
        for match in re.finditer(pattern, self.utr3):
            position = match.start()+len(self.sequence)-len(self.utr3)+1
            signals.append( (position, match.group()) )
        return signals
    
    def find_actual_polyA_tail(self, min_length=10):
        #find if there is polyA tail in the mRNA sequence
        full_tail_match = re.search(r'A{'+str(min_length)+r',}$', self.sequence)
        if full_tail_match:
            return len(full_tail_match.group())
        polyA_region = self.sequence[len(self.sequence) - len(self.utr3):]
        polyA_length = len(re.match(r'A+', polyA_region).group()) if re.match(r'A+', polyA_region) else 0
        return polyA_length if polyA_length>=min_length else 0

    def predict_polyA_length(self, signal_type: str):
        # Predict the typical length range based on signal strength
        base_length = {
            'AAUAAA': random.randint(180, 250),
            'AUUAAA': random.randint(120, 200),
            'AGUAAA': random.randint(80, 150),
            'UAUAAA': random.randint(80, 150),
            'OTHERS': random.randint(50, 100)
        }.get(signal_type, 50)
        return max(10, int(base_length * (0.8 + 0.4 * random.random())))

    def analyze(self):
        signals = self.find_polyA_signals()
        #find main signal characteristics
        main_signal = signals[-1] if signals else (None, None) #let main_signal be the last signal of the signals
        
        actual_polyA_length = self.find_actual_polyA_tail()
        actual_polyA_start = len(self.sequence) - actual_polyA_length if actual_polyA_length > 0 else None

        #predict polyA length
        if actual_polyA_length > 0:
            polyA_length = actual_polyA_length
            polyA_start = actual_polyA_start
            detection_method = "direct"
        elif signals:
            predicted_polyA_start = main_signal[0]+1+20 if main_signal[0] else None  #assume that ployA starts after 20nt of the signal, based on biological knowledge
            if predicted_polyA_start and predicted_polyA_start:
                polyA_length = self.predict_polyA_length(main_signal[1] if main_signal else 'OTHERS')
                polyA_start = predicted_polyA_start
                detection_method = "predicted"

        # mRNA stability grading
        stability = 'Low'
        if polyA_length >= 200:
            stability = 'Extremely high'
        elif polyA_length >= 100:
            stability = 'High'
        elif polyA_length >= 50:
            stability = 'Meddle'
        
        return {
            'sequence_length': len(self.sequence),
            'cds_length': len(self.cds),
            'utr3_length': len(self.utr3),
            'polyA_signals': signals,
            'dominant_signal': main_signal[1],
            'polyA_start': polyA_start,
            'detection_method': detection_method,
            'polyA_length': polyA_length,
            'mRNA_stability': stability,
            'alternative_signals': signals[:-1] 
        }
    
    def visualize_analysis(sequence):
        analyzer = PolyAAnalyzer(sequence)
        result = analyzer.analyze()

        table_data = {
            "Sequence Length": result['sequence_length'],
            "CDS Length": result['cds_length'],
            "3' UTR Length": result['utr3_length'],
            "Dominant Signal": result['dominant_signal'],
            "PolyA Start": result.get('polyA_start', 'N/A'),
            "Detection Method": result.get('detection_method', 'N/A'),
            "PolyA Length": result.get('polyA_length', 'N/A'),
            "mRNA Stability": result['mRNA_stability'],
        }

        df_main = pd.DataFrame([table_data])
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.axis('off')
        table = ax.table(
            cellText=df_main.values,
            colLabels=df_main.columns,
            loc='center',
            cellLoc='center',
            colColours=['#B0C4DE'] * len(df_main.columns),
        )

        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 2)
        plt.title("PolyA Analysis Summary", fontsize=16, pad=20)
        plt.tight_layout()
        plt.show()

        if result['polyA_signals']:
            df_signals = pd.DataFrame(result['polyA_signals'], columns=["Position", "Signal"])
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.axis('tight')
            ax.axis('off')
            ax.table(cellText=df_signals.values, colLabels=df_signals.columns, cellLoc='center', loc='center', colColours=["lightgray"]*2)

            plt.title('Identified PolyA Signals', fontsize=16)
            plt.show()

        else:
            print("\nNo PolyA signal detected.")


if __name__=="__main__":
    RNA_sequence = "AUGGAAGAGGAUAAUGGAAAGUGGAAGUUGGAGGUAAGGGUAAAGUUGGAAGGUGGGUAAUGGAAGGAGGAUGGAGGAGGUAAGGGAUUGAAGUGGAUGGAGGAAGUGGAGGUAGGAAGGAAGUAA"

    codon_frequencies = codon_calculator(RNA_sequence)
    print('Codon frequencies', codon_frequencies)
    
    if not all(c in 'AUCG' for c in RNA_sequence):
        print('Sequence Error! Only A,U,C,G allowed, please check again.')
        exit()
    
    if codon_frequencies is None:
        print("No start codon (AUG) found in the sequence.")
        exit()
    
    # construct the amino acid - codon dictionary
    aa_to_codons = {
        'Met': ['AUG'],
        'Phe': ['UUU', 'UUC'],
        'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
        'Ile': ['AUU', 'AUC', 'AUA'],
        'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
        'Ser': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
        'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
        'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
        'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
        'Tyr': ['UAU', 'UAC'],
        'His': ['CAU', 'CAC'],
        'Gln': ['CAA', 'CAG'],
        'Asn': ['AAU', 'AAC'],
        'Lys': ['AAA', 'AAG'],
        'Asp': ['GAU', 'GAC'],
        'Glu': ['GAA', 'GAG'],
        'Cys': ['UGU', 'UGC'],
        'Trp': ['UGG'],
        'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'Gly': ['GGU', 'GGC', 'GGA', 'GGG'],
    }
    
    # count amino acid frequencies (the same mechanism as Part 1)
    amino_acid_frequencies = {}
    for AA in aa_to_codons.keys():
        for codon in codon_frequencies:
            if codon in aa_to_codons[AA]:
                if AA in amino_acid_frequencies:
                    amino_acid_frequencies[AA] += codon_frequencies[codon]
                else:
                    amino_acid_frequencies[AA] = codon_frequencies[codon]
    # print the results of amino acids frequencies
    print('Amino acid frequencies:', amino_acid_frequencies)
    # print the most frequent amino acid
    
    if amino_acid_frequencies:
        highest_frequency2 = max(amino_acid_frequencies.values())
        most_frequent_AC = [AC for AC, freq in amino_acid_frequencies.items() if freq == highest_frequency2]
        print(f"The most frequent codon: {', '.join(most_frequent_AC)}")
        
    else:
        print('No amino acid was found')
    
    sorted_aa_order = [aa for aa in aa_to_codons if aa in amino_acid_frequencies]
    aa_values = [amino_acid_frequencies[aa] for aa in sorted_aa_order]
    plt.figure(figsize=(12, 6))
    bars = plt.bar(sorted_aa_order,aa_values,color='skyblue', edgecolor='black',linewidth=0.8)
    
    plt.title('Amino Acid Frequency Distribution (Original Order)', fontsize=14, pad=15)
    plt.xlabel('Amino Acids', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.005*max(aa_values), f'{yval}',ha='center', va='bottom',fontsize=13)
    
    plt.tight_layout()
    plt.show()

    rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.figsize': (10, 6),
    'axes.grid': True
})
    
    test_sequence1="GGAUCCAGGAGGUUAACGCAUGGCUACUGAAGCUUCGGAAGGCUCCGAACCGGAUUGCUAGUAAAAAUAAAGUCCAGUAUUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    test_sequence2="CGGUCAAGGCGGAGCCGAGAUGGCUACUGAAGCAUCCGAUCGAGCACGACAGACGCAGUAAAUUAAAUAUAAACGACGAGCAAAUAAA"
    PolyAAnalyzer.visualize_analysis(test_sequence1)
    PolyAAnalyzer.visualize_analysis(test_sequence2)