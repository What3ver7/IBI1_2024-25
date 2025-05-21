# Define a list called splice_combinations containing 'GTAG', 'GCAG', and 'ATAC'.
# Ask the user to input a splice combination and convert the input to uppercase and strip any whitespace.
# While the user input is not in the splice_combinations list:
# Print an error message telling the user the input is invalid.
# Prompt the user to enter the splice combination again.
# Create an output file name using the valid splice combination and the suffix '_spliced_genes.fa'.
# Open the input file named 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' in read mode.
# Open the output file using the previously generated name in write mode.
# Initialize an empty list called current_gene to store the current gene name.
# Compile a regular expression pattern to search for TATA box sequences like TATAAA, TATATA, etc.
# Compile another pattern to extract gene names from lines that contain 'gene:<name>'.
# Compile a splice site pattern using the first two and last two letters of the chosen splice combination.
# For each line in the input file:
# If the line contains a gene name:
# If there is a previous gene and its corresponding sequence stored:
# Join the sequence lines into one continuous string.
# If the splice site pattern is found in the sequence:
# Find all matching splice sequences.
# Initialize a counter to count the number of TATA boxes.
# For each splice sequence found:
# If the splice sequence contains a TATA box pattern:
# Count how many TATA boxes are found and add to the counter.
# Write the gene name and the number of TATA boxes to the output file.
# Write the original gene sequence to the output file.
# Update current_gene with the new gene name found.
# Clear the current_sequence list to start collecting new sequence lines.
# If the line does not contain a gene name, add it to the current_sequence list.
# After the loop, handle the last gene in case it was not processed:
# Join the remaining sequence lines into one string.
# If the splice pattern is found in the sequence:
# Search for TATA boxes and count them.
# Write the last gene’s information and sequence to the output file.

import re
splice_combinations=['GTAG','GCAG','ATAC']
splice_input=input(f'enter splice combination {splice_combinations[:]}').strip().upper()
while splice_input not in splice_combinations:
    print('invalid input. try again')
    splice_input=input(f'enter splice combination {splice_combinations[:]}').strip().upper()
output_filename=f'{splice_input}_spliced_genes.fa'
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile, open(f"{output_filename}_spliced_genes.fa", 'w') as outfile:
    current_gene=[]
    tata_pattern=re.compile(r'TATA[AT]A[AT]')
    gene_name_pattern=re.compile(r'gene:(\S+)')
    splice_pattern=re.compile(fr'{splice_input[:2]}.*?{splice_input[-2:]}')
    for line in infile: 
        if gene_name_pattern.search(line):
            if current_gene and current_sequence:
                full_sequence=''.join(seq.strip() for seq in current_sequence)
                if splice_pattern.search(full_sequence):
                    splice_seq=splice_pattern.findall(full_sequence)
                    tata_box_number=0
                    for i in splice_seq:
                        if tata_pattern.search(i):
                            tata_box_seq=tata_pattern.findall(i)
                            tata_box_number+=len(tata_box_seq)
                            outfile.write(f'>{current_gene[0]}, the number of instances of TATA box is {tata_box_number} \n')
                            outfile.writelines(current_sequence)
            current_gene=gene_name_pattern.findall(line)
            current_sequence=[]
        else:
            current_sequence.append(line) 
    if current_gene and current_sequence:
        full_sequence=''.join(line.strip() for line in current_sequence)
        if splice_pattern.search(full_sequence):
            splice_seq=splice_pattern.findall(full_sequence)
            for i in splice_seq:
                if tata_pattern.search(i):
                    tata_box_seq=tata_pattern.findall(i)
                    tata_box_number+=len(tata_box_seq)
            outfile.write(f'>{current_gene[0]}, the number of instances of TATA box is {tata_box_number} \n')
            outfile.writelines(current_sequence)
