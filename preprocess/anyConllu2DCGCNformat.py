import sys

file_name = sys.argv[0]


def conllu_to_tok_heads_deprel(file_name, output_name):
    file1 = open(file_name, 'r')
    lines = file1.readlines()
    tok_lines = []
    head_lines = []
    deprel_lines = []
    tok_line = []
    head_line = []
    deprel_line = []
    for line in lines:
        cur_line = line.strip()
        if len(cur_line) < 1:
            if len(tok_line) == 0:
                continue
            else:
                tok_lines.append(" ".join(tok_line) + "\n")
                head_lines.append(" ".join(head_line) + "\n")
                deprel_lines.append(" ".join(deprel_line) + "\n")
                tok_line = []
                head_line = []
                deprel_line = []
                continue
        if cur_line[0] == "#":
            continue

        cur_line = cur_line.split("\t")
        tok_line.append(cur_line[1])
        head_line.append(cur_line[6])
        deprel = cur_line[7]
        deprel_line.append(deprel)
    file1 = open(output_name + '.toks', 'w+')
    file1.writelines(tok_lines)
    file1.close()

    file1 = open(output_name + '.heads', 'w+')
    file1.writelines(head_lines)
    file1.close()

    file1 = open(output_name + '.deprels', 'w+')
    file1.writelines(deprel_lines)
    file1.close()
    return True

if __name__ == '__main__':
    conllu_to_tok_heads_deprel(file_name)