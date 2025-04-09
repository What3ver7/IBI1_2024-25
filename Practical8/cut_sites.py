# Define a function named cut with two parameters: sequence and recognised_sequence.
# Initialize a variable nucleotides_auth to True.
# Create an empty list named position_list to store the positions of the recognised sequence.
# Determine the length of the recognised_sequence.
# Loop through each character in the sequence to check if it's a valid nucleotide (A, T, C, G).
# If an invalid nucleotide is found, set nucleotides_auth to False.
# Do the same check for each character in the recognised_sequence.
# If nucleotides_auth is False at this point, return None and the nucleotides_auth.
# Initialize a counter i to 0 to track the position in the sequence.
# Use a while loop to iterate through the sequence until the end is reached.
# If the sequence slice from i to i+length matches the recognised_sequence, append i to position_list and increment i by the length.
# Otherwise, just increment i by 1.
# After the loop, return the position_list and the nucleotides_auth.
# Ask the user to input the DNA sequence.
# Ask the user to input the sequence recognised by the restriction enzyme.
# Call the cut function with the provided sequences and store the result in x and y.
# If y is False, print an error message indicating that only ATCG are valid nucleotides.
# If y is True, check if x is empty.
# If x is empty, inform the user that the recognised sequence was not found.
# If x is not empty, print the positions where the restriction enzyme cuts the DNA sequence.
# If there's only one cut position, use singular phrasing; if more than one, use plural.

def cut(sequence,recognised_sequence):
    nucleotides_auth=True
    position_list=[]
    length=len(recognised_sequence)
    for i in sequence:
        if i not in ["A","T","C","G"]:
            nucleotides_auth=False
    for i in recognised_sequence:
        if i not in ["A","T","C","G"]:
            nucleotides_auth=False
    if nucleotides_auth==False:
        return None, nucleotides_auth
    i=0
    while i<len(sequence):
        if sequence[i:i+length]==recognised_sequence:
            position_list.append(i)
            i+=len(recognised_sequence)
        else:
            i+=1
        
    return position_list, nucleotides_auth

sequence=input("Give me the DNA sequence: ")
recognised_sequence=input("Give me the sequence recognised by the restriction enzyme: ")
x,y=cut(sequence,recognised_sequence)
if y==False:
    print("It's error, sequence only contains ATCG.")
else:
    if len(x)==0:
        print("There isn't sequence recognised by the restriction enzyme")
    elif len(x)==1:
        print(f"The position within the DNA sequence where the restriction enzyme cuts is in the {','.join(str(z) for z in x)} place")
    else:
        print(f"The positions within the DNA sequence where the restriction enzyme cuts are in the {','.join(str(z) for z in x)} place")


#Success Example
"""
DNA sequence=ACTAGCGTAGCGACTACGTACTACG
recognised_sequence=ACTA
print: The positions within the DNA sequence where the restriction enzyme cuts are in the 0,12,19 place
"""

#Failure Example
"""
DNA sequence=ACTUGCAGCGTAGCTAGC
recognised_sequence=ACT
result: It's error, sequence only contains ATCG.
"""