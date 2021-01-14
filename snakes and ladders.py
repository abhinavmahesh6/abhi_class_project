import random
z=100
c=100
#for board
print("Welcome to Snakes and Ladder.")
input1=input("Press s to start and e to exit:")
l=[]

for i in range(100,0,-1):
    l.append(i)

l[93]='7(LB1)'
l[87]='13(LT1)'
l[80]='20(LB2)'
l[60]='40(LT2)'
l[75]='25(LB3)'
l[33]='67(LT3)'
l[52]='48(LB4)'
l[16]='84(LT4)'
l[37]='63(LB5)'
l[19]='81(LT5)'
l[49]='51(LB6)'
l[31]='69(LT6)'
l[2]='98(SH1)'
l[76]='24(ST1)'
l[61]='39(SH2)'
l[98]='2(ST2)'
l[11]='89(SH3)'
l[48]='52(ST3)'
l[34]='66(SH4)'
l[66]='34(ST4)'
l[13]='87(SH5)'
l[24]='76(ST5)'
l[68]='32(SH6)'
l[85]='15(ST6)'
#llb=List of ladder bases
#llt=List of ladder tops
#lsh=List of snake heads
#lst=List of snake tails
llb=[93,80,75,52,37,49]
llt=[87,60,33,16,19,31]
lsh=[2,61,11,34,13,68]
lst=[76,98,48,66,24,85]

x=0
for i in range(0,10):
    if i%2==0:
        for j in range(0,10):
            print(l[x],end='\t')
            x+=1
        print('\n')
    elif i%2==1:
        x+=10
        for j in range(0,10):
            x-=1
            print(l[x],end='\t')
        print('\n')
        x+=10
pl1=input("Enter a character to use as coin:'#''$''@'*':")
loc=['#','@','$','*']
loc.remove(pl1)
comp=random.choice(loc)
print("The computer chose",comp)
if pl1=='#':
    coin1='#'
if pl1=='$':
    coin1='$'
if pl1=='@':
    coin1='@'
if pl1=='*':
    coin1='*'
if comp=='#':
    coin2='#'
if comp=='$':
    coin2='$'
if comp=='@':
    coin2='@'
if comp=='*':
    coin2='*'
#for dice
if input1=='s' or input1=='S':
    while z>0:
        r=input("Enter r to roll dice:")
        if r=="r" or r=="R":
            diceno=random.randint(1,6)
            print("You rolled",diceno)
            #new=l.pop(z-diceno)
            #l.insert(z-diceno,coin1)
            dup=z
            dup-=diceno
            dicenoc=random.randint(1,6)
            print("Computer rolled",dicenoc)
            #newc=l.pop(c-dicenoc)
            #l.insert(c-dicenoc,coin2)
            dupc=c
            dupc-=dicenoc

            if dup in llb and dupc not in llb:
                if dup==llb[0]:
                    z=llt[0]
                if dup==llb[1]:
                    z=llt[1]
                if dup==llb[2]:
                    z=llt[2]
                if dup==llb[3]:
                    z=llt[3]
                if dup==llb[4]:
                    z=llt[4]
                if dup==llb[5]:
                    z=llt[5]
                if dup>=0 and dupc>=0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c-dicenoc)
                    l.insert(c-dicenoc,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                
                    l.pop(c-dicenoc)
                    l.insert(c-dicenoc,newc)
                
                    l.pop(z)
                    l.insert(z,new)
                    if z==0:
                        print("You win")
                        break
                    c=c-dicenoc
                    print("z=",z,"c=",c)

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup>=0 and dupc<0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(z)
                    l.insert(z,new)
                    l.pop(c)
                    l.insert(c,newc)

                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup<0 and dupc>=0:
                    newc=l.pop(c-dicenoc)
                    l.insert(c-dicenoc,coin2)
                    new=l.pop(z)
                    l.insert(z,coin1)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(c-dicenoc)
                    l.insert(c-dicenoc,newc)
                    c=c-dicenoc
                    l.pop(z)
                    l.insert(z,new)
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break

                elif dup<0 and dupc<0:
                    pass
                
                print("You climbed a ladder",100-dup,"----->",100-z)
                if z==0:
                    print("You win")
                    break
                
                print("z=",z,"c=",c)

                if c==0:
                    print("Computer wins")
                    break
            elif dup not in llb and dupc in llb:
                if dupc==llb[0]:
                    c=llt[0]
                if dupc==llb[1]:
                    c=llt[1]
                if dupc==llb[2]:
                    c=llt[2]
                if dupc==llb[3]:
                    c=llt[3]
                if dupc==llb[4]:
                    c=llt[4]
                if dupc==llb[5]:
                    c=llt[5]
                    
                if dup>=0 and dupc>=0:
                    new=l.pop(z-diceno)
                    l.insert(z-diceno,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                
                    l.pop(c)
                    l.insert(c,newc)
                
                    l.pop(z-diceno)
                    l.insert(z-diceno,new)
                    z=z-diceno
                    if z==0:
                        print("You win")
                        break
                    
                    print("z=",z,"c=",c)

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup>=0 and dupc<0:
                    new=l.pop(z-diceno)
                    l.insert(z-diceno,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(z-diceno)
                    l.insert(z-diceno,new)
                    l.pop(c)
                    l.insert(c,newc)
                    z=z-diceno
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup<0 and dupc>=0:
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    new=l.pop(z)
                    l.insert(z,coin1)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(c)
                    l.insert(c,newc)
                    l.pop(z)
                    l.insert(z,new)
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break

                elif dup<0 and dupc<0:
                    pass                
                print("Computer climbed a ladder",100-dupc,"----->",100-c)
                
                if z==0:
                    print("You win")
                    break
                print("z=",z,"c=",c)

                if c==0:
                    print("Computer wins")
                    break

            elif dup in llb and dupc in llb:
                if dupc==llb[0]:
                    c=llt[0]
                if dupc==llb[1]:
                    c=llt[1]
                if dupc==llb[2]:
                    c=llt[2]
                if dupc==llb[3]:
                    c=llt[3]
                if dupc==llb[4]:
                    c=llt[4]
                if dupc==llb[5]:
                    c=llt[5]
                if dup==llb[0]:
                    z=llt[0]
                if dup==llb[1]:
                    z=llt[1]
                if dup==llb[2]:
                    z=llt[2]
                if dup==llb[3]:
                    z=llt[3]
                if dup==llb[4]:
                    z=llt[4]
                if dup==llb[5]:
                    z=llt[5]
                if dup>=0 and dupc>=0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                
                    l.pop(c)
                    l.insert(c,newc)
                
                    l.pop(z)
                    l.insert(z,new)
                    
                    if z==0:
                        print("You win")
                        break
                    
                    print("z=",z,"c=",c)

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup>=0 and dupc<0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(z)
                    l.insert(z,new)
                    l.pop(c)
                    l.insert(c,newc)
                    
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup<0 and dupc>=0:
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    new=l.pop(z)
                    l.insert(z,coin1)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(c)
                    l.insert(c,newc)
                    
                    l.pop(z)
                    l.insert(z,new)
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break

                elif dup<0 and dupc<0:
                    pass
                
                print("You climbed a ladder",100-dup,"----->",100-z)
                print("Computer climbed a ladder",100-dupc,"----->",100-c)
                if z==0:
                    print("You win")
                    break
                print("z=",z,"c=",c)

                if c==0:
                    print("Computer wins")
                    break


            elif dup in lsh and dupc not in lsh:
                if dup==lsh[0]:
                    z=lst[0]
                if dup==lsh[1]:
                    z=lst[1]
                if dup==lsh[2]:
                    z=lst[2]
                if dup==lsh[3]:
                    z=lst[3]
                if dup==lsh[4]:
                    z=lst[4]
                if dup==lsh[5]:
                    z=lst[5]
              
                if dup>=0 and dupc>=0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c-dicenoc)
                    l.insert(c-dicenoc,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                
                    l.pop(c-dicenoc)
                    l.insert(c-dicenoc,newc)
                
                    l.pop(z)
                    l.insert(z,new)
                    
                    if z==0:
                        print("You win")
                        break
                    c=c-dicenoc
                    print("z=",z,"c=",c)

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup>=0 and dupc<0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(z)
                    l.insert(z,new)
                    l.pop(c)
                    l.insert(c,newc)
                    
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup<0 and dupc>=0:
                    newc=l.pop(c-dicenoc)
                    l.insert(c-dicenoc,coin2)
                    new=l.pop(z)
                    l.insert(z,coin1)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(c-dicenoc)
                    l.insert(c-dicenoc,newc)
                    c=c-dicenoc
                    l.pop(z)
                    l.insert(z,new)
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break

                elif dup<0 and dupc<0:
                    pass
                print("You were eaten by a snake",100-dup,"----->",100-z)
                if z==0:
                    print("You win")
                    break
                c=c-dicenoc
                print("z=",z,"c=",c)

                if c==0:
                    print("Computer wins")
                    break
            elif dup not in lsh and dupc in lsh:
                if dupc==lsh[0]:
                    c=lst[0]
                if dupc==lsh[1]:
                    c=lst[1]
                if dupc==lsh[2]:
                    c=lst[2]
                if dupc==lsh[3]:
                    c=lst[3]
                if dupc==lsh[4]:
                    c=lst[4]
                if dupc==lsh[5]:
                    c=lst[5]
                
                if dup>=0 and dupc>=0:
                    new=l.pop(z-diceno)
                    l.insert(z-diceno,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                
                    l.pop(c)
                    l.insert(c,newc)
                
                    l.pop(z-diceno)
                    l.insert(z-diceno,new)
                    z=z-diceno
                    if z==0:
                        print("You win")
                        break
                    
                    print("z=",z,"c=",c)

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup>=0 and dupc<0:
                    new=l.pop(z-diceno)
                    l.insert(z-diceno,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(z-diceno)
                    l.insert(z-diceno,new)
                    l.pop(c)
                    l.insert(c,newc)
                    z=z-diceno
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup<0 and dupc>=0:
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    new=l.pop(z)
                    l.insert(z,coin1)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(c)
                    l.insert(c,newc)
                    
                    l.pop(z)
                    l.insert(z,new)
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break

                elif dup<0 and dupc<0:
                    pass
                print("Computer was eaten by a snake",100-dupc,"----->",100-c)
                z=z-diceno
                if z==0:
                    print("You win")
                    break
                print("z=",z,"c=",c)

                if c==0:
                    print("Computer wins")
                    break

            elif dup in lsh and dupc in lsh:
                if dupc==lsh[0]:
                    c=lst[0]
                if dupc==lsh[1]:
                    c=lst[1]
                if dupc==lsh[2]:
                    c=lst[2]
                if dupc==lsh[3]:
                    c=lst[3]
                if dupc==lsh[4]:
                    c=lst[4]
                if dupc==lsh[5]:
                    c=lst[5]
                if dup==lsh[0]:
                    z=lst[0]
                if dup==lsh[1]:
                    z=lst[1]
                if dup==lsh[2]:
                    z=lst[2]
                if dup==lsh[3]:
                    z=lst[3]
                if dup==lsh[4]:
                    z=lst[4]
                if dup==lsh[5]:
                    z=lst[5]
                if dup>=0 and dupc>=0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                
                    l.pop(c)
                    l.insert(c,newc)
                
                    l.pop(z)
                    l.insert(z,new)
                    
                    if z==0:
                        print("You win")
                        break
                    
                    print("z=",z,"c=",c)

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup>=0 and dupc<0:
                    new=l.pop(z)
                    l.insert(z,coin1)
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(z)
                    l.insert(z,new)
                    l.pop(c)
                    l.insert(c,newc)
                    
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break
                
                elif dup<0 and dupc>=0:
                    newc=l.pop(c)
                    l.insert(c,coin2)
                    new=l.pop(z)
                    l.insert(z,coin1)
                    x=0
                    for i in range(0,10):
                        if i%2==0:
                            for j in range(0,10):
                                print(l[x],end='\t')
                                x+=1
                            print('\n')
                        elif i%2==1:
                            x+=10
                            for j in range(0,10):
                                x-=1
                                print(l[x],end='\t')
                            print('\n')
                            x+=10
                    l.pop(c)
                    l.insert(c,newc)
                    
                    l.pop(z)
                    l.insert(z,new)
                    print("z=",z,"c=",c)
                    if z==0:
                        print("You win")
                        break

                    if c==0:
                        print("Computer wins")
                        break

                elif dup<0 and dupc<0:
                    pass
                
                
                print("You were eaten by a snake",100-dup,"----->",100-z)
                print("Computer was eaten by a snake",100-dupc,"----->",100-c)
                if z==0:
                    print("You win")
                    break
                print("z=",z,"c=",c)

                if c==0:
                    print("Computer wins")
                    break
                
                
            elif dup>=0 and dupc>=0:
                new=l.pop(z-diceno)
                l.insert(z-diceno,coin1)
                newc=l.pop(c-dicenoc)
                l.insert(c-dicenoc,coin2)
                x=0
                for i in range(0,10):
                    if i%2==0:
                        for j in range(0,10):
                            print(l[x],end='\t')
                            x+=1
                        print('\n')
                    elif i%2==1:
                       x+=10
                       for j in range(0,10):
                            x-=1
                            print(l[x],end='\t')
                       print('\n')
                       x+=10
                
                l.pop(c-dicenoc)
                l.insert(c-dicenoc,newc)
                
                l.pop(z-diceno)
                l.insert(z-diceno,new)
                z=z-diceno
                if z==0:
                    print("You win")
                    break
                c=c-dicenoc
                print("z=",z,"c=",c)

                if c==0:
                    print("Computer wins")
                    break
                
            elif dup>=0 and dupc<0:
                new=l.pop(z-diceno)
                l.insert(z-diceno,coin1)
                newc=l.pop(c)
                l.insert(c,coin2)
                x=0
                for i in range(0,10):
                    if i%2==0:
                        for j in range(0,10):
                            print(l[x],end='\t')
                            x+=1
                        print('\n')
                    elif i%2==1:
                       x+=10
                       for j in range(0,10):
                            x-=1
                            print(l[x],end='\t')
                       print('\n')
                       x+=10
                l.pop(z-diceno)
                l.insert(z-diceno,new)
                l.pop(c)
                l.insert(c,newc)
                z=z-diceno
                print("z=",z,"c=",c)
                if z==0:
                    print("You win")
                    break

                if c==0:
                    print("Computer wins")
                    break
                
            elif dup<0 and dupc>=0:
                newc=l.pop(c-dicenoc)
                l.insert(c-dicenoc,coin2)
                new=l.pop(z)
                l.insert(z,coin1)
                x=0
                for i in range(0,10):
                    if i%2==0:
                        for j in range(0,10):
                            print(l[x],end='\t')
                            x+=1
                        print('\n')
                    elif i%2==1:
                       x+=10
                       for j in range(0,10):
                            x-=1
                            print(l[x],end='\t')
                       print('\n')
                       x+=10
                l.pop(c-dicenoc)
                l.insert(c-dicenoc,newc)
                c=c-dicenoc
                l.pop(z)
                l.insert(z,new)
                print("z=",z,"c=",c)
                if z==0:
                    print("You win")
                    break

                if c==0:
                    print("Computer wins")
                    break

            elif dup<0 and dupc<0:
                pass
















