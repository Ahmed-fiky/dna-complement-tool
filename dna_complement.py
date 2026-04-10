def get_dna_complement_from_file(file_path):
    with open(file_path, 'r') as file:
        seq = file.read()

    seq_lines = seq.split("\n")
    seq = ""
    for i in seq_lines:
        if ">" not in i:
            seq = seq + i

    seq = seq.upper()
    
    i = 0
    result = ""
  
    while i < len(seq):
        base = seq[i]
        
        if base == "A":
            result += "T"
        elif base == "T":
            result += "A"
        elif base == "G":
            result += "C"
        elif base == "C":
            result += "G"
        elif base not in ["A", "T", "C", "G"]:
            print("invalid character:", base)
            break
        
        i += 1
    
    return result

file_path = input("enter file path: ")
print(get_dna_complement_from_file(file_path))
