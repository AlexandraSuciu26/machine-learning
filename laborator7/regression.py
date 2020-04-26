def calculareaDeterminant(matrice):
    if len(matrice)==2:
        return matrice[0][0]*matrice[1][1]-matrice[0][1]*matrice[1][0]
    else:
        if len(matrice)==3:
            return matrice[0][0]*matrice[1][1]*matrice[2][2]+matrice[0][2]*matrice[1][0]*matrice[2][1]+matrice[2][0]*matrice[0][1]*matrice[1][2]-matrice[0][2]*matrice[1][1]*matrice[2][0]-matrice[0][0]*matrice[2][1]*matrice[1][2]-matrice[2][2]*matrice[1][0]*matrice[0][1]
        
        
def calculareaTranspusei(matrice):
    matriceTranspusa=[]
    for i in range(len(matrice[0])):
        a=[matrice[j][i] for j in range(len(matrice))]  
        matriceTranspusa.append(a)   
    return matriceTranspusa   
def inmultireaMatricilor(matrice1,matrice2):
    matriceaRezultat=[]
    sumaPeLinie=0
    for i in range(len(matrice1)):
        a=[]
        t=0
        while t!=len(matrice2[0]):
            for j in range(len(matrice1[0])):
                z=j
                sumaPeLinie+=matrice1[i][j]*matrice2[z][t]
            a.append(sumaPeLinie)
            t+=1
            sumaPeLinie=0
        matriceaRezultat.append(a)
    return matriceaRezultat
    
def calculareaAdjunctei(matrice):
    matrAdj=[]
    for i in range(len(matrice)):
        matrLini=[]
        for j in range(len(matrice)):
            lin = []
            for k in range(len(matrice)):
                if k==i:
                    continue
                linieDet=[]
                for l in range(len(matrice)):
                    if l==j:
                        continue
                    linieDet.append(matrice[k][l])
                lin.append(linieDet)
            matrLini.append(calculareaDeterminant(lin)*((-1)**(i+j+2)))
        matrAdj.append(matrLini)
    return matrAdj
def calculareaInversei(matricea):
    inversa=[]
    if calculareaDeterminant(matricea)==0:
        print("Determinantul trebuie sa fie diferit de 0!")
        return
    adjuncta=calculareaAdjunctei(calculareaTranspusei(matricea))
    for i in range(len(adjuncta)):
        a=[adjuncta[i][j]/calculareaDeterminant(matricea) for j in range(len(adjuncta))]
        inversa.append(a)
    return inversa

def creareMatrice(inputsGrabLib,inputsProdBrut):
    matrice=[]
    for i in range(len(inputsProdBrut)):
        matrice.append([1,inputsProdBrut[i],inputsGrabLib[i]])
    return matrice

def calculMatriceCoef(matriceSistCoef,matriceOut):
    transp=calculareaTranspusei(matriceSistCoef)
    inmultire=inmultireaMatricilor(transp,matriceSistCoef)
    inv=calculareaInversei(inmultire)
    matrice=inmultireaMatricilor(inv,transp)
    return inmultireaMatricilor(matrice, matriceOut)


'''A=[[1],[4],[7]]
B=[[1,2,1]]
C=inmultireaMatricilor(A,B)
D=calculareaTranspusei(C)
E=[[1,2,1],[4,8,5],[7,1,7]]
print(calculareaDeterminant(E))
print(calculareaInversei([[1,2,1],[4,8,5],[7,1,7]]))'''
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        