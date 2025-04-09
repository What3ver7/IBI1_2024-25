import re
with open("D:\VS CODE\gitgit\IBI1_2024-25\Homework\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r") as infile, open("D:\VS CODE\gitgit\IBI1_2024-25\Homework\Practical7\\tata_genes.fa","w") as outfile:
    gene_name=""
    sequence=""
    for line in infile:
        line=line.strip()
        if re.search(r"^>",line):
            if sequence and re.search(r"TATA[AT]A[AT]",sequence):
                outfile.write(f">{gene_name1}\n{sequence}\n")
            gene_name=re.findall(r"gene:.*?\s", line)
            gene_name1=gene_name[0][5:-1]
            sequence=""
        else:
            sequence+=line
    if sequence and re.search(r"TATA[AT]A[AT]",sequence):
            outfile.write(f">{gene_name1}\n{sequence}")

print(f"Genes with TATA box written to {outfile}")

#import re
#open the infile with read method, and outfile with write method
#Initialize variables, gene_name and sequence
#strat a while loop
#when we first time search the ">", find and sort the gene_name 
#then we search the following lines for the sequence
#when the next time we search the ">"
#if we have sequence and have TATAWAW in the sequence
#write the gene_name and sequence into the outfile
#if we don't have TATAWAW in the sequence
#ignore it
