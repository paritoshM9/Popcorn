import sys

consumed=0
n = int(input().strip())
consumed+=n
num_wrappers=n
extrapop=0
while(num_wrappers>=3):
    num_wrappers-=3
    extrapop+=1
    num_wrappers+=1
consumed+=extrapop
if(num_wrappers==2):
    #borrow 1 packet
    num_wrappers+=1
    consumed+=1
    
    
print(consumed)
