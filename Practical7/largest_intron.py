import re
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
introns=re.finditer(r"GT.*?AG",seq)
max_intron_length=0
for intron in introns:
    intron_length=intron.end()-intron.start()
    if intron_length>max_intron_length:
        max_intron_length=intron_length
print(f"The max length is {max_intron_length}.")

#Initialize variables
#sequence <- 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
#max_intron_length <- 0
#Use regular expression to find all possible introns
#intron_list <- Find all matches of the pattern "GT.*?AG" in sequence
#Iterate through each intron
#for each intron in intron_list:
#    Calculate intron_length <- intron_end_position - intron_start_position
#    if intron_length > max_intron_length:
#        Update max_intron_length <- intron_length
#Output the result
#Print "The max length is" and max_intron_length