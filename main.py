import base64
from time import sleep
import pyperclip
import os
def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear') 

def main():
    cls()
    print('Choose an option\n\n')
    print('[1] Encrypt')
    print('[2] Decrypt')
    
    optchosen = input('\n')
    
    if optchosen == '1':
        Encrypt()
        
    elif optchosen == '2':
        Decrypt()
        
    elif optchosen != '1' or '2':
        return main()
    
def Encrypt():
    cls()
    print('Enter the plain text u wanna encrypt to Base64           [§ --> back to menu]')
    plaindata = input('\n')
    if plaindata == '§':
        return main()
    utf8data = plaindata.encode("UTF-8")
    encodedstring = base64.b64encode(utf8data)
    encodedstringtoutf8 = encodedstring.decode("UTF-8")
    print('Encoded string: \n\n')
    print(encodedstringtoutf8)
    print('\n\nencoded text has been copied to your clipboard, returning in 2sec')
    pyperclip.copy(encodedstringtoutf8)
    sleep(2)
    Encrypt()

def Decrypt():
    cls()
    print('Enter the encoded text that u wanna decode           [§ --> back to menu]')
    encodedinput = input('\n')
    if encodedinput == '§':
        return main()
    encbytes = encodedinput.encode("UTF-8")
    
    d = base64.b64decode(encbytes)
    # Decoding the bytes to string
    finaldecoded = d.decode("UTF-8")
    print('Decoded string: \n\n')
    print(finaldecoded)
    print('\n\ndecoded text has been copied to your clipboard, press enter to continue...')
    pyperclip.copy(finaldecoded)
    ghosted = input()
    Decrypt()

main()
