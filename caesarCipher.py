# import caesarCipherArt
# print(caesarCipherArt.logo)
from caesarCipherArt import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# if shift>25 :
#     shift = shift%26
# if direction=="encode":
#     massege = encodeMassege(text,shift)
#     print(f"Your secret code is {massege}")
# elif direction=="decode":
#     massege = decodeMassege(text,shift)
#     print(f"Your secret code is {massege}")
# else :
#     print("please entered wrong input")

def encodeMassege(text,shift) :
        enAlphabet = []
        encodedmassege = ""
        for i in range(shift,len(alphabet)) :
            enAlphabet.append(alphabet[i])
        for i in range(0,shift) :
            enAlphabet.append(alphabet[i])

        for alpha in text:
            if alpha in alphabet:
                indexOfAlpha=alphabet.index(alpha)
                encodedmassege = encodedmassege+enAlphabet[indexOfAlpha]
            else :
                encodedmassege=encodedmassege+alpha
        return encodedmassege

def decodeMassege(text,shift) :
        deAlphabet = []
        decodedmassege = ""
        for i in range(shift,len(alphabet)) :
            deAlphabet.append(alphabet[i])
        for i in range(0,shift) :
            deAlphabet.append(alphabet[i])
        for alpha in text:
            if alpha in deAlphabet :
                indexOfAlpha=deAlphabet.index(alpha)
                decodedmassege = decodedmassege+alphabet[indexOfAlpha]
            else :
                decodedmassege =decodedmassege+alpha
        return decodedmassege

# if direction=="encode":
#     massege = encodeMassege(text,shift)
#     print(f"Your secret code is {massege}")
# elif direction=="decode":
#     massege = decodeMassege(text,shift)
#     print(f"Your secret code is {massege}")
# else :
#     print("please entered wrong input")
shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>25 :
        shift = shift%26
    if direction=="encode":
        massege = encodeMassege(text,shift)
        print(f"Your secret code is {massege}")
    elif direction=="decode":
        massege = decodeMassege(text,shift)
        print(f"Your secret code is {massege}")
    else :
        print("please entered wrong input")
    again = input("Are you want to continue (yes/no)")
    if again == "no" :
        shouldContinue=False
        print("Thank you for choosing us")

