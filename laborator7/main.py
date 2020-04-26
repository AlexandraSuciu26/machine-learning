'''
Created on 25 apr. 2020

@author: Alexandraah
'''
import csv
import os
import random
from regression import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def loadData(fileName, inputVariaProdIntBrut,inputVariableGradLib, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariableGradLib = dataNames.index(inputVariableGradLib)
    inputsGradLib = [float(data[i][selectedVariableGradLib]) for i in range(len(data))]

    selectedVariableProdBrut = dataNames.index(inputVariaProdIntBrut)
    inputsProdBrut = [float(data[i][selectedVariableProdBrut]) for i in range(len(data))]

    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

    return inputsProdBrut,inputsGradLib, outputs

def nrTeste(inputsGradLib,inputsProdBrut,outputs):
    inputTestLib=[]
    inputTestProd=[]
    nrT=0.2*len(inputsProdBrut)

    for _ in range(int(nrT)):
        ra=random.randrange(len(inputsProdBrut)-1)
        print("Random:"+str(ra))
        inputTestLib.append(inputsGradLib[ra])
        inputTestProd.append(inputsProdBrut[ra])
        inputsGradLib.pop(ra)
        inputsProdBrut.pop(ra)
        outputs.pop(ra)
    return inputTestLib,inputTestProd

def citire():
    filePath = os.path.join( 'C:\\@Alexandra\\anul2\\semestrul2\\ai\\lab\\laborator7\\world-happiness-report-2017.txt')
    return loadData(filePath, 'Economy..GDP.per.Capita.','Freedom', 'Happiness.Score')

#date antrenament
inputsProdBrut,inputsGradLib,outputs=citire()

max_prod=max(inputsProdBrut)
max_lib=max(inputsGradLib)

#date test
inputTestareGradLib,inputTestareProdBrut=nrTeste(inputsGradLib,inputsProdBrut,outputs)


matriceSistCoef=creareMatrice(inputsGradLib,inputsProdBrut)
matriceOut=[[outputs[i]] for i in range(len(outputs))]
rezultat=calculMatriceCoef(matriceSistCoef,matriceOut)
print("Matricea de coeficienti:"+str(rezultat))
fig = plt.figure()
ax = plt.axes(projection='3d')
for i in range(0,len(inputsProdBrut)):
    plt.plot([outputs[i]],[inputsProdBrut[i]],[inputsGradLib[i]],'ro')
for i in range(0,len(inputTestareGradLib)):
    predict=rezultat[0][0]+rezultat[1][0]*inputTestareProdBrut[i]+rezultat[2][0]*inputTestareGradLib[i]
    plt.plot([predict],inputTestareProdBrut[i],inputTestareGradLib[i],'b^')

y1=rezultat[0][0]
y2=predict=rezultat[0][0]+rezultat[1][0]*max_prod+rezultat[2][0]*max_lib
plt.plot([y1,y2],[0,max_prod],[0,max_lib])
plt.show()

