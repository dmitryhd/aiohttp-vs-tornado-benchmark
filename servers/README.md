# vegeta

## install
`$ go get -u github.com/tsenart/vegeta`

## simple usage
`echo 'GET http://localhost:8890/_info' | vegeta -cpus 1 attack -rate 100 -duration 10s -timeout 1s | vegeta report -reporter json | jq`

`echo 'GET http://localhost:8890/_info' | vegeta -cpus 1 attack -rate 100 -duration 4s -timeout 1s | vegeta report -reporter plot > plot.html`

`echo 'GET http://localhost:8890/sleep50' | vegeta -cpus 1 attack -rate 100 -duration 4s -timeout 1s | vegeta report -reporter plot > /tmp/plot.html; open /tmp/plot.html

pyflame -p $(pgrep -f server.py) -s 120 -r 0.001 > /tmp/aiohttp_trace.tr
cat /tmp/aiohttp_trace.tr | ./flamegraph.pl > /tmp/aiohttp_trace.svg
sed -i -e 's/\/.*site-packages//g' aiohttp_trace.svg
sed -i -e 's/\/.*python3\.6//g' aiohttp_trace.svg