## SOLUTION 1 (mine)
# dataset = "CCACCTCGTTACGTCACCAAGATCGGATTTTACAACGTGTAAGACGAAATTGCATAGGTCCTGAGATTGCACCTGCCGTTCTTCCCAAAAAACGATGTGTGTGAGGGCTTCAGGCTCGCAAAGACCAGTAGCCCAATAACTATTACGTAGCCAGACGCAATGGGGACAGAGAGCCCCCTCAGCAAACTCGGCACGCTTGGAGCATCTCACATCACAGGATCTCATTGGGCGAGTACAGCACGCTAGTGGCACCAGATGGACACTCTTACTAGTGCTTTCGTTGTGAAAGTTTCGTTCGGGCTGTGACCGAATGCGTAATGCGCAGACGCTAATGGAAGCGATCGCCAGTGGTGCCGGAGTTGCCGAATAGACGATTTTGTATAGTCCATCCTCGCCACTCCATGTATGGCCGCGCAAAGCGTTGCCTCATGTCGACGCAGGAACTTAGGGGGCTGATGATACTACTTACCCTCGTATATACAGCTTTTCGTAGCTATTGAAAGAGTGTGACTACATGAATAAAGCGTTGTGTCACACTCTTATCCAACTATATATCGCTCGTCAGAGTTTGATCTTCAGGTGTATCAGGCGCAGATGTGCAGGTACAGATACCGTGGCGGGTTCAGTGAATCTGCGTCCCTTTATTGGCGTAAGAGCTTCGCTGGCGAGGCGCTCTCTTAGCATAAGTCAATGGCCTGGGGCTAAGAGCCAGCCCGTTCTAACGGTCGCGCTCGTAAACCCTGCCTGATGGCTAACAAGACTGCGGTCTCGGCTCGGATCATGCAGGCGGAAAATCTGCTCTCGGAAATATCGGAGACCGTTGTTTAAT"
    
# count_a = 0
# count_t = 0
# count_g = 0
# count_c = 0

# for base in dataset:
#     if base == 'A':
#         count_a += 1
#     if base == 'T':
#         count_t += 1
#     if base == 'G':
#         count_g += 1
#     if base == 'C':
#         count_c += 1
    
# print(str(count_a) + " " + str(count_c) + " " + str(count_g) + " " + str(count_t))

## SOLUTION 2 (using count() method)
# dataset = "CCACCTCGTTACGTCACCAAGATCGGATTTTACAACGTGTAAGACGAAATTGCATAGGTCCTGAGATTGCACCTGCCGTTCTTCCCAAAAAACGATGTGTGTGAGGGCTTCAGGCTCGCAAAGACCAGTAGCCCAATAACTATTACGTAGCCAGACGCAATGGGGACAGAGAGCCCCCTCAGCAAACTCGGCACGCTTGGAGCATCTCACATCACAGGATCTCATTGGGCGAGTACAGCACGCTAGTGGCACCAGATGGACACTCTTACTAGTGCTTTCGTTGTGAAAGTTTCGTTCGGGCTGTGACCGAATGCGTAATGCGCAGACGCTAATGGAAGCGATCGCCAGTGGTGCCGGAGTTGCCGAATAGACGATTTTGTATAGTCCATCCTCGCCACTCCATGTATGGCCGCGCAAAGCGTTGCCTCATGTCGACGCAGGAACTTAGGGGGCTGATGATACTACTTACCCTCGTATATACAGCTTTTCGTAGCTATTGAAAGAGTGTGACTACATGAATAAAGCGTTGTGTCACACTCTTATCCAACTATATATCGCTCGTCAGAGTTTGATCTTCAGGTGTATCAGGCGCAGATGTGCAGGTACAGATACCGTGGCGGGTTCAGTGAATCTGCGTCCCTTTATTGGCGTAAGAGCTTCGCTGGCGAGGCGCTCTCTTAGCATAAGTCAATGGCCTGGGGCTAAGAGCCAGCCCGTTCTAACGGTCGCGCTCGTAAACCCTGCCTGATGGCTAACAAGACTGCGGTCTCGGCTCGGATCATGCAGGCGGAAAATCTGCTCTCGGAAATATCGGAGACCGTTGTTTAAT"

# def read_seq(s):
#     print(str(s.count("A")) + " " + str(s.count("C")) + " " + str(s.count("G")) + " " + str(s.count("T")))

# read_seq(dataset)

## SOLUTION 3 (same as above, more concise)
# dataset = ""

# def read_seq(s):
#     return s.count("A"), s.count("C"), s.count("G"), s.count("T")

# a = read_seq(dataset)
# print(a)

## SOLUTION 4 (using map, unpacking * operator)
# print(*map(input("enter dna string: ").count, "ACGT"))

## SOLUTION 5 (using dictionaries)
# string = input("enter dna string: ")
# freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
# for nuc in string:
#     freq[nuc] += 1
# print(freq['A'],freq['C'],freq['G'],freq['T'])