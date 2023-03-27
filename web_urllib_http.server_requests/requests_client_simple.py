import requests
import time


start_time = time.time()
res = requests.get('http://127.0.0.1:8000', stream=True, allow_redirects=False)
res.timing = "--- %07.3f ms ---" % ((time.time() - start_time) * 1000)

print(res.status_code)
print(res.text)
print(res.timing)
