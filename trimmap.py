#main
def trim(line):
    nline = line.replace(" ", "")
    nline = nline.strip()
    return nline

   
f = open('map.txt', 'r')
o = open('omap.txt', 'a')

line = f.readline()
while line != '':
    nline = trim(line)
    line = f.readline()
    if line == '':
        o.write(nline)
    else:
        o.write(nline + '\n')

o.close()