from .send import Main as Sender
import os, json
from random import random
from datetime import datetime
from time import sleep

paths = os.path.join(os.getcwd(), "config/")

class cycle:
    def __init__(self):
        self.config = self.__get_config()
        self.Sender = Sender()
        
    def __get_config(self, item={}):
        with open(paths+"config.json","r") as file:
            return json.load(file)
    
    def cmd_loop(self):
        for cmd in self.config["commands"]:
            self.Sender.send_msg(cmd, self.config["channel_id"])
            sleep(3)
            sleep(random() * 7)
        sleep(self.config["intervals"])
        sleep(random() * 7)
    
    def start(self):
        print("Grinding the bot... " + (datetime.now()).strftime("%H:%M:%S"))
        while True:
            self.cmd_loop()