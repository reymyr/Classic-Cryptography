import re
from collections import OrderedDict 

def getKeywordMatrices(keyword):
    alphabet = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    regex_keyword = re.sub(r'[^a-zA-Z]', '', keyword).upper()
    regex_keyword_wo_j = re.sub(r'[J]', '', regex_keyword)
    unique_capital_keyword = ''.join(OrderedDict.fromkeys(regex_keyword_wo_j))

    i,j,k=0,0,0

    matrix = [['-' for i in range(5)] for j in range(5)]
    while i < 5:
        while j<5:
            if((i*5)+j+1)<=len(unique_capital_keyword):
                matrix[i][j] = unique_capital_keyword[i*5+j]
                j+=1
            else:
                if(alphabet[k] not in (item for sublist in matrix for item in sublist)):
                    matrix[i][j] = alphabet[k]
                    j+=1
                k+=1
        j=0
        i+=1
    return matrix

def addXToRepeatedChar(text) :
    return 'X'.join(text[i:i+1] for i in range(0, len(text)))

def textToBigramArray(text):
    regex_text = re.sub(r'[^a-zA-Z]', '', text).upper()
    regex_text_wo_j = re.sub(r'[J]', 'I', regex_text)

    array_of_repeated = [m.group(0) for m in re.finditer(r'(.)\1*', regex_text_wo_j)]
    bigram_text = ""
    for x in array_of_repeated:
        if(len(x)>1):
            bigram_text+=addXToRepeatedChar(x)
        else:
            bigram_text+=x
    if(len(bigram_text)%2==1):
        bigram_text+="X"
    bigram_array = [bigram_text[i:i+2] for i in range(0, len(bigram_text), 2)]
    return bigram_array

def searchMatrixIndex(char, matrix):
    for i in range(5):
        for j in range(5):
            if(matrix[i][j]==char):
                return [i, j]

def encipherBigram(matrix, bigramArray):
    cipher_array = []
    for bigram in bigramArray:
        index1 = searchMatrixIndex(bigram[0], matrix)
        index2 = searchMatrixIndex(bigram[1], matrix)
        if(index1[0]==index2[0]):
            res = matrix[index1[0]][(index1[1]+1)%5]+matrix[index2[0]][(index2[1]+1)%5]
            cipher_array.append(res)
        elif(index1[1]==index2[1]):
            res = matrix[(index1[0]+1)%5][index1[1]]+matrix[(index2[0]+1)%5][index2[1]]
            cipher_array.append(res)
        else:
            res = matrix[index1[0]][index2[1]]+matrix[index2[0]][index1[1]]
            cipher_array.append(res)
    return cipher_array

def decipherBigram(matrix, bigramArray):
    decipher_array = []
    for bigram in bigramArray:
        index1 = searchMatrixIndex(bigram[0], matrix)
        index2 = searchMatrixIndex(bigram[1], matrix)
        if(index1[0]==index2[0]):
            res = matrix[index1[0]][(index1[1]-1)%5]+matrix[index2[0]][(index2[1]-1)%5]
            decipher_array.append(res)
        elif(index1[1]==index2[1]):
            res = matrix[(index1[0]-1)%5][index1[1]]+matrix[(index2[0]-1)%5][index2[1]]
            decipher_array.append(res)
        else:
            res = matrix[index1[0]][index2[1]]+matrix[index2[0]][index1[1]]
            decipher_array.append(res)
    return decipher_array

def decipherBigramToText(decipherArray):
    for i in range (len(decipherArray)):
        if(decipherArray[i].count('X') == 1):
            decipherArray[i] = re.sub(r'[X]', '', decipherArray[i])
        elif(decipherArray[i].count('X') == 2):
            decipherArray[i] = "X"
    return ''.join(decipherArray)


# Main
keyword = input("Enter keyword: ")
text = input("Enter plaintext: ")

matrix = getKeywordMatrices(keyword)
cipher_array = encipherBigram(matrix, textToBigramArray(text))
decipher_array = decipherBigram(matrix, cipher_array)
decipher_text = decipherBigramToText(decipher_array)


print(cipher_array)
print(decipher_array)
print(decipher_text)