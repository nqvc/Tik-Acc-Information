import requests
from bs4 import BeautifulSoup
from datetime import datetime




print("""
     [ Made By Busalah. ]
     [ + ] Instagram : nqvc
     [ ! ] You are not entitled to sell the Tool [ ! ]
""")

class DaddyBusalah():
    def __init__(self):
        self.username = input("[?] Username: ")
        if self.username[0] == "@" or "@" in self.username:
            self.username.replace("@", "")
        self.server_log = None
        self.data_json = None
        self.admin()

    def admin(self):
        self.send_request()
        self._to_json()
        self.output()

    def send_request(self):
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
        r = requests.get(f"https://www.tiktok.com/@{self.username}", headers=headers)
        self.server_log = str(r.text)
        return r.text

    def _to_json(self):
        try:
            soup = BeautifulSoup(self.server_log, 'html.parser')
            script = soup.find(id='SIGI_STATE').contents
            data = str(script).split('},"UserModule":{"users":{')[1]
            self.data_json = data
            return 1
        except IndexError:
            input("[X] Error : Username Not Found .")
            exit()

    def get_user_id(self):
        try:
            data = self.data_json
            return data.split('"id":"')[1].split('",')[0]
        except IndexError:
            return "Unknown"

    def get_name(self):
        try:
            data = self.data_json
            return data.split(',"nickname":"')[1].split('",')[0]
        except IndexError:
            return "Unknown"

    def is_verified(self):
        try:
            data = self.data_json
            check = data.split('"verified":')[1].split(',')[0]
            if check == "false":
                return "No"
            else:
                return "Yes"
        except IndexError:
            return "Unknown"

    def secUid(self):
        try:
            data = self.data_json
            check = data.split(',"secUid":"')[1].split('"')[0]
            return check
        except IndexError:
            return "Unknown"

    def is_private(self):
        try:
            data = self.data_json
            check = data.split('"privateAccount":')[1].split(',')[0]
            if check == "true":
                return "Yes"
            else:
                return "No"
        except IndexError:
            return "Unknown"

    def followers(self):
        try:
            data = self.data_json
            check = data.split('"followerCount":')[1].split(',')[0]
            return check
        except IndexError:
            return "Unknown"

    def following(self):
        try:
            data = self.data_json
            check = data.split('"followingCount":')[1].split(',')[0]
            return check
        except IndexError:
            return "Unknown"

    def user_create_time(self):
        try:
            url_id = int(self.get_user_id())
            binary = "{0:b}".format(url_id)
            i = 0
            bits = ""
            while i < 31:
                bits += binary[i]
                i += 1
            timestamp = int(bits, 2)
            dt_object = datetime.fromtimestamp(timestamp)
            return dt_object
        except:
            return "Unknown"

    def last_change_name(self):
        try:
            data = self.data_json
            time = data.split('"nickNameModifyTime":')[1].split(',')[0]
            check = datetime.fromtimestamp(int(time))
            return check
        except IndexError:
            return "Unknown"

    def account_region(self):
        try:
            data = self.data_json
            check = data.split('"region":"')[1].split('"')[0]
            return check
        except IndexError:
            return "Unknown"

    def output(self):
        print(f"[ Get Info For @{self.username} ] ..")
        print(f"[ + ] UserID : {self.get_user_id()}")
        print(f"[ + ] Nickname : {self.get_name()}")
        print(f"[ + ] is verified : {self.is_verified()}")
        print(f"[ + ] is private : {self.is_private()}")
        print(f"[ + ] secUid : {self.secUid()}")
        print(f"[ + ] Followers : {self.followers()}")
        print(f"[ + ] Following : {self.following()}")
        print(f"[ + ] User Create Time : {self.user_create_time()}")
        print(f"[ + ] Last Time Change Nickname : {self.last_change_name()}")
        print(f"[ + ] Account Region : {self.account_region()}\n\n")
        input("[ + ] Done Sir ..")
        exit()

DaddyBusalah()