import os
from cryptography.fernet import Fernet

user_path_ = r'C:\Users\User\source\malware'
encrypted_list = []
encrypted_list_path = []

for i in os.listdir(user_path_):
    if os.path.isfile(os.path.join(user_path_,i)) == True:
        with open(os.path.join(user_path_,i),'rb') as reader:
            encrypted_list.append(reader.read())
print(encrypted_list)

decrypted_list = []
for i in encrypted_list:
    with open('file4.txt','rb') as keyreader:
        decrypter = Fernet(keyreader.read()).decrypt(i)
        decrypted_list.append(decrypter.decode('UTF-8'))

for i in decrypted_list:
    print(i)

for i in os.listdir(user_path_):
    if os.path.isfile(os.path.join(user_path_,i)) == True:
        encrypted_list_path.append(i)

print(encrypted_list_path)

for i in encrypted_list_path:
    with open(os.path.join(user_path_,i),'w') as write_to_file:
        write_to_file.write(decrypted_list[encrypted_list_path.index(i)])
        


        
