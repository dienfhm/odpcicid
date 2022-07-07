import requests

print ("hello world")
print ("odp BNI")

response = requests.get("https://www.google.com")

print (response.text)