#Playfair Cypher
from string import ascii_uppercase

# Creates the matrix given a keyword.
def matrixGeneration(key): 
    matrix = [[],[],[],[],[],[]]                # Matrix
    # List of available letters
    lettersAvail = ["A","B","C","D","E","F",
                    "G","H","I","J","K","L",
                    "M","N","O","P","Q","R",
                    "S","T","U","V","W","X",
                    "Y","Z","1","2","3","4",
                    "5","6","7","8","9"," "]
    # Empty list to store Key
    keyList = []
    # Loop to add key characters to keyList, only if not already present
    # Also coverts all key charaxters to uppercase                  
    for i in key:
        if i.upper() not in keyList:
            keyList.append(i.upper())
    # Empty list to store letter for matrix generation in order
    matrixLetters=[]
    # Loop through all key elements and append to matrix letters
    for i in keyList:
            matrixLetters.append(i)
    # Iterate through all available letters,
    # if character is not already present add it to matrix letters
    for i in lettersAvail:
        if i not in matrixLetters:
            matrixLetters.append(i)
    # Fill in each row and column of matrix
    for row in matrix:
        for index in range(6):
            row.append(matrixLetters[0])    # Append first letter in list to matrix
            matrixLetters.pop(0)            # Remove first letter from list after
    return matrix                           # Return the finished matrix


#Method to create pairs from the input plaintext string. This method results in a list of pairs that can be used for encryption.
def createPairs(Text):
    textlist = []                           # Empty list to be used to store plaintext letters.
    # Loop to iterate through the input plaintext and append letters to list
    # Also converts to uppercase
    # If the character is "0", replace with "O"
    for j in Text:
        if j == "0":
            textlist.append("O")
        else:
            textlist.append(j.upper())
    
    pairs = []                              # Empty list to store pairs
    while len(textlist) != 0:               # loops through the plaintext letters list until its empty
        if len(textlist) == 1:              # If the textlist is down to just one letter, it needs an "X" as a pair
            pairs.append(textlist[0]+"X")   # Append the last letter + "X" to the pairs list
            textlist.pop(0)                 # Remove the list element at index 0
        else:
            if textlist[0] == textlist[1]:  # If the list is not on its last element, and elements that will be grouped are the same
                pairs.append(textlist[0]+"X")# Append the first letter of the pair and add "X"
                textlist.pop(0)             # Remove only the first letter from the list
                                            # Second occurance of the letter stays in the list to be added to next pair
            else:                           # If the entries are not the same, and there is more than one entry in the list
                pairs.append(textlist[0]+textlist[1])# Append both entries to the pairs list, together
                textlist.pop(0)             # Remove first letter from remaining list   
                textlist.pop(0)             # Remove second letter from remaining list         
    return pairs                            # Method return a list of pairs

# Loops through the matrix to get the index of a letter
# Function takes a matrix and letter as input
def getIndex(mat, lett):
    for y in range(6):      # Loops through all columns of matrix
        for x in range(6):  # Loops through all rows/elements in column
            # If the letter in the matrix at the current coordinates are the
            # same as the input letter, return those coordinates
            if mat[y][x] == lett:
                return y,x

# Method will encode pairs depending on their location in the 6x6 matrix
# Function takes matrix list and pairs list as input, returns Encoded message
def encode(matrix,pairs):
    encodedString = ""
    for element in pairs:
        # Split the pair into its individual letters
        e1 = element[0] # First Letter
        e2 = element[1] # Second letter

        y1,x1 = getIndex(matrix,e1) # coordinates of first letter
        y2,x2 = getIndex(matrix,e2) # coordinates of second letter

        # If the letters of a pair are in the same column, the letter below is used
        if y1 == y2:
            encodedString+=(matrix[y1][x1-5]+matrix[y2][x2-5])
        # If the letters of a pair are in the same row, the letter to the right is used
        elif x1 == x2:
            encodedString+=(matrix[y1-5][x1]+matrix[y2-5][x2])
        # If the letters are not in the same row or column, swap the x coordinates
        else:
            encodedString+=(matrix[y1][x2]+matrix[y2][x1])
    return encodedString

def main():
    keyIn = input("KEY:")               # Take key from terminal input
    plaintextIn = input("PLAINTEXT:")   # Take plaintext from terminal
    m6X6 = matrixGeneration(keyIn)      # Pass key to matrix generation function
    pList = createPairs(plaintextIn)    # Pass plaintext to pair creation funtion
    eMessage = encode(m6X6,pList)       # Call encoding message and pass it the matrix and pairs
    print("Encoded Message:",eMessage)   # print the encoded message to terminal
    
main()  # Call main function