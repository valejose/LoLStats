import json
import pprint
import requests

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

def loadChampionsJson():
    json_file = open('.vscode/champions.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)
    return json_data['data']

def requestSummonerData(summonerName, APIKey):
    URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestMatchData(accountId, APIKey):
    URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

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
    summonerName = "Legend Master"
    APIKey = "RGAPI-a6406680-2848-4857-89d9-69fb9608612f"

    champions = loadChampionsJson()
    responseJSON = requestSummonerData(summonerName, APIKey)
    summonerLevel = responseJSON['summonerLevel']
    accountId = responseJSON['accountId']
    matchData = requestMatchData(accountId, APIKey)
    mostRecentGameId = matchData['matches'][0]['gameId']
    championOccurences = getCountChampionOccurencesInMatches(matchData)  

    print("Summoner's Name: " + summonerName)
    print("Summoner's Level: " + str(summonerLevel))
    print("\n")
    print("Most recent game id: " + str(mostRecentGameId))
    print("\n")

    for x in championOccurences:
        x = str(x)
        name = getChampionNameByKey(champions.values(), x)
        timesPlayed = championOccurences[x] 
        print(name + " was played " + str(timesPlayed) + " times")
    print("\n")

if __name__ == "__main__":
    main()