import requests
import csv

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder, prints the status code, 
    and prints the title of each post if successful."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder, structures them into a list 
    of dictionaries with specific keys, and saves them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        structured_posts = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]
        
        fieldnames = ['id', 'title', 'body']
        
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)
