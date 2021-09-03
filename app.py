from flask import Flask, render_template, url_for, request, redirect
from playfair_cipher import getKeywordMatrices, addXToRepeatedChar, textToBigramArray, searchMatrixIndex, encipherBigram, decipherBigram, encipherBigramToText, decipherBigramToText


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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
        decipher_text = encipherBigramToText(decipher_array)
        
        return render_template("playfair.html", mode="Decrypt", keyword=keyword, ciphertext=text, result=decipher_text)
    else:
        return render_template("playfair.html", mode="Decrypt")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,threaded=True)
