alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)    

def decrypt(cipher_text,shift_amount):
    plaain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plaain_text += new_letter
    print(plaain_text)

direction = input(" type encode to encrypt typr decode yo decrypt \n")
text = input("type your massage").lower()
shift = int (input("type the shift number"))
shift = shift % 25

if direction == "encrypt":
    encrypt(plain_text = text ,shift_amount = shift)              
elif direction == "decrypt":
    decrypt(cipher_text= text ,shift_amount = shift)        

