from bs4 import BeautifulSoup
import requests
import time

# defining the url
url = "https://cryptorank.io/ico"

# sending a get request to the url and getting the html info
response = requests.get(url)
html_content = response.content

# creating a beautiful soup object to parse the html
soup = BeautifulSoup(html_content, "html.parser")

# finding the elements with the specific class
elements = soup.find_all("a", class_="sc-39ba2409-1 bgOSTi")

# for collecting the links from the elements
https_links = []
for element in elements:
    link = element.get("href")
    if link and link.startswith("/ico/"):
        https_links.append("https://cryptorank.io" + link)

# Now iterate through each link
for link in https_links:
    
    # Get the content of the ICO page
    ico_response = requests.get(link)
    ico_soup = BeautifulSoup(ico_response.content, "html.parser")
    
    # Find the div with the specified class
    div = ico_soup.find("div", class_="sc-7145b3a-0 sc-e160646e-1 ehuebT cQPrWc sc-fb0fcd25-0 dzRVol")
    
    # creating a list where everything will be stored 
    main_link = []
    
    # for getting the personal project links
    if div:
        # Inside the div, find the anchor tag with the specified class
        anchor = div.find("a", class_="sc-1f2a5732-0 dhwDIO")
        if anchor:
            main_link.append(f"https://cryptorank.io/{anchor.get('href')}")
    time.sleep(1)  # Wait for 1 second before the next request

    # Iterate over the main_link list
    for main in main_link:
        response = requests.get(main)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            div_with_class = soup.find("div", class_="sc-a1033891-0 hOpBIt")
            if div_with_class:
                a_tag = div_with_class.find("a", class_="sc-5ceb66b2-0 heuyJQ")
                if a_tag and 'href' in a_tag.attrs:
                    print(a_tag['href'])
        time.sleep(1)  # Wait for 1 second before the next request