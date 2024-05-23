import requests
import json

tksm_url = "https://api.takasumibot.com/v1/"

class tksm_usr:
    def __init__(self, id: int):
        self.id = id
        self.req = (requests.get(f"{tksm_url}discord/user?id={self.id}"), requests.get(f"{tksm_url}money"))
        self.reqj = (json.loads(self.req[0].text), json.loads(self.req[1].text))
        self.reqd = (self.reqj[0]["data"], self.reqj[1]["data"])
        for i in range(len(self.reqd[1])):
            if self.reqd[1][i]["id"] == str(self.id):
                self.data = (self.reqd[1][i])
                break

usr = tksm_usr(874430259599142922)

print(usr.data)
