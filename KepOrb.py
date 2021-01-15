def AngFreq(Init_Galpy):
    
    o= Orbit(Init_Galpy[:,1:],radec=True)
    o0= Orbit(None)

    W=[] #the unit for it is km/s.kpc

    for i in range(0, len(o)):

        R= o[i].R()
        vx= o[i].vx()
        vy= o[i].vy()
        S= (vx*vx + vy*vy)**0.5

        w= S/R

        W.append(w)

    a= Init_Galpy[:,0].astype('int64')
    a_list= list(a)

    df= pd.DataFrame(data=W)

    data= {'source_id': a_list ,'angular frequency': df.iloc[:,0]}
    D= pd.DataFrame(data=data, columns=['source_id','angular frequency'])

    return D



def FreqFil(data, b=0.00001): #data should be a pandas data frame
    
    o0= Orbit(None)
    R0= o0.R()
    vx0= o0.vx()
    vy0= o0.vy()
    S0= (vx0*vx0 + vy0*vy0)**0.5
    w0= S0/R0
    
    d= np.array(data.iloc[:,1])
    
    WR=[] #This will give the relative error
    
    for i in range(0,len(d)):
        wr= ((d[i]-w0)**2)**0.5 /d[i]
        WR.append(wr)

    D0= {'source_id': data.iloc[:,0],'relative_frequency': WR}
    D1= pd.DataFrame(data=D0, columns=['source_id','relative_frequency'])
    
    D1_filtered= D1.query('relative_frequency < {0}'.format(b))
    
    return D1_filtered
    
    
    
    