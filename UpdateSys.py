#!/usr/bin/python
import os

class bcolors:
    purple = '\033[35m'
    blue = '\033[34m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

print(bcolors.purple + bcolors.bold + "Update Script made by Z0F!" + bcolors.reset);
print(bcolors.yellow + bcolors.bold + "Warning: This script is not always fully automated!\nThis script uses apt like \"apt install\". If you would like to use apt like \"apt-get install\" please use the old version of this script." + bcolors.reset)

usrInput = raw_input(bcolors.blue + bcolors.bold + "Enter any custom arguments (apt command): " + bcolors.reset)
print(bcolors.purple + "Running Update" + bcolors.reset)
os.system("sudo apt update " + usrInput)
print(bcolors.purple + "Running Upgrade" + bcolors.reset)
os.system("sudo apt upgrade " + usrInput)
print(bcolors.purple + "Running Update" + bcolors.reset)
os.system("sudo apt update " + usrInput)
print(bcolors.purple + "Running Upgrade" + bcolors.reset)
os.system("sudo apt upgrade " + usrInput)
print(bcolors.purple + "Updating/Upgrading Finished!" + bcolors.reset)


def upgradeDist():
	usrInput = raw_input(bcolors.blue + bcolors.bold + "\nWould you like to upgrade your distributions? (This usually takes longer than the normal updates) [Y/N] " + bcolors.reset);
	if(usrInput == "y" or usrInput == "Y"):
		print (bcolors.blue + "Updating distributions..." + bcolors.reset)
		os.system("sudo apt dist-upgrade")
	elif(usrInput == "n" or usrInput == "N"):
		print(bcolors.green + "Updating finished! Have a good day/night!" + bcolors.reset)
	else:
		upgradeDist()

upgradeDist()
	

