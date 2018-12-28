import pandas as pd
import random

header = ["id", "name", "rarity", "idolized_url", "unidolized_url"]
df = pd.read_csv("idols.csv", names = header)

def single_pull():
    pull = df.sample(1).values[0]
    return "You got " + pull[2] + " " + pull[1] + "! Congratulations! https:" + pull[3]