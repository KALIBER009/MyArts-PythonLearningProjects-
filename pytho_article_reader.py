import requests  # Used to send HTTP requests to websites
from bs4 import BeautifulSoup  # Used for parsing HTML and extracting data
import os  # Used for interacting with the operating system (e.g., directories)
import html5lib  # HTML parser that works well with poorly-formed HTML

try:
    # Ask the user to enter the URL of the article
    URL = input('please enter the url :')

    # Send a GET request to the URL
    request = requests.get(URL)

    # Check if the request was successful (HTTP status code 200)
    if request.status_code == 200:
        # Parse the HTML content of the page using html5lib parser
        show_data = BeautifulSoup(request.content, "html5lib")

        # Try to find the <article> tag, which usually contains the main content
        article = show_data.find("article")

        if article:
            # Extract all text within the <article> tag, stripping whitespace
            new_twxt = article.get_text(strip=True)

            # Split the article text into individual lines
            lines = article.get_text(strip=True).splitlines()

            # Print the first 5 non-empty lines
            for line in lines[:5]:
                if line.strip():
                    print(line)
        else:
            # If no <article> tag was found, show this message
            print("لم أجد محتوى المقال داخل <article>")  # "Article tag not found"
    else:
        # Raise an error if the HTTP request failed (not status code 200)
        raise ValueError("please try a diffrent URL ..")

except Exception as e:
    # Catch and display any unexpected errors
    print('Error:', e)
