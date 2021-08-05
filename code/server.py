import os 
import socket

#def getIP():
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#	s.connect(('8.8.8.8',1))
#	return s.getsockname()[0]

#server_ip = getIP()
print()
#print(f'Server IP: {server_ip}')
print()
opensshDir = os.path.expanduser('~/openssh/')


myCmd = f'{opensshDir}./sshd -D -f {opensshDir}/regress/sshd_config -o KexAlgorithms=kyber-512-sha256 -o HostKeyAlgorithms=ssh-dilithium3 -o PubkeyAcceptedKeyTypes=ssh-dilithium3 -h {opensshDir}/regress/host.ssh-dilithium2'

os.system(myCmd)