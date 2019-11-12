import time 
from datetime import datetime as dt 
  
#change hosts path according to your OS 
hostsPath = r"/etc/hosts"
# localhost's IP 
redirect = "127.0.0.1"
  
# insert your website here! 
websiteList = ["www.facebook.com","facebook.com","www.youtube.com","youtube.com"] 
  
while True:  
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23): 
        print("Working hours...") 
        with open(hostsPath, 'r+') as file: 
            content = file.read() 
            for website in websiteList: 
                if website in content: 
                    pass
                else:  
                    file.write(redirect + " " + website + "\n") 
    else: 
        with open(hostsPath, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in websiteList): 
                    file.write(line) 
                    
            file.truncate() 
  
        print("Not working hours...") 
    time.sleep(5)
