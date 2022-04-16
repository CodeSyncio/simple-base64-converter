import base64
from time import sleep
import pyperclip
import os
from linecache import getline as gl

curdir = os.getcwd()

def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear') 

#start of input from config
condir = curdir + '/config.txt'
retsymbol = gl(condir,1).strip()
Timeoutvar = gl(condir,2).strip()
ClipboardSetting = gl(condir,3).strip()
#end of input from config
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
    print('Enter the plain text u wanna encrypt to Base64           ['+str(retsymbol)+' --> back to menu]')
    plaindata = input('\n')
    if plaindata == str(retsymbol):
        return main()
    utf8data = plaindata.encode("UTF-8")
    encodedstring = base64.b64encode(utf8data)
    encodedstringtoutf8 = encodedstring.decode("UTF-8")
    print('Encoded string: \n\n')
    print(encodedstringtoutf8)
    print('\n\nencoded text has been copied to your clipboard, returning in '+Timeoutvar+' sec')
    if ClipboardSetting == 'True':
        pyperclip.copy(encodedstringtoutf8)
    sleep(int(Timeoutvar))
    Encrypt()

def Decrypt():
    cls()
    print('Enter the encoded text that u wanna decode           ['+str(retsymbol)+' --> back to menu]')
    encodedinput = input('\n')
    if encodedinput == str(retsymbol):
        return main()
    encbytes = encodedinput.encode("UTF-8")
    
    d = base64.b64decode(encbytes)
    # Decoding the bytes to string
    finaldecoded = d.decode("UTF-8")
    print('Decoded string: \n\n')
    print(finaldecoded)
    print('\n\ndecoded text has been copied to your clipboard, press enter to continue...')
    if ClipboardSetting == 'True':
        pyperclip.copy(finaldecoded)
    ghosted = input()
    Decrypt()

main()
