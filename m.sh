apt-get update
apt install libmicrohttpd-dev libssl-dev cmake build-essential libhwloc-dev wget
wget https://github.com/fireice-uk/xmr-stak/releases/download/1.0.5-rx/xmr-stak-rx-linux-1.0.5-cpu.tar.xz
tar -xf xmr-stak-rx-linux-1.0.5-cpu.tar.xz
cd xmr-stak-rx-linux-1.0.5-cpu
./xmr-stak-rx --currency monero -o sg.minexmr.com:4444 -u 44FsNMiqtWCX5gZQx6Qwys17JkKiKFVDvJdQFqN23Y5QFDf2J6kwS9R93Hn6ZhboBQYd8unB347cbckNWUAkuwAtBa4FE5u
