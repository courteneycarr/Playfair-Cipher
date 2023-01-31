#Method to create pairs from the input plaintext. This method results in a list of pairs that can be used for encryption.
def createPairs(Text):
    textlist = []                           # Empty list to be used to store plaintext letters.
    # Loop to iterate through the input plaintext and append letters to list
    for j in Text:
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

matrix = [[1,2,3,4],[5,6,7,8]]
print(matrix[0-1][0])