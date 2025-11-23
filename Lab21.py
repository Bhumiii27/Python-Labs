import requests
# Making a GET Request
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
if response.status_code == 200:
    posts = response.json()
    print("Fetched Posts:")
    for post in posts[:5]:
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")

# Making a POST Request
new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}
response = requests.post(url, json=new_post)
if response.status_code == 201:
    created_post = response.json()
    print("\nCreated Post:")
    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
else:
    print(f"Failed to create post. Status code: {response.status_code}")

# Error Handling Example
url = 'https://jsonplaceholder.typicode.com/posts/1000'  # Non-existent post
response = requests.get(url)
if response.status_code == 200:
    post = response.json()
    print("Fetched Post:", post)
else:
    print(f"Error: {response.status_code} - {response.reason}")

#POST LAB:
import requests
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    # Method to GET posts
    def get_posts(self):
        url = f"{self.base_url}/posts"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()   # return all posts
        else:
            return f"Error: {response.status_code}"
    # Method to CREATE a new post (POST request)
    def create_post(self, title, body, user_id):
        url = f"{self.base_url}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return response.json()   # created post
        else:
            return f"Error: {response.status_code}"

# ----------- Usage Example -----------

client = APIClient("https://jsonplaceholder.typicode.com")
# Fetch first 3 posts
posts = client.get_posts()
print("Fetched Posts:")
for p in posts[:3]:
    print("Title:", p['title'])
# Create a new post
new_post = client.create_post("My API Post", "This is created using class method.", 1)
print("\nCreated Post:")
print(new_post)
