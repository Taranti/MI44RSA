from random import*
from math import*
global alph
alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","'","!","?",",","²","&","é","(","-","è","_","ç","à",")","<",">",";",":","~","#","{","[","|","`","^","@","]","}","0","1","2","3","4","5","6","7","8","9"]
def PGCD(a,b):
    c=0
    r=0
    if a>=b:
        for i in range(b):
            c=c+1
            if a/c==int(a/c) and b/c==int(b/c):
                r=c
        return r
    if b>=a:
        for i in range(a):
            c=c+1
            if a/c==int(a/c) and b/c==int(b/c):
                r=c
        return r
    
def primeNumber(a,b):
    if PGCD(a,b)==1:
        return True
    else:
        return False

def nombrePremier(a):
    for i in range(2,int(sqrt(a))+1):
        if a/i==int(a/i):
            return False
    return True
    
def calcExpChiff(phi):
    e=0
    for i in range(2,phi-1):
        if primeNumber(i,phi):
            e=i
    return e

def modulo(a,b):
    c=a%b
    return c
def calcExpDechiff(e,phi):
    d=0
    l=[]
    a=0
    for i in range(phi):
        a=(i*e)%phi
        if a==1:
            l.append(i)
    k=len(l)
    if k==1:
        r=0
    else:
        r=randint(0, k-1)
    d=l[r]
    return(d)




def calcCle():
    #prive=0
    #public=0
    p=randint(1,100)
    while(not nombrePremier(p)):
        p=randint(1,100)
    q=randint(1,100)
    while(not nombrePremier(q)):
        q=randint(1,100)
    n=p*q
    phi=(q-1)*(p-1)
    e=calcExpChiff(phi)
    d=calcExpDechiff(e,phi)
    #if public==1:
        #return (n,e)
    #if prive==1:
        #return(d)
    return(n,e,d)

def codeMess(a,n,e):#n et e de celui qui doit recevoir
    l=[]
    for car in a:
        for i in range(len(alph)):
                      
            if car==alph[i]:
                mess=i
        
        mcode=(mess**e)%n
        l.append(mcode)
    return l

def decodeMess(l,n,d,itera):#n et d de celui qui doit décoder
    md=""
    for i in range(len(l)):
        l[i]=int(l[i])
        j=(l[i]**d)%n
        if j>=len(alph):
            if itera==1:
                main1()
                break
            if itera==2:
                main2()
                break
        md=md+alph[j]
    return(md)

def main1():
    global An,Ae,Ad,Bn,Be,Bd
    An,Ae,Ad=calcCle()
    Bn,Be,Bd=calcCle()
    
    print("Clé publique de A : ",An,Ae)
    print("Clé privée de A : ", Ad)
    print("Clé publique de B : ",Bn,Be)
    print("Clé privée de B : ", Bd)
    print("A envoie le message 'AB?!...")
    l=codeMess("AB?!",Bn,Be)
    print("B reçoit : ",l)
    m=decodeMess(l,Bn,Bd,1)
    
    if m=="AB?!":
        print("B a trouvé 'AB?!'")
        main2()
    else :
        print("Mauvais décodage phase 1")
        print("Veuillez relancer le programme")
    h=input()    
    exit()
    
def main2():
    print("B envoie 'AB OK'")
    l=codeMess("AB OK",An,Ae)
    print("A reçoit : ",l)
    m=decodeMess(l,An,Ad,2)
    if m=="AB OK":
        print("A a trouvé 'AB OK'")
        main3()
    else:
        print("Mauvais décodage phase 2")
        print("Veuillez relancer le programme")

def main3():
    x=randint(1000,9999)
    x=str(x)
    print("A a choisit :", x)
    l=codeMess(x,Bn,Be)
    print("B reçoit :",l)
    y=decodeMess(l,Bn,Bd,2)
    print("B décode et envoie : ",y)
    l=codeMess(y,An,Ae)
    print("A reçoit :",l)
    z=decodeMess(l,An,Ad,2)
    print("A décode : ",z)
    if z==x:
        print("Aucune erreur")
    
main1()
