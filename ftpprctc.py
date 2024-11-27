import os
import shutil
import paramiko
ssh_client = paramiko.SSHClient()
host = "demo.wftpserver.com"
username = "demo"
password = "demo"
port = 2222

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=host,port=port,username=username,password=password)

print('connection established successfully') 

ftp = ssh_client.open_sftp()

files = ftp.listdir("download")
print(files)
for i, file in enumerate(files):

   ftp.get(f'/download/{file}', f'C:/Users/adebb/destination_bami/{file}')

   print(f'Moved {file}')
   print(f'no of files pulled {i}')

    

print("Listing all the files and Directory: ",files)

ssh_client.close()
