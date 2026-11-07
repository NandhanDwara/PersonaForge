import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
df=pd.read_csv('2025-11-16_14-04-41.csv')
filtered = df[df["speaker"] == "Gustave"]
filtered_happiness=df[((df["speaker"] == "Gustave") & (df["happiness"]>0))]
filtered_ambitious=df[((df["speaker"] == "Gustave") & (df["ambitious"]>0))]
filtered_surprise=df[((df["speaker"] == "Gustave") & (df["surprise"]>0))]
filtered_anger=df[((df["speaker"] == "Gustave") & (df["surprise"]>0))]
filtered_sadness=df[((df["speaker"] == "Gustave") & (df["sadness"]>0))]
filtered_fear=df[((df["speaker"] == "Gustave") & (df["fear"]>0))]
filtered_neutral=df[((df["speaker"] == "Gustave") & (df["neutral"]>0))]
filtered.to_json("happy_characters.json", orient="records", indent=4)
emotions_displayed=np.array(['ambitious','anger','fear','happiness','sadness','surprise'])
emotional_value=np.array([len(filtered_ambitious),len(filtered_anger),len(filtered_fear),len(filtered_happiness),len(filtered_sadness),len(filtered_surprise)])
mp.bar(emotions_displayed,emotional_value)
mp.title("Emotion study of Gustave")
mp.xlabel("Emotion")
mp.ylabel("Emotion frequency")
mp.show()