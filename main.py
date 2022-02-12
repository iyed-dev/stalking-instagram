#importation des modules
import instaloader
from tkinter import *
import datetime
import glob
import os
#définition des variables
path = "stories"
instance = instaloader.Instaloader()
login = "iyedamri21"
pwd = "aqzsedr4"
account_to_scrap = "nln_1383"
#connexion au compte instagram
instance.login(user=login, passwd=pwd)
#compte à scrap
profile = instaloader.Profile.from_username(instance.context, username=account_to_scrap)
#installation des stories
instance.download_stories(userids=[profile.userid], filename_target=path)
# chercher le fichier jpg le plus récent
filesInmp3dir = os.listdir(path)