# Python simple http(s) server

### simple http server 

```
python3 -m http.server
```

### https server

[Finding local IP addresses using Python's stdlib](https://stackoverflow.com/a/28950776/3608824)


[simple-https-server.py](https://gist.github.com/DannyHinshaw/a3ac5991d66a2fe6d97a569c6cdac534)
 
```
import http.server
import ssl
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print('https://' + get_ip() + ':4443')
server_address = ('', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(certfile="server.pem", keyfile="key.pem")
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
```


### wrap in tk

```
#!/usr/bin/env python3

import http.server
import ssl
import socket
import tkinter as tk
import sys
import threading


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def start_https_server(path, port):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(certfile="server.pem", keyfile="key.pem")
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()



def main():

    path = ""
    port = 4443
    
    ipaddress = get_ip_address()
    url = "https://{}:{}/".format(ipaddress, port)
    print("Serving at {}".format(url))
    
    # Start the web server
    web_server = threading.Thread(name='web_server',
                                   target=start_https_server,
                                   args=(path, port))
    web_server.setDaemon(True)
    web_server.start()
    
        
    # App GUI window gets the main loop
    root = tk.Tk()
    root.title("App Server")
    tk.Label(root, text="Serving at {}".format(url)).pack()
    tk.Button(root, text="Quit", command=root.destroy).pack()
    tk.mainloop()
    
if __name__ == '__main__':
    main()
```





