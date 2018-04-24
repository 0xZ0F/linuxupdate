#!/bin/bash
set -e
printf "\033[35mUpdate Script made by Z0F!\033[0m\n"
printf "\033[93mWarning: This script is not always fully automated!\nThis script uses apt like \"apt install\". If you would like to use apt like \"apt-get install\" please use the old version of this script.\033[0m\n"
printf "\033[34mWhat arguments would you like to use? (apt command):\033[0m "
read usrCmd
printf "\033[93m>>>NOTE: If you enter an invalid argument, you will receive the following error: \"The update command takes no arguments\".\033[0m\n"
for x in {1..2}
do
printf "\033[91mUpdating...\033[0m\n"
command sudo apt update $usrCmd
printf "\033[91mUpgrading...\033[0m\n"
command sudo apt full-upgrade $usrCmd
done

printf "\033[34mDo you want to update your distribution?:\033[0m "
read distAns
if [ $distAns == "y" ] || [ $distAns == "Y" ]
then
printf "\033[91mUpgrading Distro...\033[0m\n"
command sudo apt dist-upgrade
printf "\033[91mUpdating finished! Have a fabulous day!\033[0m\n"
else
printf "\033[91mUpdate finished! Have a fabulous day!\033[0m\n"
fi
