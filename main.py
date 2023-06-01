import sys
import NextcloudRelease as NR
import KaliRelease as KR
import SendMail as SM
print("ChangelogNotifier starting")

password = sys.argv[1]
smtpServer = sys.argv[2]

### Nextcloud release
NextcloudReleaseOutput = NR.start()
if len(NextcloudReleaseOutput) != 0:
    SM.start(NextcloudReleaseOutput[0], NextcloudReleaseOutput[1], password, smtpServer)

### Kali release
KaliReleaseOutput = KR.start()
if len(KaliReleaseOutput) != 0:
    SM.start(KaliReleaseOutput[0], KaliReleaseOutput[1], password, smtpServer)
