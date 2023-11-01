paramiko module used to work with remote servers
sshv2 protocol

working with remote linux server from linux/windows using paramiko of python

Local Server                      Remote Server
windows                             windows
windows                             linux
linux                               windows
linux                                linux

username and password
ssh.connect(hostname='50.112.170.86', username='ec2-user', password='paramiko', port='22')
sudo passwd ec2-user -set the password
sudo vim /etc/ssh/sshd_config
PasswordAuthentication no change this to yes
sudo systemctl restart sshd

using the ssh key
ssh.connect(hostname='50.112.170.86', username='ec2-user', key_filename='/Users/mars/.ssh/id_rsa', port='22')
with ec2-user we exchanged our key, first do ssh-keygen then copy the public key id_rsa.pub to instance using ssh-copy-id ec2-user@50.112.170.86, then get the path of private key using /Users/mars/.ssh/id_rsa





