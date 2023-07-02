#Concatenar array de strings
def solution(picture):
    anchoOriginal=len(picture[0])
    altoOriginal=len(picture)
    
    print(f"{anchoOriginal} : {altoOriginal}")
    
    resultado= [ '*'*(anchoOriginal+2) for i in range(altoOriginal+2)]
    
    for i in range(altoOriginal):
        resultado[i+1]='*'+picture[i]+'*'
    
    return resultado

