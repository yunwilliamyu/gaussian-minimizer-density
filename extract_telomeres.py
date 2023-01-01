#!/usr/bin/env python3


tel_annot = []
with open('chm13v2.0_telomere.bed') as f:
    for line in f:
        c, x, y = line.split()
        tel_annot.append([c, int(x), int(y)])

#print(tel_annot)

chromosomes = []
with open('chm13v2.0.fa') as f:
    text = f.read()
    s_chr = text.split('>')

chrom_dict = {}
for chrom in s_chr:
    if chrom[0:3] == 'chr':
        chrom_id = chrom.split()[0]
        chrom_text = "".join(chrom.split('\n')[1:])
        chrom_dict[chrom_id] = chrom_text

print("{", end='')
for tel in tel_annot:
    name_string = '-'.join([str(x) for x in tel])
    tel_text = chrom_dict[tel[0]][tel[1]:tel[2]].upper()
    print('"' + name_string + '":"' + tel_text + '", ', end='')
print("}")
# Note the trailing comma if you want to use this in anything other than a Python dictionary


#print(s_chr[0])
#print(len(s_chr))
#print(s_chr[1])
