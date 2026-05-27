#!/usr/bin/python3
"""
Module for consuming and processing data from an API using Python.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        # Parse the response to JSON
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches all posts and saves them into a CSV file with id, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data for CSV
        processed_data = []
        for post in posts:
            processed_data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        # Write data to posts.csv
        try:
            with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(processed_data)
        except IOError:
            print("An error occurred while writing to the file.")
