def matrixGeneration():
    matrix = [[],[],[],[],[],[]]
    lettersAvail = ["A","B","C","D","E","F",
                    "G","H","I","J","K","L",
                    "M","N","O","P","Q","R",
                    "S","T","U","V","W","X",
                    "Y","Z","1","2","3","4",
                    "5","6","7","8","9"," "]
    key = input("KEY:")
    keyList = []
    for i in key:
        if i.upper() not in keyList:
            keyList.append(i.upper())
    
    matrixLetters=[]
    for i in keyList:
        if i not in matrixLetters:
            matrixLetters.append(i)
    for i in lettersAvail:
        if i not in matrixLetters:
            matrixLetters.append(i)

    for row in matrix:
        for index in range(0,6,1):
            row.append(matrixLetters[0])
            matrixLetters.pop(0)
    return matrix

def search(mat,let):
    for i in range(6):
        for j in range(6):
            if mat[i][j] == let:
                return i,j      #This works 

matrix = matrixGeneration()
letter = "A"
i,j = search(matrix,letter)
print(matrix[i][j])


        
    
