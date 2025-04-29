import re

class PolyAAnalyzer:       

    def __init__(self, seq: str):
        self.sequence = seq.upper()
        self.utr3 = ""               
        self.cds = ""                
        self._preprocess_sequence()  
        
        # Signal type weights (based on experimentally validated cutting efficiency)
        self.SIGNAL_WEIGHTS = {
            'AAUAAA': 2.0,    # Typical signal
            'AUUAAA': 1.5,    # Common variable signal
            'AGUAAA': 1.2, 'UAUAAA': 1.2,    # Low frequency active signal
            'OTHERS': 0.8                   # Other matching modes
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

    def analyze(self):
        signals = self.find_polyA_signals()
        #find main signal characteristics
        main_signal = signals[-1] if signals else (None, None) #let main_signal be the last signal of the signals
        polyA_start = main_signal[0]+1+20 if main_signal[0] else None  #assume that ployA starts after 20nt of the signal, based on biological knowledge
        
        #predict polyA length
        polyA_length = 0
        if polyA_start and polyA_start < len(self.sequence):
            polyA_region = self.sequence[polyA_start:]
            polyA_length = len(re.match(r'A+', polyA_region).group()) if re.match(r'A+', polyA_region) else 0

        #Signal Strength Calculation
        signal_strength = sum(self.SIGNAL_WEIGHTS.get(signal, self.SIGNAL_WEIGHTS['OTHERS'])
                              for _, signal in signals)

        # mRNA stability grading
        stability = 'Low'
        if polyA_length >= 200:
            stability = 'Extremely high'
        elif polyA_length >= 100:
            stability = 'High'
        elif polyA_length >= 50 and main_signal[1] in {'AAUAAA'}:
            stability = 'Meddle'
        
        return {
            'sequence_length': len(self.sequence),
            'cds_length': len(self.cds),
            'utr3_length': len(self.utr3),
            'polyA_signals': signals,
            'dominant_signal': main_signal[1],
            'polyA_start': polyA_start,
            'polyA_length': polyA_length,
            'signal_strength': round(signal_strength, 1),
            'mRNA_stability': stability,
            'alternative_signals': signals[:-1] 
        }

if __name__=="__main__":
    test_seq=input("Give me a mRNA sequence: ")
    analysis=PolyAAnalyzer(test_seq)
    results=analysis.analyze()
    
    print(f"sequence_length:{results['sequence_length']} nt")
    print(f"cds_length:{results['cds_length']} nt")
    print(f"3'utr_length:{results['utr3_length']} nt")
    print(f"polyA_signals:{results['polyA_signals']}")
    print(f"dominant_signal:{results['dominant_signal']}")
    print(f"polyA_start:{results['polyA_start']}")
    print(f"polyA_length:{results['polyA_length']} nt")
    print(f"signal_strength:{results['signal_strength']}")
    print(f"mRNA_stability:{results['mRNA_stability']}")
    print(f"alternative_signals:{results['alternative_signals']}")