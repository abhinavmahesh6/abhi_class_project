p=[]
for i in range(65,93):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10):
                    if j==0 and k==0 and l==0 and m==0:
                        pass
                    else:
                        s=str(chr(i))+str(j)+str(k)+str(l)+str(m)
                        p.append(s)
    

