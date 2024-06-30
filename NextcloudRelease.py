def start():
    print("\n-----------------------------")
    print("  NextcloudRelease starting  ")
    print("-----------------------------")
    import requests
    from bs4 import BeautifulSoup
    from lxml import etree
    import IsItNew
    print("[NR] - Scraping starting...")
    url = "https://nextcloud.com/fr/changelog/"
    page = requests.get(url)
    HTMLCode = page.content
    scrapPage = BeautifulSoup(HTMLCode, 'html.parser')
    scrapPageXPATH = etree.HTML(str(scrapPage))  # Utilisation de lxml
    dateRelease = scrapPageXPATH.xpath('//*[@id="version-fixed-26-0-1"]/div/p/text()')[0]
    dateRelease = " ".join(dateRelease.split())
    print("[NR] - Scraping complete")

    def createMailContent():
        print("[NR] - Mail content creation...")
        newVersion = scrapPageXPATH.xpath('//*[@id="26-0-1"]/text()')[1]
        newVersion = " ".join(newVersion.split())
        oneChange = scrapPageXPATH.xpath(
            '//*[@id="latest26"]/div[2]/div/div/div/div/div[2]/div/div[2]/div/ul/li[1]/a/text()')
        changes = list()
        nbLi = 2
        while len(oneChange) != 0:
            try:
                oneChange = scrapPageXPATH.xpath(
                    '//*[@id="latest26"]/div[2]/div/div/div/div/div[2]/div/div[2]/div/ul/li[' + str(
                        nbLi) + ']/a/text()')
                changes.append("\n" + "- " + oneChange[0])
                nbLi += 1
            except:
                break
        mailSubject = "Nextcloud " + newVersion.lower() + " is out"
        mailContent = "Nextcloud " + newVersion.lower() + " - " + dateRelease + " \nChanges : " + ' '.join(
            changes) + "\n" + url
        print("[NR] - Mail content creation complete")
        return mailSubject, mailContent

    if IsItNew.start("NR", 0, dateRelease):
        return createMailContent()
    else:
        return []

