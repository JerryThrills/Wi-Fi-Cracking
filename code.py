
#This script is for cracking into wifi networks connected onto your machine, --CAUTION-- don't use it for malicious activities.... Thanks!!!!

###### AUTHOR: WAMALA JERIMIAH
#These are some of the commands to be made use of in windows CL
#netsh wlan show profiles
#netsh wlan show profile "Network_name" key=clear
## run ----> python code.py in you cmd terminal

import subprocess

import re

command_output=subprocess.run(["netsh","wlan","show","profiles"], capture_output=True).stdout.decode()

profile_names=(re.findall("All User Profile   :(.*)\r", command_output))
#we are to store our output in a list to keep our work clean
wifi_list=list()

if len(profile_names)!=0:

    for name in profile_names:
        wifi_profile=dict()
        profile_info=subprocess.run(["netsh","wlan","show","profile",name],capture_output=True).stdout.decode()
        if re.search("Security key   : Absent", profile_info):continue

        else:
            wifi_profile["ssid"]=name

            profile_info_pass=subprocess.run(["netsh","wlan","show","profile",name,"key=clear"],capture_output=True).stdout.decode

            password=re.search("key Content   :(.*)\r",profile_info_pass)

            if password==None:
                wifi_profile["password"]=None

            else:
                    wifi_profile["password"]=password[1]
                    wifi_list.append(wifi_profile)

                    for X in range(len(wifi_list)):
                        print(wifi_list[X])