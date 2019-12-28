from sys import argv
script, filename_txt = argv

txt = open(filename_txt, "r")
read_txt = txt.read()
print(type(read_txt))

def count_ATGC(s):
    num_A, num_T, num_C, num_G = 0, 0, 0, 0

    for char in s:
        if char == "A":
            num_A += 1
            print("A")
        elif char == "T":
            num_T += 1
            print("T")
        elif char == "C":
            num_C += 1
            print("C")
        elif char == "G":
            num_G += 1
            print("G")
    return "%d %d %d %d" % (num_A, num_C, num_G, num_T)

print(count_ATGC(read_txt))
