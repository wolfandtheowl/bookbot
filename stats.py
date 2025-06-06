def wordcounter(text):
    counter = []
    counter = text.split()
    words = 0
    for count in counter:
        words += 1
    return words

def tpcfreq(text):
    flattext = text.lower()
    characters = {'t':0,'p':0,'c':0}
    for c in flattext:
        if c == "t":
            characters["t"] += 1
        elif c == "p":
            characters["p"] += 1
        elif c == "c":
            characters["c"] += 1
    return characters

def freqsort(text):
    flattext = text.lower()
    chardic = {}
    alphabet = "abcdefghijklmnopqrstuvwxyzæâêëô"
    diccy = {}
    diclist = []
    for letter in alphabet:
        chardic[letter] = 0
        for char in flattext:
            if char == letter:
                chardic[char] += 1
    for key, value in chardic.items():
        diccy = {"char": key, "num": value}
        diclist.append(diccy)
        # print(f"added {diccy} to diclist")
    return diclist

def sort_on(dict):
    return dict["num"]
