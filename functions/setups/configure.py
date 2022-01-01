import json, os, sys


class Main:
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "config/")
        self.setup_main()
        self.channel = None
        
    def get_input(self, ask):
        print(f"{ask}: ")
        return input("")
    
    def __get_bot(self, item={}):
        with open(self.path+"bot.json","r") as file:
            return json.load(file)
        
    def __get_config(self, item={}):
        with open(self.path+"config.json","r") as file:
            return json.load(file)
    
    def __setup_bot(self, item={}):
        item = self.__get_bot()
        item["token"]           = self.get_input("User Token (dev browser Technique)")
        self.channel            = self.get_input("Channel ID (use developer Options)")
        item["channel_id"]      = self.channel
        item["channel_url"]     = self.get_input("Channel Url (use browser to get channel url)")
        item["browser"]         = self.get_input("Browser Agent (https://www.google.com/search?q=what+is+my+user+agent)")
        return item
    
    def get_list(self, items = []):
        print("Enter START to stop")
        bool = True
        while bool:
            cmd = self.get_input("Command String")
            if cmd.upper() == "START":
                bool = False
            else:
                items.append(cmd)
        return items
    
    def __setup_config(self, item={}):
        item = self.__get_config()
        item["channel_id"]      = self.channel
        item["intervals"]       = self.get_input("Time Delay between commands")
        item["commands"]        = self.get_list()
        return item
    
    def __save_bot(self, item={}):
        item = self.__setup_bot()
        with open(self.path+"bot.json","w") as file:
            json.dump(item, file, indent=7)
            
            
    def __save_config(self, item={}):
        item = self.__setup_config()
        with open(self.path+"config.json","w") as file:
            json.dump(item, file, indent=7)
    
    
    def setup_main(self):
        print(self.path)
        self.__save_bot()
        self.__save_config()
        
        