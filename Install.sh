#Assuming Ubuntu 18.04
#building openssh

sudo apt-get remove openssh-server
sudo apt-get purge openssh-client

sudo apt install autoconf automake cmake gcc libtool libssl-dev make ninja-build zlib1g-dev git

git clone https://github.com/prchander/openssh.git
cd openssh

sudo mkdir -p -m 0755 /var/empty
sudo groupadd sshd
sudo useradd -g sshd -c 'sshd privsep' -d /var/empty -s /bin/false sshd
./oqs-scripts/clone_liboqs.sh
./oqs-scripts/build_liboqs.sh
./oqs-scripts/build_openssh.sh