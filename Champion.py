class Champion:
    # LucidChart Visual: https://www.lucidchart.com/documents/edit/c418d0f7-0a48-4ca8-8608-b4bdfafad002/1?beaconFlowId=DED0DE9F7A7CD204
    
    # ---Attributes---
    # version:string
    # id:string
    # key:int
    # name:string
    # title:string
    # blurb:string
    # info:Info
    # image:Image
    # tags:List[string]
    # partype:string
    # stats:Stats

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
        ret += "id: " + str(self.id) + "\n"
        ret += "key: " + self.key + "\n"
        ret += "name: " + self.name + "\n"
        ret += "title: " + self.title + "\n"
        ret += "blurb: " + self.blurb + "\n"
        ret += "info: " + str(self.info) + "\n"
        ret += "image: " + str(self.image) + "\n"
        ret += "tags: " + str(self.tags) + "\n"
        ret += "partype: " + self.partype + "\n"
        ret += "stats: " + str(self.stats) + "\n"
        return ret
