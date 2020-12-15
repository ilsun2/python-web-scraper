# from bs4 import BeautifulSoup
import requests

url = "https://www.indeed.com/jobs?q=python"
r = requests.get(url)
print(r)