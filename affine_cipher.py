import re
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
prime26 = [1,3,5,7,9,11,15,17,19,21,23,25]

def inversOfXModuloN(x, n):
    a = 1
    while(a%x != 0):
        a+=n
    return (a//x)%n

def encryptCharAffine(m, p, b, n):
    return (m*p+b)%n

def decryptCharAffine(invM, c, b, n):
    return (invM*(c-b))%n

def encryptStringAffine(string, m, b):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    regex_text = re.sub(r'[^a-zA-Z]', '', string).upper()
    result = ""
    for char in regex_text:
        result+= alphabet[encryptCharAffine(m, alphabet.index(char), b, 26)]
    return result

def decryptStringAffine(string, m, b):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = ""
    for char in string:
        result+= alphabet[decryptCharAffine(inversOfXModuloN(m, 26), alphabet.index(char), b, 26)]
    return result

# Main
text = input("Enter plaintext: ")
m = int(input("Enter key: "))
b = int(input("Enter offset: "))

if(m not in prime26 or  b>25 or b<0):
    print("Key is not prime relative to 26 or Offset not in range 0-25")
else:
    enkripsi = encryptStringAffine(text, m, b)
    dekripsi = decryptStringAffine(enkripsi, m, b)
    print(enkripsi)
    print(dekripsi)