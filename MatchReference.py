import datetime

class MatchReference:
    # LucidChart Visual: https://www.lucidchart.com/documents/edit/c418d0f7-0a48-4ca8-8608-b4bdfafad002/1?beaconFlowId=DED0DE9F7A7CD204

    # ---Attributes---
    # lane:string
    # gameId:long
    # champion:int
    # platformId:string
    # season:int
    # queue:int
    # role:string
    # timestamp:long

    def __init__(self, matchReferenceData):
        self.lane = matchReferenceData['lane']
        self.gameId = matchReferenceData['gameId']
        self.champion = matchReferenceData['champion']
        self.platformId = matchReferenceData['platformId']
        self.season = matchReferenceData['season']
        self.queue = matchReferenceData['queue']
        self.role = matchReferenceData['role']
        self.timestamp = matchReferenceData['timestamp']

    def getTimestampAsDateTime(self):
        return datetime.datetime.fromtimestamp(self.timestamp / 1e3)

    def toString(self):
        ret = "\n"
        ret += "lane: " + self.lane + "\n"
        ret += "gameId: " + str(self.gameId) + "\n"
        ret += "champion: " + str(self.champion) + "\n"
        ret += "platformId: " + self.platformId + "\n"
        ret += "season: " + str(self.season) + "\n"
        ret += "queue: " + str(self.queue) + "\n"
        ret += "role: " + self.role + "\n"
        ret += "timestamp: " + str(self.getTimestampAsDateTime()) + "\n"
        return ret
