from csv import writer

import requests
from bs4 import BeautifulSoup

url = "https://www.rithmschool.com/blog"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title", "Link", "Date"])
    
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        
        csv_writer.writerow([title, url, date])
