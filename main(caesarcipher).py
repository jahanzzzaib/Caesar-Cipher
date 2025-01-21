alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                    
''')


def caesar():
    def encrypt(original_text, shift_amount):
        encoded_text = ""
        for letter in original_text:
            if letter not in alphabet:
                encoded_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                encoded_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {encoded_text}")

    def decrypt(original_text, shift_amount):
        decoded_text = ""
        for letter in original_text:
            if letter not in alphabet:
                decoded_text += letter
            else:
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                decoded_text += alphabet[shifted_position]
        print(f"Here is the decoded result: {decoded_text}")

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type your shift number:\n"))

    caesar()

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "yes":
        should_continue = True
    elif restart == "no":
        print("Goodbye!")
        should_continue = False
