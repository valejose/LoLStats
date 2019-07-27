class Participant:
    # ---Attributes---
    # stats:ParticipantStatsDto
    # participantId:int
    # runes:List[RuneDto]
    # timeline:ParticipantTimelineDto
    # teamId:int
    # spell2Id:int
    # masteries:List[MasteryDto]
    # highestAchievedSeasonTier:string
    # spell1Id:int
    # championId:int

    def __init__(self, data):
        self.stats = data['stats']
        self.participantId = data['participantId']
        self.runes = data['runes']
        self.timeline = data['timeline']
        self.teamId = data['teamId']
        self.spell2Id = data['spell2Id']
        self.masteries = data['masteries']
        self.highestAchievedSeasonTier = data['highestAchievedSeasonTier']
        self.spell1Id = data['spell1Id']
        self.championId = data['championId']

class Player:
    # ---Attributes---
    # currentPlatformId:string
    # summonerName:string
    # matchHistoryUri:string
    # platformId:string
    # currentAccountId:string
    # profileIcon:int
    # summonerId:string
    # accountId:string

    def __init__(self, data):
        self.currentPlatformId = data['currentPlatformId']
        self.summonerName = data['summonerName']
        self.matchHistoryUri = data['matchHistoryUri']
        self.platformId = data['platformId']
        self.currentAccountId = data['currentAccountId']
        self.profileIcon = data['profileIcon']
        self.summonerId = data['summonerId']
        self.accountId = data['accountId']

    def toString(self):
        ret = "\n"
        ret += "currentPlatformId: " + self.currentPlatformId + "\n"
        ret += "summonerName: " + self.summonerName + "\n"
        ret += "matchHistoryUri: " + self.matchHistoryUri + "\n"
        ret += "platformId: " + self.platformId + "\n"
        ret += "currentAccountId: " + self.currentAccountId + "\n"
        ret += "profileIcon: " + str(self.profileIcon) + "\n"
        ret += "summonerId: " + self.summonerId + "\n"
        ret += "accountId: " + self.accountId + "\n"
        return ret

class ParticipationIdentity:
    # ---Attributes---
    # player:PlayerDto
    # participantId:int

    def __init__(self, data):
        self.player = Player(data['player'])
        self.participantId = data['participantId']

    def toString(self):
        ret = "\n"
        ret += "Player: " + self.player.toString() + "\n"
        ret += "participantId: " + str(self.participantId) + "\n"
        return ret 

class Match:
    # LucidChart Visual: https://www.lucidchart.com/documents/edit/c418d0f7-0a48-4ca8-8608-b4bdfafad002/1?beaconFlowId=DED0DE9F7A7CD204

    # ---Attributes---
    # seasonId:int
    # queueId:int
    # gameId:long
    # participantIdentities:List[ParticipantIdentityDto]
    # gameVersion:string
    # platformId:string
    # gameMode:string
    # mapId:int
    # gameType:string
    # teams:List[TeamStatsDto]
    # participants:List[ParticipantDto]
    # gameDuration:long
    # gameCreation:long

    def __init__(self, data):
        participantIdentitiesList = []
        for participantIdentity in data['participantIdentities']:
            participantIdentitiesList.append(ParticipationIdentity(participantIdentity))

        self.seasonId = data['seasonId']
        self.queueId = data['queueId']
        self.gameId = data['gameId']
        self.participantIdentities = participantIdentitiesList
        self.gameVersion = data['gameVersion']
        self.platformId = data['platformId']
        self.gameMode = data['gameMode']
        self.mapId = data['mapId']
        self.gameType = data['gameType']
        self.teams = data['teams']
        self.participants = data['participants']
        self.gameDuration = data['gameDuration']
        self.gameCreation = data['gameCreation']

    def toString(self):
        ret = "\n"
        ret += "seasonId: " + str(self.seasonId) + "\n"
        ret += "queueId: " + str(self.queueId) + "\n"
        ret += "gameId: " + str(self.gameId) + "\n"
        ret += "participantIdentities:\n"
        for p in self.participantIdentities:
            ret += p.toString()
        ret += "gameVersion: " + str(self.gameVersion) + "\n"
        ret += "platformId: " + str(self.platformId) + "\n"
        ret += "gameMode: " + str(self.gameMode) + "\n"
        ret += "mapId: " + str(self.mapId) + "\n"
        ret += "gameType: " + str(self.gameType) + "\n"
        ret += "teams: " + str(self.teams) + "\n"
        ret += "participants: " + str(self.participants) + "\n"
        ret += "gameDuration: " + str(self.gameDuration) + "\n"
        ret += "gameCreation: " + str(self.gameCreation) + "\n"
        return ret
