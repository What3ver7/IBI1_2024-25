import re
#Let the user give us the mRNA sequence and make them a list
sequence=input("Give me mRNA sequence, thanks :) ").upper()
sequence_list=list(sequence)

#Part1
def find_sequence():
    global remaining_sequence
    coding_region=[]
    start_code=False
    start_position=-1
    end=True
    #Find start code "AUG" first
    for i in range(0,len(sequence_list)-2):
        code=sequence[i:i+3]
        if code=="AUG":
            start_position=i
            start_code=True
            break
    #cut the mRNA begining with start code
    #read the code
    #if it has end code, cut it until end code, and append it to coding_region
    if start_code:
        remaining_sequence=sequence[start_position:]
        j=0
        while j < len(remaining_sequence) - 2:
            if j + 3 > len(remaining_sequence):
                break
            end_code = remaining_sequence[j:j+3]
            if end_code in ["UAA", "UAG", "UGA"]:
                end=False
                for v in remaining_sequence[:j]:
                    coding_region.append(v)
                break
            j += 3
    #consider if there is no end code 
    #and has 1 or 2 more useless code at the tail of mRNA
    #cut it and append the remain
    if end:
        if len(remaining_sequence) - j == 1 or len(remaining_sequence) - j == 2:
            remaining_sequence = remaining_sequence[:j]
        for v in remaining_sequence:
            coding_region.append(v)
        #if there is noend code and has 1 or 2 more useless code, cut it and append the remain
    return coding_region

#Part2
codon_table = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}
# def a counter function to counter the frequency of acid
def counter(m):
        acid_dict={}
        for i in m:
            acid_dict[i]=acid_dict.get(i,0)+1
        return acid_dict

#define a funtion to find the max fruquent amino acid
def max_amino_acid(coding_region):
    all_acids=[]
    if not coding_region:
        return None
    for i in range(0,len(coding_region)-2,3):
        #translate the mRNA into the amnio acid
        mRNA1=coding_region[i:i+3]
        mRNA2="".join(mRNA1)
        acids=codon_table[mRNA2]
        all_acids.append(acids)
    #counter the number of all amino acids
    acid=counter(all_acids)
    #find the max number amino acid
    max_count=max(acid.values())
    #append the name of the amino acid into a list
    #if the max have more than 1, append all of them
    max_acid=[acid_name for acid_name,count in acid.items() if count==max_count]
    return acid,max_acid

#Part4
#define a function to calculate the A,U,C,G numbers in the mRNA sequence
def reverse(z):
    DNA_sequence=re.sub(r'[AUCG]', lambda m:{'A':'T','U':'A','C':'G','G':'C'}[m.group()], z)
    return DNA_sequence
def calculator(sequence):
    A_count=sequence.count("A")
    T_count=sequence.count("T")
    C_count=sequence.count("C")
    G_count=sequence.count("G")
    per=((C_count+G_count)/(C_count+G_count+A_count+T_count))
    print(f"The percentage of C and G is {per}")
    if per<=0.3:
        print("It's not stable, DNA may be more susceptible to degradation.")
    elif 0.3<per<0.7:
        print("It's stable.")
    else:
        print("It's stable, However, it may lead to the overcomplexity of the secondary structure of mRNA, "
        "which affects the transcription efficiency")

#The main part
x=find_sequence()
y=max_amino_acid(x)
acid=y[0]
max=y[1]
result="".join(x)
print(f"The mRNA sequence is {result}")
print(f"Most frequency amino acid is {max}")

#Part3
#Draw
import matplotlib.pyplot as plt
x=list(acid.keys())
y=[int(value) for value in acid.values()]
plt.bar(x,y)
plt.xlabel("Amino acid name")
plt.ylabel("Times")
for i,value in enumerate(y):
    plt.text(i, value, f"{value}",ha="center", va="bottom")
plt.title("Amino acid frequencies")
plt.show()

#reverse transcription the mRNA into DNA
#Then calculate the CG porpotion in the DNA sequence and judge whether the DNA chain is stable or not.
DNA=reverse(result)
print(DNA)
calculator(DNA)