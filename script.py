import os, re 
import webbrowser, requests 


cmd = str(os.popen('cmd /c "arp -a"').read()) #finding and capturing all ip addresses in lan
addresses = re.findall("([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", cmd) #using regex to catch all ip addresses

for i in addresses:
    try: 
        web = requests.get("http://"+i) #getting http response from site
        if(web.status_code == 200):
            webbrowser.open_new("http://"+i) #opening existing site 
    except:
        pass
    







