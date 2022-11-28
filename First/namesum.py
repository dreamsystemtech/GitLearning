alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
Alphabet = alphabet.upper()

splittedalphabet = {value: key for key, value in enumerate(alphabet, 1)}
Splittedalphabet = {value: key for key, value in enumerate(Alphabet, 1)}

alphabet = Splittedalphabet | splittedalphabet

name = [sign for sign in "Виктор"]

namesum = 0

print (alphabet)
print(name)
