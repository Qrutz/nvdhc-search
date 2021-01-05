import requests
import json


response = requests.get(
    "https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/DGrDvqSs7IsGJJHi36NSGZCGxOA3yZuRXqW9_o5iEXS2hn8VAt8kc7CxykKIUlATsRRevHG9pQeuRQ?api_key=RGAPI-bab00037-ae72-4304-961a-ff60f928737c")


with open("NVHSS/riot/result.json", "w") as y:
    json.dump(response.json(), y)


def getAccountDetails(dataType):
    with open('NVHSS/riot/accounts.json', 'r') as f:
        accounts_dict = json.load(f)
        return accounts_dict


def getAccountNames():
    accountNames = []
    AccountDict = getAccountDetails("name")
    for i in range(len(AccountDict)):
        accountNames.append(AccountDict[i])
    return accountNames


def AccountInput(inputforjson):
    with open("riot/accounts.json", "w") as d:
        json.dump(inputforjson, d)


AccountInputt = input("Type the account name you want to insert: ")

if type(AccountInputt) == str:
    print("Yes")


print(getAccountNames())
