alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
Alphabet = alphabet.upper()

splittedalphabet = {value: key for key, value in enumerate(alphabet, 1)}
Splittedalphabet = {value: key for key, value in enumerate(Alphabet, 1)}

alphabet = Splittedalphabet | splittedalphabet




if __name__ == '__main__':
    namesum = 0
    name = input('Как тебя звать? ')
    splitedname = [sign for sign in name]
    print(splitedname)
    for letter in splitedname:
        namesum = namesum + alphabet[letter]
        print(namesum)