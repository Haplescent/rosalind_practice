from sys import argv
script , filename = argv

txt_file = open(filename, "r")
txt = txt_file.read()
txt_file.close()

print(txt)

def complementary(t):
    dna_list = []
    for char in t:
        if char == "T":
            dna_list.append("A")
        elif char == "A":
            dna_list.append("T")
        elif char == "G":
            dna_list.append("C")
        elif char == "C":
            dna_list.append("G")
    dna_list.reverse()
    reverse_complement = "".join(dna_list)
    return reverse_complement
print(complementary(txt))
