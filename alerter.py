import http.server
from socket import socket, timeout
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import urllib3
import threading
import sys
from socket import timeout
from urllib.error import HTTPError, URLError


httprequest = urllib3.PoolManager()

alert_failure_count = 0
class NetworkStubHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        query_components = parse_qs(urlparse(self.path).query)
        if 'temperature_celcius' in query_components:
            temperature_celcius = query_components["temperature_celcius"][0]
            print(f'ALERT: Temperature is {temperature_celcius} celcius')        
        return

# Create an object of the above class
network_handler_object = NetworkStubHttpRequestHandler

LOCAL_SERVER_PORT = 7670
network_stub_server = socketserver.TCPServer(("", LOCAL_SERVER_PORT), network_handler_object)

# Star the server
def start_network_stub_server():
    network_stub_server.serve_forever()



def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    print("Entering Alerter")
    try:
        returnCode = httprequest.request("GET", "http://localhost:7670/?temperature_celcius="+str(celcius),timeout=1).status
    except :
        returnCode = 500
    else:
        print("Response received from server")
    print(returnCode)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1
    return(returnCode)

network_stub_thread=threading.Thread(target=start_network_stub_server)
network_stub_thread.daemon = True
network_stub_thread.start()

if(alert_in_celcius(400.5) != 200):
    assert(alert_failure_count==1)
if(alert_in_celcius(303.6) == 200):
    assert(alert_failure_count !=2)

print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
sys.exit()
