import requests

response = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(response.status_code)
print(response.content)