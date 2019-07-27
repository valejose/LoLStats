import datetime

class Mastery:
    # LucidChart Visual: https://www.lucidchart.com/documents/edit/c418d0f7-0a48-4ca8-8608-b4bdfafad002/2?beaconFlowId=DED0DE9F7A7CD204
    
    # ---Attributes---
    # chestGranted:boolean
    # championLevel:int
    # championPoints:int
    # championId:long
    # championPointsUntilNextLevel:long
    # lastPlayTime:long
    # tokensEarned:int
    # championPointsSinceLastLevel:long
    # summonerId:string

    def __init__(self, masteryData):
        self.chestGranted = masteryData['chestGranted']
        self.championLevel = masteryData['championLevel']
        self.championPoints = masteryData['championPoints']
        self.championId = masteryData['championId']
        self.championPointsUntilNextLevel = masteryData['championPointsUntilNextLevel']
        self.lastPlayTime = masteryData['lastPlayTime']
        self.tokensEarned = masteryData['tokensEarned']
        self.championPointsSinceLastLevel = masteryData['championPointsSinceLastLevel']
        self.summonerId = masteryData['summonerId']

    def getLastPlayTimeAsDateTime(self):
        return datetime.datetime.fromtimestamp(self.lastPlayTime / 1e3)

    def toString(self):
        ret = "\n"
        ret += "chestGranted: " + str(self.chestGranted) + "\n"
        ret += "championLevel: " + str(self.championLevel) + "\n"
        ret += "championPoints: " + str(self.championPoints) + "\n"
        ret += "championId: " + str(self.championId) + "\n"
        ret += "championPointsUntilNextLevel: " + str(self.championPointsUntilNextLevel) + "\n"
        ret += "lastPlayTime: " + str(self.getLastPlayTimeAsDateTime()) + "\n"
        ret += "tokensEarned: " + str(self.tokensEarned) + "\n"
        ret += "championPointsSinceLastLevel: " + str(self.championPointsSinceLastLevel) + "\n"
        ret += "summonerId: " + self.summonerId + "\n"
        return ret
        