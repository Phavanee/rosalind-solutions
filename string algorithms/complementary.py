## SOLUTION 1 (mine)
# s = input("enter a dna sequence: ")

# def complement(s):
#     sc = ""
#     for index in range(len(s)-1,-1,-1):
#         if s[index] == "A":
#             sc += "T"
#         if s[index] == "T":
#             sc += "A"
#         if s[index] == "G":
#             sc += "C"
#         if s[index] == "C":
#             sc += "G"
#     return sc

# print(complement(s))

## SOLUTION 2
# st = "AAAACCCGGT"
# st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# print(st)

## SOLUTION 3
# s = 'AAAACCCGGT'
# print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))