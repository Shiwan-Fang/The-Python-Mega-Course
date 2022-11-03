import time
from datetime import datetime as dt

hosts_temp=r"D:\thePythonMegaCourse\18_app11WebsiteBlocker\hosts"
# host_path=r"C:\Windows\System32\drivers\etc\hosts"
# with "r",tell python that you are actually passing a raw string in there
#or delete "r" and use "//"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) <dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23): #dt.now().year returns the year now as an integer   
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            print(content)
            for  website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
