from .header import Header
from http.client import HTTPSConnection
from sys import stderr
from json import dumps

def connect():
    return HTTPSConnection("discordapp.com", 443)

class Main:
    def __init__(self):
        self.header = Header()
        
    def send_msg(self, msg, chn_id):
        conn = connect()
        try:
            conn.request(
                    "POST", 
                    f"/api/v6/channels/{chn_id}/messages", 
                    dumps(self.header.get_msg_ctx(msg)), 
                    self.header.get_header()
                )
            resp = conn.getresponse()
            if 199 < resp.status < 300:
                pass
            else:
                stderr.write(f"While sending message, received HTTP {resp.status}: {resp.reason}\n")
                pass
        except:
            stderr.write("Failed to send_message\n")
    
    def get_embed(self, chn_id):
        channel = connect().request(
                "GET", 
                f"/api/v6/channels/{chn_id}/messages", 
                headers=self.header.get_header()
            )
        resp = connect().getresponse()

        if 199 < resp.status < 300:
            resp_string = str(resp.read(600))

            return resp_string

        else:
            stderr.write(f"While checking message, received HTTP {resp.status}: {resp.reason}\n")
            pass
    
    
    
    def get_text():
        pass