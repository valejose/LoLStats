from MatchReference import MatchReference

class MatchList:
    # LucidChart Visual: https://www.lucidchart.com/documents/edit/c418d0f7-0a48-4ca8-8608-b4bdfafad002/1?beaconFlowId=DED0DE9F7A7CD204

    # ---Attributes---
    # matches:List[MatchReferenceDTO]
    # totalGames:int
    # startIndex:int
    # endIndex:int

    def __init__(self, data):
        matchReferenceList = []
        for matchReference in data['matches']:
            matchReferenceList.append(MatchReference(matchReference))

        self.matches = matchReferenceList
        self.totalGames = data['totalGames']
        self.startIndex = data['startIndex']
        self.endIndex = data['endIndex']

    def getMostRecentMatchId(self):
        return self.matches[0].gameId

    def getRolesList(self):
        rolesList = []
        for x in self.matches:
            rolesList.append(x.role)
        return rolesList

    def getLanesList(self):
        lanesList = []
        for x in self.matches:
            lanesList.append(x.lane)
        return lanesList

    def toString(self):
        ret = "\n"
        ret += "matches:\n"
        for m in self.matches:
            ret += m.toString()
        ret += "totalGames: " + str(self.totalGames) + "\n"
        ret += "startIndex: " + str(self.startIndex) + "\n"
        ret += "endIndex: " + str(self.endIndex) + "\n"
        return ret
