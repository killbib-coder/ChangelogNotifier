# ChangelogNotifier
ChangelogNotifier is a versatile tool for automating changelog notifications via email. It simplifies the process of keeping users informed about software and operating system updates.


## More informations
Scraped websites:
- [Nextcloud](https://nextcloud.com/fr/changelog/)


File hierarchies
- main.py - where the files are linked together
- NextcloudRelease.py - where the scraping of Nextcloud's website is executed
- SendMail.py - where the emails are sent
- VerifDate.txt - where the update date is recorded to check if the update has already been sent or not

## Details
For the moment, there aren't many websites on which I perform scraping, but in the future, I plan to include all the software or operating systems that interest me. Similarly, I currently send notifications via email, but ultimately, I would like it to be a web platform.
