#Concatenar array de strings
def solution(picture):
    anchoOriginal=len(picture[0])
    altoOriginal=len(picture)
    
    print(f"{anchoOriginal} : {altoOriginal}")
    
    resultado= [ '*'*(anchoOriginal+2) for i in range(altoOriginal+2)]
    
    for i in range(altoOriginal):
        resultado[i+1]='*'+picture[i]+'*'
    
    return resultado

#Boolean function if swaping one element in a at most equals b
def solution(a, b):
    position1=-1
    position2=-1
    diferentes=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            diferentes+=1
            if position1==-1:
                position1=i
            else:
                if position2==-1:
                    position2=i
                else:
                    break
    if diferentes==2:
        return a[position1]==b[position2] and a[position2]==b[position1]
    if diferentes==0:
        return True
    return False
