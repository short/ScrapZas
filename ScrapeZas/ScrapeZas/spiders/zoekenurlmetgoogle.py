try:
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# zoektermen voorbereiden
keywordlist = ["utrecht", "softdrugs", "harddrugs", "hasj", "xtc", "mdma", "MDMA", "pma", "speed", "pep", "heroine", "sos", "M",
            "dexies", "truffels", "paddo's", "dexamfetamine", "creak", "wiet", "GHB", "cocaine", "delivery", "versneden",
            "pasta", "gram", "milligram", "mg", "delivery", "bezorgen", "dealers", "ecstasy", "snuif", "snuiven",
            "snatsen", "kwaliteit", "dealer", "pillen", "festivals", "festival", "lachgas", "amfetamine", "cannabis",
            "assie", "coke", "wit", "liter", "kilo", "k", "shop", "naalden", "smartshop", "smart shop", "magic",
            "mushrooms", "locatie", "sell", "buy", "kopen", "verkopen", "puurc24", "bokser101232@gmail.com", "31686465870", "Fdelivery", "Fdelivery@protonmail.com",
            "2CB", "utrechtdeliver", "Highline1", "whitemarket", "Partysquad19", "0685036987", "gedrukt", "stuk", "mropium", "Ketamine",
            "kristallen", "jasper030"]



for woorden in range(len(keywordlist)):
    a = keywordlist[50 + woorden]
    for woorden in range(len(keywordlist)):
        if keywordlist[woorden] != a:
            b = a + ' ' + str(keywordlist[woorden])
            for woorden in range(len(keywordlist)):
                if keywordlist[woorden] != a:
                    query = b + ' ' + str(keywordlist[woorden])
                    print(query)
                    with open('paginalijst', 'w+') as paginalijst:
                        for j in search(str(query), tld='.nl', stop=30, pause=11):
                            a = j.split()
                            for items in range(len(a)):
                                print(a[items] + '\n')
                                paginalijst.write(str(a[items] + '\n'))
        else:
            query = a



#daadwerkelijk vinden van de links







