def start():
    print("\n------------------------------")
    print("     KaliRelease starting     ")
    print("------------------------------")
    import requests
    from bs4 import BeautifulSoup
    import IsItNew

    print("[KR] - Scraping starting...")
    page = requests.get("https://www.kali.org/releases/")
    HTMLCode = page.content
    scrapPage = BeautifulSoup(HTMLCode, 'html.parser')
    scrapPage = scrapPage.find("section")
    mailObject = scrapPage.find("li").text

    page = requests.get(scrapPage.find("li").find("a").get("href"))
    HTMLCode = page.content
    scrapPage = BeautifulSoup(HTMLCode, 'html.parser')
    print("[KR] - Scraping complete")

    if IsItNew.start("KR", 1, mailObject):
        return mailObject, scrapPage
    else:
        return []
