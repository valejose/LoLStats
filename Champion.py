class Champion:
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

    def __init__(self, championData):
        self.version = championData['version']
        self.id = championData['id']
        self.key = championData['key']
        self.name = championData['name']
        self.title = championData['title']
        self.blurb = championData['blurb']
        self.info = championData['info']
        self.image = championData['image']
        self.tags = championData['tags']
        self.partype = championData['partype']
        self.stats = championData['stats']

        def toString(self):
        ret = "\n"
        ret += "version: " + self.version + "\n"
        ret += "id: " + self.id + "\n"
        ret += "key: " + self.key + "\n"
        ret += "name: " + self.name + "\n"
        ret += "title: " + self.title + "\n"
        ret += "blurb: " + self.blurb + "\n"
        ret += "info: " + self.info + "\n"
        ret += "image: " + self.image + "\n"
        ret += "tags: " + self.tags + "\n"
        ret += "partype: " + self.partype + "\n"
        ret += "stats: " + self.stats + "\n"
        return ret