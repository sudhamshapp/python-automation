'''
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='50.112.170.86', username='ec2-user', password='paramiko', port='22')
stdin, stdout, stderr = ssh.exec_command('ls -ltra')
print("the output is")
print(stdout.readlines())
print("the error is")
print(stderr.readlines())
'''

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establish an SSH connection
# ssh.connect(hostname='50.112.170.86', username='ec2-user', password='paramiko', port='22')
ssh.connect(hostname='50.112.170.86', username='ec2-user', key_filename='/Users/mars/.ssh/id_rsa', port='22') #with ec2-user we exchanged our key, first do ssh-keygen then copy the public key id_rsa.pub to instance using ssh-copy-id ec2-user@50.112.170.86, then get the path of private key using /Users/mars/.ssh/id_rsa

# Execute the 'ls -ltra' command on the remote server
stdin, stdout, stderr = ssh.exec_command('ls -ltra')

# Print the output
print("the output is")
print(stdout.read().decode())  # Use 'read()' to read the entire output as a string

# Print the error, if any
print("the error is")
print(stderr.read().decode())  # Use 'read()' to read the entire error as a string

# Close the SSH connection
ssh.close()
