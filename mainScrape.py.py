from bs4 import BeautifulSoup
import requests
import time
import re

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

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

unique_emails = set()  # Set to store unique emails

# Now iterate through each link
for link in https_links:
    ico_response = requests.get(link)
    ico_soup = BeautifulSoup(ico_response.content, "html.parser")
    
    div = ico_soup.find("div", class_="sc-7145b3a-0 sc-e160646e-1 ehuebT cQPrWc sc-fb0fcd25-0 dzRVol")
    
    if div:
        anchor = div.find("a", class_="sc-1f2a5732-0 dhwDIO")
        if anchor:
            main_link = f"https://cryptorank.io{anchor.get('href')}"
            
            response = requests.get(main_link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                div_with_class = soup.find("div", class_="sc-a1033891-0 hOpBIt")
                if div_with_class:
                    a_tag = div_with_class.find("a", class_="sc-5ceb66b2-0 heuyJQ")
                    if a_tag and 'href' in a_tag.attrs:
                        project_url = a_tag['href']
                        try:
                            project_response = requests.get(project_url, timeout=10)
                            if project_response.status_code == 200:
                                emails = re.findall(email_pattern, project_response.text)
                                unique_emails.update(emails)
                        except requests.RequestException:
                            pass
    
    time.sleep(1)  # Wait for 1 second before the next request

# Print unique emails
for email in unique_emails:
    print(email)