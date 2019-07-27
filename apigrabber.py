import json
import pprint
import requests

from Summoner import Summoner
from Mastery import Mastery

# Takes in a failed API Query response status and prints it to the user
def printError(status):
    statusCode = status['status_code']
    message = status['message']
    print("Status code " + str(statusCode) + ": " + message)

# Creates a json file based on the champions.json file found here http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json 
# This was to learn how to find the specific information that I wanted and to make a JSON file that was easier to use
def saveJsonFile():
    champions = json.loads(open('.vscode/champions.json').read())

    formatChamps = {}
    for name in champions['data']:
        key = champions['data'][name]['key']
        tags = champions['data'][name]['tags']
        title = champions['data'][name]['title']

        formatChamps.update({key: {"name": name, "tags": tags, "title": title}})

    with open('.vscode/champions_by_id.json', 'w') as fp:
        json.dump(formatChamps, fp, indent=4)

# Loads all the champion data and returns it
def loadChampionsJson():
    json_file = open('.vscode/champions.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)
    return json_data['data']

# Makes a query to the Riot API for information about a specific summoner and returns it
# Returns: SummonerDTO
def requestSummonerDataByName(summonerName, APIKey):
    URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    if response.status_code == requests.codes['ok']:
        return response.json()
    else:
        printError(response.json()['status'])
        return None

# Makes a query to the Riot API for information about a specific summoner and returns it
# Returns: SummonerDTO
def requestSummonerDataByAccount(accountId, APIKey):
    URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-account/" + accountId + "?api_key=" + APIKey
    response = requests.get(URL)
    if response.status_code == requests.codes['ok']:
        return response.json()
    else:
        printError(response.json()['status'])
        return None

# Makes a query to the Riot API for information about a specific summoners match history and returns it
def requestMatchData(accountId, APIKey):
    URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestAllMasteryDataForSummoner(summonerId, APIKey):
    URL = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId + "?api_key=" + APIKey
    response = requests.get(URL)
    if response.status_code == requests.codes['ok']:
        return response.json()
    else:
        printError(response.json()['status'])
        return None

def requestMasteryDataForSingleChampionOfSummoner(summonerId, championId, APIKey):
    URL = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId + "/by-champion/" + str(championId) + "?api_key=" + APIKey
    response = requests.get(URL)
    if response.status_code == requests.codes['ok']:
        return response.json()
    else:
        printError(response.json()['status'])
        return None

def getCountChampionOccurencesInMatches(matchData):
    matches = matchData['matches']

    championsArr = {}
    for match in matches:
        champion = str(match['champion'])
        if not champion in championsArr:
            championsArr[champion] = 1
        else:
            championsArr[champion] += 1
    
    return championsArr

def getChampionNameByKey(champions, search_key):
    for i in champions:
        if i['key'] == search_key:
            return i['name']

def main():
    summonerName = "Cefiroth"
    # APIKey = "GAPI-ddf82131-cea0-4065-937f-6f976fcfc8bb"
    APIKey = "RGAPI-ddf82131-cea0-4065-937f-6f976fcfc8bb"

    summonerData = requestSummonerDataByName(summonerName, APIKey)
    if summonerData != None:
        mySummoner = Summoner(summonerData)
        print(mySummoner.toString())

    masteryData = requestMasteryDataForSingleChampionOfSummoner(mySummoner.id, 143, APIKey)
    if masteryData != None:
        myMasteryData = Mastery(masteryData) 
        print(myMasteryData.toString())

    allMasteryData = requestAllMasteryDataForSummoner(mySummoner.id, APIKey)
    if allMasteryData != None:
        for masteryInfo in allMasteryData:
            m = Mastery(masteryInfo)
            print(m.toString())

    # matchData = requestMatchData(mySummoner.accountId, APIKey)
    # championOccurences = getCountChampionOccurencesInMatches(matchData)  

    # print("Summoner's Name: " + mySummoner.name)
    # print("Summoner's Level: " + str(mySummoner.summonerLevel))
    # print("\n")

    # champions = loadChampionsJson()
    # for x in championOccurences:
    #     x = str(x)
    #     name = getChampionNameByKey(champions.values(), x)
    #     timesPlayed = championOccurences[x] 
    #     print(name + " was played " + str(timesPlayed) + " times")
    # print("\n")

if __name__ == "__main__":
    main()
