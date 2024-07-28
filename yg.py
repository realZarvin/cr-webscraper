from bs4 import BeautifulSoup
import requests
import re
from email.message import EmailMessage
import my_module
import ssl
import smtplib

# defining the url
url = "https://cryptorank.io/ico?page=40"

# sending a get request to the url and getting the html info
response = requests.get(url)
html_content = response.content

# creating a beautiful soup object to parse the html
soup = BeautifulSoup(html_content, "html.parser")

# finding the elements with the specific class
elements = soup.find_all("a", class_="sc-77da7dd7-1 dTUxdJ")

# for collecting the links from the elements
https_links = []
for element in elements:
    link = element.get("href")
    # petch here !!!!
    if link.startswith("/ico/"):
        https_links.append("https://cryptorank.io" + link)

        # print the https links
        for links in https_links:
            print(links)

# FOR GETTING THE PROJECT WEBSITE LINK FROM THE ICO PAGE
for link in https_links:
    # Send a request to the webpage
    response = requests.get(link)
    html_code = response.content

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_code, 'html.parser')

    # Find the first <a> tag with the modified class name
    link = soup.select_one('a.sc-6d85e775-0.gOcXaF')

    # Check if the link exists before accessing its attributes
    if link is not None:
        href = link.get('href')
        list_of_emails = []
        url_2 = href
        email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        response = requests.get(href)
        matches = re.findall(email, response.text)
        for match in matches:
            list_of_emails.append(match)
            # for presenting them neatly
        for items in list_of_emails:
            print(items)
            email_sender = "bigtimeyagaz@gmail.com"
            email_password = my_module.email
            email_receiver = items

            subject = "Invitation to List Your Project on Our Leading CEX"

body_template = """
Hello

I hope this message finds you well.

My name is Yagaz, and I am the Listing Manager at Bitmart. I am writing to extend an invitation for you to list your project on our Centralized Exchange (CEX).

At Bitmart, we are committed to providing a premier trading platform that offers extensive benefits to our listed projects, including:
- Increased Visibility: Gain exposure to a global audience of enthusiastic traders and investors.
- Robust Security: Our state-of-the-art security measures ensure the safety and integrity of your assets.
- Liquidity Support: Access deep liquidity pools to facilitate seamless trading experiences for your users.
- Dedicated Support: Benefit from our dedicated support team, ready to assist you at every step.

We are confident that your project will thrive on our platform, reaching new heights and attracting a broader community of supporters.

If you are interested in exploring this opportunity, please reply to this email. I would be delighted to provide you with further details and assist you with the listing process.

Thank you for considering our invitation. We look forward to the possibility of collaborating with you.

Best regards,

Yagazz
Community Manager
BitMart
zarvinns@gmail.com
"""
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            break
