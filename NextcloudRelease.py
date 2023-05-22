def start():
    print("-----------------------------")
    print("  NextcloudRelease starting  ")
    print("-----------------------------")
    import requests
    from bs4 import BeautifulSoup
    from lxml import etree
    print("[NR] - Démarage du scraping...")
    url = "https://nextcloud.com/fr/changelog/"
    page = requests.get(url)
    codehtml = page.content
    pageScrapable = BeautifulSoup(codehtml,'html.parser')
    pageScrapableAvecXPATH = etree.HTML(str(pageScrapable)) #Utilisation de lxml
    dateRelease = pageScrapableAvecXPATH.xpath('//*[@id="version-fixed-26-0-1"]/div/p/text()')[0]
    dateRelease = " ".join(dateRelease.split())
    print("[NR] - Fin du scraping")

    def createMailContent():
        print("[NR] - Création du contenue du mail..")
        nouvelleVersion = pageScrapableAvecXPATH.xpath('//*[@id="26-0-1"]/text()')[1]
        nouvelleVersion = " ".join(nouvelleVersion.split())
        oneChange = pageScrapableAvecXPATH.xpath('//*[@id="latest26"]/div[2]/div/div/div/div/div[2]/div/div[2]/div/ul/li[1]/a/text()')
        changes = list()
        boucle = 0
        nbLi=2
        while boucle<1 and len(oneChange)!=0 :
            try :
                oneChange = pageScrapableAvecXPATH.xpath('//*[@id="latest26"]/div[2]/div/div/div/div/div[2]/div/div[2]/div/ul/li['+str(nbLi)+']/a/text()')
                changes.append("\n"+"- "+oneChange[0])
                nbLi+=1
            except :
                boucle==1
        mailSubject = "Nextcloud "+nouvelleVersion.lower()+" is out"
        mailContent = "Nextcloud "+nouvelleVersion.lower()+" - "+dateRelease+" \nChanges : "+' '.join(changes)+"\n"+url
        print("[NR] - Fin de création du contenue du mail")
        return mailSubject, mailContent

    print("[NR] - Vérification de la date...")
    content = open("VerifDate.txt").read()
    if content != dateRelease:
        Output = createMailContent()
        open("VerifDate.txt", "w").write(dateRelease)
        print("[NR] - (msg) Modification du fichier de vérification...")
    else :
        Output = []
        print("[NR] - (msg) Pas de nouvelle version")
    print("[NR] - Fin de la vérification")

    print("")
    return Output