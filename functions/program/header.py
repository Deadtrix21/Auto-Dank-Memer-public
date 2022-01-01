import os, json


class Header:
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "config/")
    
    def __get_config(self):
         with open(self.path+"bot.json","r") as file:
            return json.load(file)
        
    def __format_header(self, items={}):
        items = self.__get_config()
        HEADER = \
        {
            "content-type": "application/json",
            "user-agent": items["browser"],
            "authorization": items["token"],
            "host": "discordapp.com",
            "referrer": items["channel_url"]
        }
        return HEADER

    def get_msg_ctx(self, msg):
        return {"content": msg,"tts": False}
    
    def get_header(self):
        return self.__format_header()