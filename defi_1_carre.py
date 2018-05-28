
# coding: utf-8

# In[1]:


from math import sqrt


# l'approche utilisée consiste à éliminer tous les éléments de l'interval ayant un facteur premier qui ne se repete pas sur tous l'interval

# In[2]:


def factorialise(n):
    # retourne la liste des facteurs premier d'un entier n
    i = 2
    factors = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    
    if n > 1:
        factors.append(n)
    
    return factors


# In[3]:


def clean(a, b):
    # check tous les facteur premier de tous les nombres à la fois et élimine ceux qui ne se repete pas.
    
    fact  = ( factorialise(i) for i in range(a, b+1) )
    merge = [ i for sub in fact for i in sub ] # fusionne les listes de facteur
    
    repeat  = set()
    cleaned = []

    # compte les occurences et retiens ceux qui n'occure qu'une fois
    for i in set(merge):
        if merge.count(i) == 1 :
            repeat.add(i)
    
    # élimine tous les éléments contenant un facteur non repeté
    for i in range(a, b+1) :
        k = set( factorialise(i) )
        
        if len( k&repeat ) == 0 :
            cleaned.append(i)

    return cleaned


# In[4]:


def power_set(A):
    # crée la power set (ensemble de tous les sous ensemble possible) de A

    P = [set()]

    for element in A:
        e =  { element }
        P += [ sub_set | e for sub_set in P ]

    return P[1:] # élimine l'ensemble vide


# In[5]:


def C(a, b): # la fonction principal
    
    A = clean(a, b)
    squares = 0

    # calcule du produit de chauque sous ensemble i
    for i in power_set( A ) :
        
        p = 1
        for j in i :
            p *= j

        # si c'est un carré parfait on ajoute 1 au total
        if not sqrt(p)%1 :
            squares += 1

    print( "Nombre de carrés parfaits formés =", squares )


# In[6]:


C(5, 10)

