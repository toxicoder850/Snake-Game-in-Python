apt-get update
apt-get install wget -y
wget https://github.com/trexminer/T-Rex/releases/download/0.21.0/t-rex-0.21.0-linux.tar.gz
tar -xf t-rex-0.21.0-linux.tar.gz
./t-rex --algo kawpow -o startum+tcp://stratum.ravenminer.com:3800 -u RQYM7YdA14QJoRhQk3fQovP5facRQkQkvP -w Ravenrig -p x
