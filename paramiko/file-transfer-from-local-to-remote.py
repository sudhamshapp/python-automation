'''
# downloads a file
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='50.112.170.86', username='ec2-user', key_filename='/Users/mars/.ssh/id_rsa', port='22')  

#opening sftp connection with the remote server
sftp_client = ssh.open_sftp()
# print(dir(sftp_client))
# this retrieve the file from the remote server to the local machine
# sftp_client.get('/home/ec2-user/mars.txt', 'mars.txt')
sftp_client.chdir('/home/ec2-user')
print(sftp_client.getcwd()) 
# it takes two arguments, first is the file name on the remote server, second is the file name on the local machine
sftp_client.get('demo.txt', 'demo.txt') 

sftp_client.close()
ssh.close()
'''

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='50.112.170.86', username='ec2-user', key_filename='/Users/mars/.ssh/id_rsa', port='22')  
#opening sftp connection with the remote server
sftp_client = ssh.open_sftp()
sftp_client.put('dummy.txt', '/home/ec2-user/dummy.txt')
sftp_client.close()
ssh.close()
