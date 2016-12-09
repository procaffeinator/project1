import json
import time
t0 = time.clock()
config=json.loads(open('tuberculist4.json').read())

#Pattern 1
def swap(st,n):
    return st[::-1]

#calling of functions 

dna=swap(config['Rv0007_Rv0007'],len(config['Rv0007_Rv0007']))
print(dna)


t1 = time.clock()
cpu_time = t1 - t0
print(cpu_time)
