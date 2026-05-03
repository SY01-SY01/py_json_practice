import json,requests,japanize_matplotlib
import matplotlib.pyplot as plt

url = "https://api.aoikujira.com/like/api.php?m=get&item_id=8"
r = requests.get(url)

data = json.loads(r.text)


labals,values =[],[]

for it in data["answers"]:
    labals.append(it["label"])
    values.append(it["point"])

plt.barh(labals,values)
plt.title("好きなOSは？")
plt.show()    