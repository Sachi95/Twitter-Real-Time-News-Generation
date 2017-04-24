import linecache

with open('Governing Council') as f:
    for i, l in enumerate(f):
            pass
    x=i+1
    k=0
    i=2
    j=1
    initial=linecache.getline('Governing Council', 1)
    clean= open ('clean.txt','w')
    clean.write(initial)
    while i<(x+1):
        a=linecache.getline('Governing Council', i)
        while j<i:
            b=linecache.getline('Governing Council', j)
            t1=set(a.split(" "))
            t2=set(b.split(" "))
            t3=t1.intersection(t2)
            if len(t3)>0.5*len(t1):
                k=k+1
            j=j+1
        if k==0:
                clean= open ('clean.txt','a')
                clean.write(a)
        k=0
        j=1
        i=i+1