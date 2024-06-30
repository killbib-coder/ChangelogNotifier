# ChangelogNotifier

ChangelogNotifier is a versatile tool for automating changelog notifications via email. It simplifies the process of
keeping users informed about software and operating system updates. For the moment, there aren't many websites on which I perform scraping, but in the future, I plan to include all the
software or operating systems that interest me. Similarly, I currently send notifications via email, but ultimately, I
would like it to be a web platform.

### Scraped websites:

- [Nextcloud](https://nextcloud.com/fr/changelog/)
- [Kali](https://www.kali.org/releases/)

###  File hierarchies:

- main.py - Inside, the files are linked together
- NextcloudRelease.py - Inside, the scraping of Nextcloud's website is executed
- KaliRelease.py - Inside, the scraping of Kali's website is executed
- SendMail.py - Inside, the emails are sent
- DateCheck.txt - Inside, the update date is recorded to check if the update has already been sent or not
- IsItNew.py - Inside, the dates of each file are verified through the text file DateCheck.txt

