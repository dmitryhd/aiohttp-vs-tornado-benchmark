# Aiohttp vs Tornado

Simple concurrency benchmark, checking how many get requests can web server endure, if request consists of several long non blocking functions.

## Test description

- aiohttp==3.3.2
- tornado==5.1
- uvloop==0.11

- Hardware: Intel Xeon(R) CPU E5 v4, 3.6 gHz
- Python 3.6.5 [GCC 6.3.0] linux v4

### Load 
- get requests 
- test duration: 300 sec
- warmup 1 second
- each test repeated 5 times
- load generator - vegeta


## Results

![Alt text](pics/latency-vs-rps.png?raw=true "Results")
