import json
import time
t0 = time.clock()
config=json.loads(open('tuberculist4.json').read())


def oddswapp(st):
    s = list(st)
    for c in range(0,len(s),4):
        t=s[c]
        s[c]=s[c+1]
        s[c+1]=t

    return "".join(s)    

#calling of functions 


#calling of functions 
dna1=oddswapp(config['Rv0007_Rv0007'])
print(dna1)



t1 = time.clock()
cpu_time = t1 - t0
print(cpu_time)
