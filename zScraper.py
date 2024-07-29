#Importing all Libraries;
import requests
from bs4 import BeautifulSoup
import time


# Fetch the HTML content of the main page
url = 'https://cryptorank.io'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# Find all anchor tags with the specified class, which I no understand.
elements = soup.find_all("a", class_="sc-39ba2409-1 bgOSTi")


# Collecting the links from the elements
https_links = []
for element in elements:
    link = element.get("href")
    if link and link.startswith("/ico/"):
        https_links.append("https://cryptorank.io" + link)


# List to store all project links
main_links = []


# Iterate through each ICO link
for link in https_links:
    # Get the content of the ICO page
    ico_response = requests.get(link)
    ico_soup = BeautifulSoup(ico_response.content, "html.parser")
    
    
    # Find the div with the specified class
    div = ico_soup.find("div", class_="sc-7145b3a-0 sc-e160646e-1 ehuebT cQPrWc sc-fb0fcd25-0 dzRVol")
    
    
    # Get the personal project links
    if div:
        # Inside the div, find the anchor tag with the specified class
        anchor = div.find("a", class_="sc-1f2a5732-0 dhwDIO")
        if anchor:
            # Append the full URL to the main_links list
            main_links.append(f"https://cryptorank.io{anchor.get('href')}")
            
    
    # Wait for 1 second before the next request
    time.sleep(0.87)


# Print all collected project links
for main_link in main_links:
    print(main_link)
