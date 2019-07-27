import datetime

class Summoner:
    # LucidChart Visual: https://www.lucidchart.com/documents/edit/c418d0f7-0a48-4ca8-8608-b4bdfafad002/1?beaconFlowId=DED0DE9F7A7CD204
    
    # ---Attributes---
    # profileIconId:int   ID of the summoner icon associated with the summoner.
    # name:string         Summoner name.
    # puuid:string        Encrypted PUUID. Exact length of 78 characters.
    # summonerLevel:long  Summoner level associated with the summoner.
    # revisionDate:long   Date summoner was last modified specified as epoch milliseconds. 
    #                     The following events will update this timestamp: profile icon change, 
    #                     playing the tutorial or advanced tutorial, finishing a game, summoner name change
    # id:string           Encrypted summoner ID. Max length 63 characters.
    # accountId:string    Encrypted account ID. Max length 56 characters.

    def __init__(self, summonerData):
        self.profileIconId = summonerData['profileIconId']
        self.name = summonerData['name']
        self.puuid = summonerData['puuid']
        self.summonerLevel = summonerData['summonerLevel']
        self.revisionDate = summonerData['revisionDate']
        self.id = summonerData['id']
        self.accountId = summonerData['accountId']

    def getRevisionDateAsDateTime(self):
        return datetime.datetime.fromtimestamp(self.revisionDate / 1e3)

    def toString(self):
        ret = "\n"
        ret += "profileIconId: " + str(self.profileIconId) + "\n"
        ret += "name: " + self.name + "\n"
        ret += "puuid: " + self.puuid + "\n"
        ret += "summonerLevel: " + str(self.summonerLevel) + "\n"
        ret += "revisionDate: " + str(self.getRevisionDateAsDateTime()) + "\n"
        ret += "id: " + self.id + "\n"
        ret += "accountId: " + self.accountId
        return ret
        