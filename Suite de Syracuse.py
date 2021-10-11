def syracuse(s0, n):
    s = s0
    k =0
    while k<n:
        if s%2==0:
            s=s/2
        else:
            s=3*s+1
        k+=1
    return s

def syracuseListe(s0, n):
    s = s0
    s_liste = [s0]
    k =0
    while k<n:
        if s%2==0:
            s=s/2
        else:
            s=3*s+1
        s_liste.append(s)
        k+=1
    return s_liste

def syracuseTemps(s0):
    n = 0
    while syracuse(s0, n) != 1:
        n += 1
    return n+1

def syracuseHauteur(s0):
    n = syracuseTemps(s0)
    return max(syracuseListe(s0, n))
