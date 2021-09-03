from flask import Flask, render_template, url_for, request, redirect
from playfair_cipher import getKeywordMatrices, textToBigramArray, encipherBigram, decipherBigram, encipherBigramToText, decipherBigramToText
from affine_cipher import encryptStringAffine, decryptStringAffine
from vigenere_cipher import vigenere, autoKeyVigenere, fullVigenere, extendedVigenere

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vigenere/standard/encrypt", methods=['POST','GET'])
def standardVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        cipher_text = vigenere(text, keyword)
        
        return render_template("vigenere.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text)
    else:
        return render_template("vigenere.html", mode="Encrypt")

@app.route("/vigenere/standard/decrypt", methods=['POST','GET'])
def standardVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        plain_text = vigenere(text, keyword, type="DEC")
        
        return render_template("vigenere.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=plain_text)
    else:
        return render_template("vigenere.html", mode="Decrypt")

@app.route("/vigenere/full/encrypt", methods=['POST','GET'])
def fullVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        cipher_text = fullVigenere(text, keyword)
        
        return render_template("full_vigenere.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text)
    else:
        return render_template("full_vigenere.html", mode="Encrypt")

@app.route("/vigenere/full/decrypt", methods=['POST','GET'])
def fullVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        plain_text = fullVigenere(text, keyword, type="DEC")
        
        return render_template("full_vigenere.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=plain_text)
    else:
        return render_template("full_vigenere.html", mode="Decrypt")

@app.route("/vigenere/autokey/encrypt", methods=['POST','GET'])
def autokeyVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        cipher_text = autoKeyVigenere(text, keyword)
        
        return render_template("autokey_vigenere.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text)
    else:
        return render_template("autokey_vigenere.html", mode="Encrypt")

@app.route("/vigenere/autokey/decrypt", methods=['POST','GET'])
def autokeyVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        plain_text = autoKeyVigenere(text, keyword, type="DEC")
        
        return render_template("autokey_vigenere.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=plain_text)
    else:
        return render_template("autokey_vigenere.html", mode="Decrypt")

@app.route("/vigenere/extended/encrypt", methods=['POST','GET'])
def extendedVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        cipher_text = extendedVigenere(text, keyword)
        
        return render_template("extended_vigenere.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text)
    else:
        return render_template("extended_vigenere.html", mode="Encrypt")

@app.route("/vigenere/extended/decrypt", methods=['POST','GET'])
def extendedVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        plain_text = extendedVigenere(text, keyword, type="DEC")
        
        return render_template("extended_vigenere.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=plain_text)
    else:
        return render_template("extended_vigenere.html", mode="Decrypt")

@app.route("/playfair/encrypt", methods=['POST','GET'])
def playfairEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        matrix = getKeywordMatrices(keyword)
        cipher_array = encipherBigram(matrix, textToBigramArray(text))
        cipher_text = encipherBigramToText(cipher_array)
        
        return render_template("playfair.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text)
    else:
        return render_template("playfair.html", mode="Encrypt")

@app.route("/playfair/decrypt", methods=['POST','GET'])
def playfairDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        matrix = getKeywordMatrices(keyword)
        decipher_array = decipherBigram(matrix, textToBigramArray(text))
        decipher_text = decipherBigramToText(decipher_array)
        
        return render_template("playfair.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=decipher_text)
    else:
        return render_template("playfair.html", mode="Decrypt")

@app.route("/affine/encrypt", methods=['POST','GET'])
def affineEncrypt():
    offset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    coprime = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if request.method == 'POST':
        text = request.form['text2']
        m = int(request.form['select1'])
        b = int(request.form['select2'])
        cipher_text = encryptStringAffine(text, m, b)
        
        return render_template("affine.html", mode="Encrypt", offset=offset, coprime=coprime, plaintext=text, result=cipher_text, m=m, b=b)
    else:
        return render_template("affine.html", mode="Encrypt", offset=offset, coprime=coprime)

@app.route("/affine/decrypt", methods=['POST','GET'])
def affineDecrypt():
    offset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    coprime = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if request.method == 'POST':
        text = request.form['text2']
        m = int(request.form['select1'])
        b = int(request.form['select2'])
        cipher_text = decryptStringAffine(text, m, b)
        
        return render_template("affine.html", mode="Decrypt", offset=offset, coprime=coprime, ciphertext=text, result=cipher_text, m=m, b=b)
    else:
        return render_template("affine.html", mode="Decrypt", offset=offset, coprime=coprime)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,threaded=True)
