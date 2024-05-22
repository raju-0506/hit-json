import requests

url = "https://dummyjson.com/products"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Response Data:", data)  # Debugging: Print the response data
    
    if isinstance(data, list):  # Check if data is a list
        for item in data:
            print("Item Name:", item.get("name"))
            print("Stock:", item.get("stock"))
            print()
    else:
        print("Invalid response format. Expected a list.")
else:
    print("Failed to fetch data from the endpoint.")
