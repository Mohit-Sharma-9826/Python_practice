print("Welcome to the Caesar Cipher!\n")

task = input("Type 'encode' to encript or type 'decode' to decript: ")
if task not in ["encode", "decode"]:
    print("Enter wrong input")

msg = input("Enter your message: ")
shift = int(input("Enter shift number: "))

new_msg = ""
for i in range(len(msg)):
    if task == "encode":
        n = ord(msg[i]) + shift
    elif task == "decode":
        n = ord(msg[i]) - shift
    new_msg += chr(n)
        
print("Your is encoded: ", new_msg)