import os
os.system("apt update")
os.system("apt upgrade -y")
os.system("pkg install git -y")
os.system("pkg install python -y")

os.system("rm -rf $HOME/Cracker-X")

os.system("git clone https://github.com/TeamSinchu/Cracker-X")

os.system("cd Cracker-X")
