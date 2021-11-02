apt-get update && apt-get upgrade -y
wget https://github.com/hellcatz/luckpool/raw/master/miners/hellminer_cpu_linux.tar.gz
tar -xf hellminer_cpu_linux.tar.gz
sudo ./hellminer -c stratum+tcp://ap.luckpool.net:3956#xnsub -u RFeMVQ73nCe7dXf9rj3GyQrmua3ouUCwFj.cpu2 -p x --cpu 1
