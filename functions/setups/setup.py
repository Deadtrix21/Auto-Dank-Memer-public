import json, os, sys


class Main:
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "config/")
        self.setup_main()
    
    def __create_bot(self, item = {}):
        item["token"]           = None
        item["channel_id"]      = None
        item["channel_url"]     = None
        item["browser"]         = None
        return item
        
    def __create_config(self, item = {}):
        item["intervals"]       = None
        item["commands"]        = []
        return item
    
    def __save_bot(self, item=None):
        item = self.__create_bot()
        with open(self.path+"bot.json","w") as file:
            json.dump(item, file, indent=7)
        
    def __save_config(self, item=None):
        item = self.__create_config()
        with open(self.path+"config.json","w") as file:
            json.dump(item, file, indent=7)
        
    def __check_loc(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            
            
    def setup_main(self):
        self.__check_loc()
        self.__save_bot()
        self.__save_config()