def read_sequence(seq_name):
    with open(seq_name) as seq:
        lines=seq.read().splitlines()
    return ''.join([line for line in lines if not line.startswith(">")])

def read_BLOSUM62(matrix_name):
    matrix={}
    with open(matrix_name) as m:
        lines=[]
        for line in m:
            line=line.strip()
            lines.append(line)

        headers = lines[0].split()
        for line in lines[1:]:
            parts = line.split()
            row_aa = parts[0] 
            for i in range(1, len(parts)):
                col_aa = headers[i - 1]
                score = int(parts[i])
                matrix[(row_aa, col_aa)] = score
    
    return matrix

def compare_sequence(seq1,seq2,matrix):
    score=0
    matches=0
    for a,b in zip(seq1,seq2):
        if (a,b) in matrix:
            score+=matrix[(a,b)]
        else:
            score+=0
        if a==b:
            matches+=1
    identity=matches/len(seq1)*100
    return score, identity

seq1=read_sequence(r"D:\IBI1\IBI1_2024-25\Practical13\mouse_sod2.fasta")
seq2=read_sequence(r"D:\IBI1\IBI1_2024-25\Practical13\random.fasta")
matrix=read_BLOSUM62(r"D:\IBI1\IBI1_2024-25\Practical13\BLOSUM62.txt")

score, identity=compare_sequence(seq1, seq2, matrix)
print(f"Score: {score}, Identity: {identity:.2f}%")