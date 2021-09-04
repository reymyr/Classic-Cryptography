from flask import Flask, render_template, request, send_file
from playfair_cipher import getKeywordMatrices, textToBigramArray, encipherBigram, decipherBigram, encipherBigramToText, decipherBigramToText
from affine_cipher import encryptStringAffine, decryptStringAffine
from vigenere_cipher import vigenere, autoKeyVigenere, fullVigenere, extendedVigenere
from hill_cipher import textToArray, encryptHill, decryptHill, formKeyMatricesFromInput
import io
import re

app = Flask(__name__)

def display5LetterGroup(text):
    result = re.findall('.{1,5}', text)
    result = ' '.join(result)
    return result

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vigenere/standard/encrypt", methods=['POST','GET'])
def standardVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        cipher_text = vigenere(text, keyword)
        display = request.form['inlineRadio']
        if(display=="option2"):
            cipher_text = display5LetterGroup(cipher_text)
        return render_template("vigenere.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text, display=display)
    else:
        return render_template("vigenere.html", mode="Encrypt", display="option1")

@app.route("/vigenere/standard/decrypt", methods=['POST','GET'])
def standardVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        plain_text = vigenere(text, keyword, type="DEC")
        display = request.form['inlineRadio']
        if(display=="option2"):
            plain_text = display5LetterGroup(plain_text)
        return render_template("vigenere.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=plain_text, display=display)
    else:
        return render_template("vigenere.html", mode="Decrypt", display="option1")

@app.route("/vigenere/full/encrypt", methods=['POST','GET'])
def fullVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        cipher_text = fullVigenere(text, keyword)
        display = request.form['inlineRadio']
        if(display=="option2"):
            cipher_text = display5LetterGroup(cipher_text)
        return render_template("full_vigenere.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text, display=display)
    else:
        return render_template("full_vigenere.html", mode="Encrypt", display="option1")

@app.route("/vigenere/full/decrypt", methods=['POST','GET'])
def fullVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        plain_text = fullVigenere(text, keyword, type="DEC")
        display = request.form['inlineRadio']
        if(display=="option2"):
            plain_text = display5LetterGroup(plain_text)
        return render_template("full_vigenere.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=plain_text, display=display)
    else:
        return render_template("full_vigenere.html", mode="Decrypt", display="option1")

@app.route("/vigenere/autokey/encrypt", methods=['POST','GET'])
def autokeyVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        cipher_text = autoKeyVigenere(text, keyword)
        display = request.form['inlineRadio']
        if(display=="option2"):
            cipher_text = display5LetterGroup(cipher_text)
        return render_template("autokey_vigenere.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text, display=display)
    else:
        return render_template("autokey_vigenere.html", mode="Encrypt", display="option1")

@app.route("/vigenere/autokey/decrypt", methods=['POST','GET'])
def autokeyVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']

        plain_text = autoKeyVigenere(text, keyword, type="DEC")
        display = request.form['inlineRadio']
        if(display=="option2"):
            plain_text = display5LetterGroup(plain_text)
        return render_template("autokey_vigenere.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=plain_text, display=display)
    else:
        return render_template("autokey_vigenere.html", mode="Decrypt", display="option1")

@app.route("/vigenere/extended/encrypt", methods=['POST','GET'])
def extendedVigenereEncrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        file = request.files['file']
        file_contents = file.read()
        filename = file.filename

        cipher_file = extendedVigenere(file_contents, keyword)

        return send_file(cipher_file, as_attachment=True, attachment_filename="encrypted-"+filename)
    else:
        return render_template("extended_vigenere.html", mode="Encrypt")

@app.route("/vigenere/extended/decrypt", methods=['POST','GET'])
def extendedVigenereDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        file = request.files['file']
        file_contents = file.read()
        filename = file.filename

        cipher_file = extendedVigenere(file_contents, keyword, type="DEC")

        return send_file(cipher_file, as_attachment=True, attachment_filename="decrypted-"+filename)
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
        display = request.form['inlineRadio']
        if(display=="option2"):
            cipher_text = display5LetterGroup(cipher_text)
        return render_template("playfair.html", mode="Encrypt", keyword=keyword, plaintext=text, result=cipher_text, display=display)
    else:
        return render_template("playfair.html", mode="Encrypt", display="option1")

@app.route("/playfair/decrypt", methods=['POST','GET'])
def playfairDecrypt():
    if request.method == 'POST':
        keyword = request.form['text1']
        text = request.form['text2']
        matrix = getKeywordMatrices(keyword)
        decipher_array = decipherBigram(matrix, textToBigramArray(text))
        decipher_text = decipherBigramToText(decipher_array)
        display = request.form['inlineRadio']
        if(display=="option2"):
            decipher_text = display5LetterGroup(decipher_text)
        return render_template("playfair.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=decipher_text, display=display)
    else:
        return render_template("playfair.html", mode="Decrypt", display="option1")

@app.route("/affine/encrypt", methods=['POST','GET'])
def affineEncrypt():
    offset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    coprime = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if request.method == 'POST':
        text = request.form['text2']
        m = int(request.form['select1'])
        b = int(request.form['select2'])
        cipher_text = encryptStringAffine(text, m, b)
        display = request.form['inlineRadio']
        if(display=="option2"):
            cipher_text = display5LetterGroup(cipher_text)
        return render_template("affine.html", mode="Encrypt", offset=offset, coprime=coprime, plaintext=text, result=cipher_text, m=m, b=b, display=display)
    else:
        return render_template("affine.html", mode="Encrypt", offset=offset, coprime=coprime, display="option1")

@app.route("/affine/decrypt", methods=['POST','GET'])
def affineDecrypt():
    offset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    coprime = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if request.method == 'POST':
        text = request.form['text2']
        m = int(request.form['select1'])
        b = int(request.form['select2'])
        decipher_text = decryptStringAffine(text, m, b)
        display = request.form['inlineRadio']
        if(display=="option2"):
            decipher_text = display5LetterGroup(decipher_text)
        return render_template("affine.html", mode="Decrypt", offset=offset, coprime=coprime, ciphertext=text, result=decipher_text, m=m, b=b, display=display)
    else:
        return render_template("affine.html", mode="Decrypt", offset=offset, coprime=coprime, display="option1")

@app.route("/hill/encrypt", methods=['POST','GET'])
def hillEncrypt():
    if request.method == 'POST':
        n = int(request.form['text1'])
        array = request.form['text2']
        entries = list(map(int, array.split()))
        text = request.form['text3']
        matrices= formKeyMatricesFromInput(entries, n)
        cipher_text = encryptHill(matrices, textToArray(text, n), n)
        display = request.form['inlineRadio']
        if(display=="option2"):
            cipher_text = display5LetterGroup(cipher_text)
        return render_template("hill.html", mode="Encrypt", plaintext=text, result=cipher_text, n=n, array=array, display=display)
    else:
        return render_template("hill.html", mode="Encrypt", display="option1")

@app.route("/hill/decrypt", methods=['POST','GET'])
def hillDecrypt():
    if request.method == 'POST':
        n = int(request.form['text1'])
        array = request.form['text2']
        entries = list(map(int, array.split()))
        text = request.form['text3']
        matrices= formKeyMatricesFromInput(entries, n)
        decipher_text = decryptHill(matrices, textToArray(text, n), n)
        display = request.form['inlineRadio']
        if(display=="option2"):
            decipher_text = display5LetterGroup(decipher_text)
        return render_template("hill.html", mode="Decrypt", ciphertext=text, result=decipher_text, n=n, array=array, display=display)
    else:
        return render_template("hill.html", mode="Decrypt", display="option1")

@app.route("/saveresult", methods=['POST'])
def saveResult():
    result = request.form['result']

    return send_file(io.BytesIO(result.encode()), mimetype="text/plain",as_attachment=True, attachment_filename="result.txt")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,threaded=True)
