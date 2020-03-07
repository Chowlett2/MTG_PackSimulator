import random
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd

def cardSet(name, link):
    page = requests.get(link, timeout = 35)
    content = soup(page.text, "html.parser")
    tbody = content.find('tbody')
    trs = tbody.find_all('tr')
    final_results = []

    for i in trs:
        results = i.text.splitlines()
        results = [i.strip().strip('$') for i in results if i != '']
        final_results.append(results)
    final_results = final_results[1:]

    name = pd.DataFrame.from_records(final_results)
    name = name.drop(name.columns[[2, 4, 6, 8, 10, 11]], axis=1)
    name.columns = ['Card Name', 'Rarity', 'Serial no.', 'Market Price',
                    'Buylist Price', 'Listed Median']
    return name

#guilds = cardSet('guilds', 'https://shop.tcgplayer.com/price-guide/magic/guilds-of-ravnica')
#allegiance = cardSet('allegiance', 'https://shop.tcgplayer.com/price-guide/magic/ravnica-allegiance')
#spark = cardSet('spark', 'https://shop.tcgplayer.com/price-guide/magic/war-of-the-spark')
#core2020 = cardSet('core2020', 'https://shop.tcgplayer.com/price-guide/magic/core-set-2020')
eldraine = cardSet('eldraine', 'https://shop.tcgplayer.com/price-guide/magic/throne-of-eldraine')

def packStats():
    '''
    User inputs the set for which they want to open packs.
    Returns the breakdown of which rarities and card types are to be returned
    '''        
    common = 9
    uncommon = 3
    rare = 0
    mythic = 0
    land = 1
    token = 1
    foil = 0    
    mythicChance = random.randint(1, 8)
    foilChance = random.randint(1, 6) 
    while True:
        if mythicChance == 8:
            mythic += 1
        else:
            rare += 1   
        break
    while True:
        if foilChance == 6:
            foil += 1
        else:
            common += 1 
        break        
    pack = [common, uncommon, rare, mythic, land, token, foil]   
    return pack

(commonIndex, uncommonIndex, rareIndex, mythicIndex, 
 landIndex, tokenIndex, foilIndex) = packStats()[:]

def showPack():
    
    (commonIndex, uncommonIndex, rareIndex, mythicIndex, 
     landIndex, tokenIndex, foilIndex) = packStats()[:]
        
    while foilIndex > 0:
        print(str(eldraine['Card Name'].sample().values) + 'FOIL')
        foilIndex -= 1
    while commonIndex > 0:
        print(str(eldraine[eldraine['Rarity'] == 'C'].sample()["Card Name"].values))
        commonIndex -= 1
    while uncommonIndex > 0:
        print(str(eldraine[eldraine['Rarity'] == 'U'].sample()["Card Name"].values))
        uncommonIndex -= 1
    while rareIndex > 0:
        print(str(eldraine[eldraine['Rarity'] == 'R'].sample()["Card Name"].values))
        rareIndex -= 1
    while mythicIndex > 0:
        print(str(eldraine[eldraine['Rarity'] == 'M'].sample()["Card Name"].values))
        mythicIndex -= 1
    while landIndex > 0:
        print(str(eldraine[eldraine['Rarity'] == 'L'].sample()["Card Name"].values))
        landIndex -= 1
    while tokenIndex > 0:
        print(str(eldraine[eldraine['Rarity'] == 'T'].sample()["Card Name"].values))
        tokenIndex -= 1
    
def packValue():
    
    total = 0.00
    
    (commonIndex, uncommonIndex, rareIndex, mythicIndex, 
     landIndex, tokenIndex, foilIndex) = packStats()[:]
    
    while foilIndex > 0:
        try:    
            total += (float(eldraine['Buylist Price'].sample().values))
        except:
            ValueError
        foilIndex -= 1
    while commonIndex > 0:
        try:
            total += (float(eldraine[eldraine['Rarity'] == 'C'].sample()["Buylist Price"].values))
        except:
            ValueError
        commonIndex -= 1
    while uncommonIndex > 0:
        try:
            total += (float(eldraine[eldraine['Rarity'] == 'U'].sample()["Buylist Price"].values))
        except:
            ValueError
        uncommonIndex -= 1
    while rareIndex > 0:
        try:
            total += (float(eldraine[eldraine['Rarity'] == 'R'].sample()["Buylist Price"].values))
        except:
            ValueError
        rareIndex -= 1
    while mythicIndex > 0:
        try:
            total += (float(eldraine[eldraine['Rarity'] == 'M'].sample()["Card Name"].values))
        except:
            ValueError
        mythicIndex -= 1
    while landIndex > 0:
        try:
            total += (float(eldraine[eldraine['Rarity'] == 'L'].sample()["Card Name"].values))
        except:
            ValueError
        landIndex -= 1
    while tokenIndex > 0:
        try:
            total += (float(eldraine[eldraine['Rarity'] == 'T'].sample()["Card Name"].values))
        except:
            ValueError
        tokenIndex -= 1
    total = (round(total, 2))
    return total
    
def testCase(num):
    count = num
    final = 0.00
    while count > 0:
        final += (packValue())
        count -= 1
    return round(final/num, 2)

showPack()

# print(testCase(1000))