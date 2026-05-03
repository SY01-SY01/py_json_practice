import json , japanize_matplotlib
import matplotlib.pyplot as plt
import requests, os ,time, json
import urllib.parse
from bs4 import BeautifulSoup

savefile = "janken_history.json"
with open(savefile,encoding="UTF-8") as fp:
    history = json.load(fp)

win,lose,draw = 0,0,0
hand = [0,0,0]
for i in history:
    if i["result"] =="あいこ":
        draw +=1
    if i["result"] =="負け":
        lose +=1
    if i["result"] =="勝ち":
        win +=1
        hand[i["user"]] += 1


print("勝率:",win / (win+lose))
plt.subplot(1,2,1)
plt.pie([win,lose,draw],labels=["勝ち","負け","あいこ"],autopct="%1.1f %%")
plt.title("勝敗")

plt.subplot(1,2,2)
plt.barh(["グー","チョキ","パー"],hand)
plt.title("どの手で勝ったか")

plt.show()
