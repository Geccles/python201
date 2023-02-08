import requests
import time

req =  requests.get("https://www.google.com")
print(req.status_code) # we should get a 200 here

# you could make a monitoring program with the following
while True:
    print(req.status_code)
    if req.status_code != 200:
        print("Something is wrong, please contact someone for assistance.")
        pass
    time.sleep(3) # wait every 3 seconds to run
