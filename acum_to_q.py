import sys
out = ''
for line in sys.stdin:
    line = line.rstrip()
    tabs = line.split('\t')
    for i in range(len(tabs)):
        if i > 0: out += '\t'
        if i%4 == 0:
            out += tabs[i]
        else:
            if i%4==1:
              out += '='+tabs[i]+'-RC[-1]'
            elif i%4==2:
              out += '='+tabs[i]+'-RC[-1]-RC[-2]'
            else:
              out += '='+tabs[i]+'-RC[-1]-RC[-2]-RC[-3]'
    out += '\n'


out = out.rstrip('\n')
sys.stdout.write(out)

