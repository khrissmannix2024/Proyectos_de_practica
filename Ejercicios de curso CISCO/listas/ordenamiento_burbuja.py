Lista = [30,12,67,24,1,27,100,-5,98]
activar = True
while activar:
    activar = False
    for i in range(len(Lista)-1):
        if Lista[i] > Lista[i + 1]:
            Lista[i], Lista[i + 1] = Lista[i + 1], Lista[i]
            activar = True
    
print(Lista)