
# coding: utf-8

# L'algorithme utilisé est celui de Sliding Window.

# In[1]:


from math import log


# In[2]:


def minProd(k):# fonction qui contient seulement la main loop
    
    Total = 0  # initialisation
    for i in range(2, k+1):
        partial = float('inf')
        
        for j in range(1, int(log(i,2))+1 ):
            w = window(i, j)
            if w < partial :
                partial = w # chaine minimale

        Total += partial

    print( "Somme de la longueur des chaines d'exponentiations =", Total )


# In[3]:


def window(a, k):
    
    # conversion en base 2
    b = bin(a)[2:]
    b = b[::-1]
    L = len(b)-1
    
    # precalculation, puissances impaires uniquements
    pre_compute = {1:2, 2:4}
    for i in range(1, 2**(k-1) ) :
        pre_compute[2*i+1] = pre_compute[2*i-1]*pre_compute[2]
    
    mul = len(pre_compute) - 1 # nombre de multiplication utilisé jusqu'ici
    indx_utile, X, i = 1, 1, L

    # lecture des digits de gauche X droite
    while i >= 0 :
        if b[i] == '0':
            # mise au carré
            X = X**2
            mul, i = mul+1, i-1 

        else :
            f = []
            for j in range(k) :
                h = max(i-j,0)
                f.append( (b[h:i+1], h) ) if b[ h ] == '1' else None
            
            # sequence de longeur maximale est retenu
            seq, l = sorted(f, key=lambda x: -len(x[0]) )[0]
            seq = int( seq[::-1], 2 )

            # mise au carré
            for _ in range(i-l+1):
                X = X**2
            mul = mul + (i-l+1) if X > 1 else mul
            
            X = X*pre_compute[ seq ]

            if indx_utile < pre_compute[ seq ] :
                indx_utile = pre_compute[ seq ]
            
            # evite une étape ou l'un des termes est 1
            mul = mul + 1 if X > pre_compute[ seq ]  else mul
            i = l-1
    
    # on retire les précalcules non utilisé
    mul = mul - sum( i > indx_utile for i in pre_compute.values() )
    return mul


# In[4]:


minProd(200)

