def cost():
    st="select cost from aeroplane_cost where plane_id='%s'"%(Z)
    cursor.execute(st)
    W=cursor.fetchone()
    V,=W
    U=int(V)
    CA=U
    CC=0.6*U
    CI=0
    
    
print('Cost(Adults)',e,'x',CA,'=',e*CA)
print('Cost(Children)',f,'x',CC,'=',f*CC)
print('Cost(Infants)=0')
TC=(e*CA)+(f*CC)
print('Total Cost=',TC)
