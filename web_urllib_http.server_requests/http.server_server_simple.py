from http.server import SimpleHTTPRequestHandler, HTTPServer

hostName = "127.0.0.1"
serverPort = 8000
webServer = HTTPServer((hostName, serverPort), SimpleHTTPRequestHandler)
webServer.serve_forever()
