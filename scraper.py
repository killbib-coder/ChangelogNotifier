import requests
from bs4 import BeautifulSoup

def scrap(tool) :
    response = requests.get(tool.url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        html_version = soup.select_one(tool.version_path)
        html_link = soup.select_one(tool.link_path)

        if html_version and html_link:
            version = html_version.text.strip()
            link = html_link.get('href').strip()
            if link[0]+link[1]+link[2]+link[3] != "http":
                link = tool.url

            if version != tool.version :
                tool.version = version
                return tool
            else :
                return None
            print("[+] Scraper - Scraping complete")

        else:
            print(f"[-] Scraper - The 'strong' or 'a' elements were not found in {tool.name} page")
    else:
        print(f"[-] Scraper - Error downloading the page of {tool.name}. Status code : {response.status_code}")
