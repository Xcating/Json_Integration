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
    y = (
        x.replace("须弥", dictionary["须弥"])
          .replace("苍漠", dictionary["苍漠"])
          .replace("宝箱",dictionary["宝箱"])
          .replace("挑战", dictionary["挑战"])
          .replace("摩拉", dictionary["摩拉"])
          .replace("神瞳", dictionary["神瞳"])
          .replace("解谜", dictionary["解谜"])

    )
    source = mypath + x
    destination = mypath + y
    os.rename(source, destination)
    
    
    
    