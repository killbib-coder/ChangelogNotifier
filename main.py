print("Importation des modules...")
import sys
import NextcloudRelease as NR
import SendMail as SM
print("Fin de l'importation\n")

password = sys.argv[1]
smtpServeur = sys.argv[2]

### Nexcloud release mail 
NextcloudReleaseOutput = NR.start()
if len(NextcloudReleaseOutput)!=0:
	SM.start(NextcloudReleaseOutput[0], NextcloudReleaseOutput[1], password, smtpServeur)