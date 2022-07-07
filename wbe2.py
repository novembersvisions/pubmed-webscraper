import requests
from bs4 import BeautifulSoup
import time

url = "https://pubmed.ncbi.nlm.nih.gov/?term=whole+brain+emulation"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#title = soup.get_text()
content = soup.find_all("div", {"class": "docsum-content"})

for result in content:
    print(result.text)

# send email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from emaildetails import email
from emaildetails import password

send_to_email = 'hprice@carboncopies.org'
subj = 'PubMed Search Titles'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subj

for result in content:
    msg.attach(MIMEText(result.text))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

mailtxt = msg.as_string()
server.sendmail(email, send_to_email, mailtxt)
server.quit()

