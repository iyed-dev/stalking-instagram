#importation des modules
import instaloader
#définition des variables
path = "stories"
instance = instaloader.Instaloader()
login = "" #identifiant
pwd = "" #mot de passe
account_to_scrap = "" #compte à stalker
#connexion au compte instagram
instance.login(user=login, passwd=pwd)
#compte à scrap
profile = instaloader.Profile.from_username(instance.context, username=account_to_scrap)
#installation des stories
instance.download_stories(userids=[profile.userid], filename_target=path)
# chercher le fichier jpg le plus récent
filesInmp3dir = os.listdir(path)
