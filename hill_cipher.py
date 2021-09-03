import numpy as np
import re
from sympy import Matrix

def inversOfXModuloN(x, n):
    a = 1
    while(a%x != 0):
        a+=n
    return (a//x)%n
    
def formKeyMatricesFromInput(entry, n):
    matrices= np.array(entry).reshape(n, n)
    return matrices

def textToArray(text, n):
    regex_text = re.sub(r'[^a-zA-Z]', '', text).upper()
    if(len(regex_text)%n != 0):
        regex_text+='X'*(n-(len(regex_text)%n))
    res = [regex_text[i:i+n] for i in range(0, len(regex_text), n)]
    return res

def encryptHill(matrices, arr, n):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    text = ""
    for x in arr:
        current = []
        for i in range(n):
            current.append(alphabet.index(x[i]))
        encryptCurr = np.matmul(matrices, np.array(current)).tolist()
        for i in range(n):
            text+=alphabet[encryptCurr[i]%26]
    return text

def inverseModMatrices(matrices, n):
    pre_inverse1 = matrices.flatten().tolist()
    pre_inverse2 = Matrix(n, n, pre_inverse1)
    pre_inverse3 = pre_inverse2.inv_mod(26)
    inverse = np.array(pre_inverse3)
    return inverse

def decryptHill(matrices, arr, n):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    text = ""
    inverse = inverseModMatrices(matrices, n)
    for x in arr:
        current = []
        for i in range(n):
            current.append(alphabet.index(x[i]))
        encryptCurr = np.matmul(inverse, np.array(current)).tolist()
        for i in range(n):
            text+=alphabet[encryptCurr[i]%26]
    return text

# Main
# n = int(input("Enter the number of linear equation (matrix size): "))
# print("Enter the entries in a single line (separated by space): ")
# entries = list(map(int, input().split()))
# text = input("Enter plaintext: ")
# matrices= formKeyMatricesFromInput(entries, n)
# encryptText = encryptHill(matrices, textToArray(text, n), n)
# print(encryptText)
# print(decryptHill(matrices, textToArray(encryptText, n), n))

