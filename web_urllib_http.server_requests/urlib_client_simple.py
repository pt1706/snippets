import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    status = response.status

print(status, html, sep='\n')
