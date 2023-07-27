# Yvonne Aime
# Lab 4 - Challenge 3
# Petey Message Decoder

# Decodes the message
def decrypt(message, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ""
    
    for letter in message:
        if letter in LETTERS:
            value = chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
            translated += value
        else:
            translated += letter
            
    return translated

def main():
    # Welcome Message
    print("Welcome to the Petey Message Decoder")
    print("------------------------------------")
    print("We will be trying to decode messages from Petey.")

    # Open Files
    fread = open("large_file-1.txt","r")
    fwrite = open("answer.txt", "w")

    for l in range(24):
        # Read from file, decypt, and write files. 
        line = fread.readline()
        fwrite.write("Whatever you like to write\n")
        decrypted_line = decrypt(line, 8)
        fwrite.write(decrypted_line)

    # Close Files
    fread.close()
    fwrite.close()


    print("----------------------------")
    print("Done")



main()
