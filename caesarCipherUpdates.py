from caesarCipherArt import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shouldContinue = True

def caesarCipher(cipher_direction,cipher_text,cipher_shift) :
    massege=""
    for alpha in cipher_text :
        if alpha in alphabet :
            indexOfAlpha = alphabet.index(alpha)
            if cipher_direction =="decode":
                cipher_shift *= -1
            new_IndexOf_Alpha = indexOfAlpha+cipher_shift
            massege = massege+alphabet[new_IndexOf_Alpha]
        else :
            massege = massege + alpha
    return massege

while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>25 :
        shift = shift%26
    
    massege=caesarCipher(cipher_direction=direction,cipher_text=text,cipher_shift=shift)
    print(f"Your {direction}d text is {massege}")
    again = input("Are you want to continue (yes/no)")
    if again == "no" :
        shouldContinue=False
        print("Thank you for choosing us")