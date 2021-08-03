import os 
import socket 

opensshDir = os.path.expanduser('~/opehssh')


myCmd = f'{opensshDir}>./ssh -F {opensshDir}/regress/ssh_config \
                  -o KexAlgorithms=kyber-512-sha256 \
                  -o HostKeyAlgorithms=ssh-dilithium2>\
                  -o PubkeyAcceptedKeyTypes=ssh-dilithium2 \
                  -o PasswordAuthentication=no \
                  -i regress/ssh-dilithium2 \
                  somehost true'

os.system(myCmd)