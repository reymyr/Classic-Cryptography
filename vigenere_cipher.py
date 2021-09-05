import io

fullVigenereTable = [
  "NSBEAPLMOHFRVKUIQCJXYZDWGT",
  "VEYKPXHRWODFSUGNAIJTZBMCLQ",
  "MGAXQFVWSZYRLPNEUDBCHITKOJ",
  "QUSYFRCMTXGPJBZOWKLNEHAVDI",
  "EQPVFUXJWBTNOHRAMSIGYCZKDL",
  "GPEVZDXOFTSQAUJBRCWNKILMYH",
  "SPNFXMZBCDIVOYLUJTWHRQAGKE",
  "DVILYGTMUXPQKJAHCBWZONESFR",
  "SDHCXPNOJITAGRLMWZUBKFYVQE",
  "UQFJWDVOBLNYCERMXKSPHZAIGT",
  "YKNHQUSWRCODILJZEAFBMXTGPV",
  "XWSBRTJFYEKZQHPNLDCGMAUVIO",
  "MJRGHKTECLBSXVZOQYDNWPIAFU",
  "RIQWONPJEMGLBUCDKSFYXHAZVT",
  "JWAGCKLVMBZOXPQEUSNYTHIDFR",
  "BKJPEWXFHICMLYANVRUTZSQOGD",
  "CQJMHASEUFWNILKXTYVGBZORPD",
  "MEPYKASWJVGQHUOIBTCRFZDNXL",
  "DUKLRQMECHPGFOIZABYVNXSJWT",
  "AMVYWLSIXKUNDFJORPQTBHGCEZ",
  "OZJPHBQNUMCIYKLTDERFWAXVSG",
  "XGUBYKTLWSMHOVINACJZFDPRQE",
  "CFMYVSEXRGUNWIBOLKHQTPDZJA",
  "NTMWBEDIOHJSKLXFUQRVGCPYAZ",
  "ITXOAHFVSDLWZMPQCNBJYRKGUE",
  "YFUWSAJQHZTBEODRCXMGIVNPKL",
]

# Convert alfabet ke angka (case insensitive, a=A=0...)
def alphabetToInt(char):
  if char.isupper():
    return ord(char) - 65
  else:
    return ord(char) - 97

# Fungsi standard vigenere cypher
def vigenere(inText, key, type="ENC"):
  text = ''.join(filter(str.isalpha, inText))
  if type == "ENC":
    outText = ""
    for i in range(len(text)):
      outText += chr((alphabetToInt(text[i]) + alphabetToInt(key[i % len(key)])) % 26 + 65)
    return outText
  elif type == "DEC":
    outText = ""
    for i in range(len(text)):
      outText += chr((alphabetToInt(text[i]) - alphabetToInt(key[i % len(key)])) % 26 + 65)
    return outText
  else:
    return "Type not valid"

# Fungsi full vigenere cypher
def fullVigenere(inText, key, type="ENC"):
  text = ''.join(filter(str.isalpha, inText))
  if type == "ENC":
    outText = ""
    for i in range(len(text)):
      outText += fullVigenereTable[alphabetToInt(key[i % len(key)])][alphabetToInt(text[i])]
    return outText
  elif type == "DEC":
    outText = ""
    for i in range(len(text)):
      outText += chr(fullVigenereTable[alphabetToInt(key[i % len(key)])].index(text[i]) + 65)
    return outText
  else:
    return "Type not valid"

# Fungsi auto key vigenere cypher
def autoKeyVigenere(inText, key, type="ENC"):
  text = ''.join(filter(str.isalpha, inText))

  if type == "ENC":
    outText = ""
    key += text
    for i in range(len(text)):
      outText += chr((alphabetToInt(text[i]) + alphabetToInt(key[i % len(key)])) % 26 + 65)
    return outText
  elif type == "DEC":
    outText = ""
    for i in range(len(text)):
      outText += chr((alphabetToInt(text[i]) - alphabetToInt(key[i % len(key)])) % 26 + 65)
      key += outText[-1]
    return outText
  else:
    return "Type not valid"

# Fungsi extended vigenere cypher
def extendedVigenere(inText, key, type="ENC"):
  if type == "ENC":
    outText = bytearray()
    for i in range(len(inText)):
      outText.append(((inText[i]) + ord(key[i % len(key)])) % 256)
    return io.BytesIO(outText)
  elif type == "DEC":
    outText = bytearray()
    for i in range(len(inText)):
      outText.append(((inText[i]) - ord(key[i % len(key)])) % 256)
    return io.BytesIO(outText)
  else:
    return "Type not valid"
