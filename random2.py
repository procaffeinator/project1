import json
import time
t0 = time.clock()
config=json.loads(open('tuberculist4.json').read())

#Pattern 1
def swap(st,n):
    return st[::-1]

def oddswap(st):
    s = list(st)
    for c in range(0,len(s),2):
        t=s[c]
        s[c]=s[c+1]
        s[c+1]=t

    return "".join(s)    

#calling of functions 

dna=swap(config['Rv0007_Rv0007'],len(config['Rv0007_Rv0007']))

#calling of functions 
dna1=oddswap(dna)
print(dna1)



t1 = time.clock()
cpu_time = t1 - t0
print(cpu_time)
