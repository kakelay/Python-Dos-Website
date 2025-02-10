# import requests

# # Replace this URL with the website you want to request
# url = 'https://portfolio-gd5c6tbhj-kruytharin.vercel.app/'

# # Number of requests
# num_requests = 1000

# for _ in range(num_requests):
#     try:
#         response = requests.get(url)
#         # You can add more code here to process the response, if needed
#         if response.status_code == 200:
#             print(f"Request successful: {response.status_code}")
#         else:
#             print(f"Request failed: {response.status_code}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# print("All requests completed.")



import requests

# Replace this URL with the website you want to request
url = 'https://portfolio-gd5c6tbhj-kruytharin.vercel.app/'

# Number of requests
num_requests = 1000

for i in range(num_requests):
    try:
        response = requests.get(url)
        # You can add more code here to process the response, if needed
        if response.status_code == 200:
            print(f"Request {i+1}: Successful ({response.status_code})")
        else:
            print(f"Request {i+1}: Failed ({response.status_code})")
    except Exception as e:
        print(f"Request {i+1}: An error occurred - {e}")

print("All requests completed.")  
