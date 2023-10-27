import requests
import json
response=requests.get("https://jsonplaceholder.typicode.com/users")
users=json.loads(response.text)

with open("users_api.csv","a") as file:
    file.write(f"name,email,phone,company name\n")
    for user in users:
        file.write(f"{user['name']},{user['email']},{user['phone']},{user['company']['name']}\n")