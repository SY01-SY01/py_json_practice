import json, japanize_matplotlib
import matplotlib.pyplot as plt

date = json.load(open("pi.json",encoding="UTF-8"))

values = [i[0] for i in date]
labels = [i[1] for i in date]

plt.pie(values,labels=labels)
plt.show()
