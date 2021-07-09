def repetition(x):
    max_val, count=1, 1
    for i in range(1,len(x)):
        count= count+1 if (x[i])==x[i-1] else 1
        max_val=max(max_val,count)
    return(max_val)
s=input()
print(repetition(s))
