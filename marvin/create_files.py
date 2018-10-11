import marvin.webscrape
from platform import system, release
import json
import os

contacts_path = os.path.join('marvin','json','contacts.json')
corrections_path = os.path.join('marvin','json','corrections.json')

check_os = system()
os_release = release()
marvin_version = webscrape.getVersion()

try:
    with open('Os.json', 'w') as outfile:
        var = {"Marvin_Release":marvin_version,"Os_data":{"OS":check_os,"os_release":os_release},"apps":{"IOS":"INACTIVE"},"voice":"female"}
        json.dump(var, outfile)
    with open(contacts_path, 'w') as outfile1:
        var1 = {"contacts":{},"nicks":{}}
        json.dump(var1, outfile1)
    with open(corrections_path, 'w') as outfile2:
        var2 = {"corrections":{"who r u":{"correct":"who are you"},"who are u":{"correct":"who are you"}}}
        json.dump(var2, outfile2)
except Exception as e:
    print('We ran into a problem\nPlease report this issue ' + str(e) + '\nFiles couldn\'t be created properly')