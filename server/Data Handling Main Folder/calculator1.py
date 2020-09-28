import pandas as pd

dataset = pd.read_csv("allMatches_modified1-Copy.csv")

for i in range(0,640):
    if(dataset["home_team"][i]==dataset["winner"][i]):
        dataset["winner"][i]="home"
    if(dataset["away_team"][i]==dataset["winner"][i]):
        dataset["winner"][i]="away"


dataset.to_csv("allMatches_final.csv")
