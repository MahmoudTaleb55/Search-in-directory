import requests
from bs4 import BeautifulSoup

base_url = "HTTP://example.com"
directories = []

def find_flag(directories, base_url):
   for directory in directories:

     url = f"{base_url}hidden/{directory}/flag.txt"
     response = requests.get(url)
 
     if requests.status_codes == 200:

        print(f"The Flag is: {directory}")

     else:
        print("The flag was not found!")    

find_flag(directories, base_url)        
