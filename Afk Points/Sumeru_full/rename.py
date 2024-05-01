from os import walk
import os

mypath = "D://github_project//Json_Integration//afk_point//Sumeru_full//"
filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file


dictionary = {
    "须弥":"sumeru",
    "苍漠":"Girdle of the Sands",
    "宝箱":"Chests",
    "挑战":"Challenge",
    "摩拉":"Mora",
    "神瞳":"Oculi",
    "解谜":"Puzzle"
    
}

for x in filenames:
    for meaning in dictionary.keys():

        y = (
            x.replace(meaning, dictionary[meaning])
        )

    source = mypath + x
    destination = mypath + y
    print(y)
    # os.rename(source, destination)
    
    
    
    