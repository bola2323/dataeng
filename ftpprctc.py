import paramiko

# create ssh client 
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "demo.wftpserver.com"
username = "demo"
password = "demo"
port = 2222

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

# create an SFTP client object
ftp = ssh_client.open_sftp()

# download a file from the remote server
files = ftp.put(f'C:/Users/adebb/source_folder/crime_rates.csv',f"/upload/crime_rates.csv")
print("files")

# close the connection
ftp.close()
ssh_client.close()
