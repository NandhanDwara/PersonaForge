import basic_emotional_analysis as bs
import matplotlib.pyplot as plt
import numpy as np
chapters=bs.filtered['chapter'].unique()

# chapterwise ambition analysis

gommage_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='The Gommage']
festival_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='Festival de l’Expédition']
spring_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='Spring Meadows']
Flying_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='Flying Waters']
Sanctuary_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='Ancient Sanctuary']
Gestral_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='Gestral Village']
Nest_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='Esquie’s Nest']
Cliffs_ambition=bs.filtered_ambitious[bs.filtered_ambitious['chapter']=='Stone Wave Cliffs']

#chapterwise Anger analysis

gommage_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='The Gommage']
festival_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='Festival de l’Expédition']
spring_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='Spring Meadows']
Flying_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='Flying Waters']
Sanctuary_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='Ancient Sanctuary']
Gestral_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='Gestral Village']
Nest_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='Esquie’s Nest']
Cliffs_anger=bs.filtered_anger[bs.filtered_anger['chapter']=='Stone Wave Cliffs']

#chapterwise Fear analysis

gommage_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='The Gommage']
festival_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='Festival de l’Expédition']
spring_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='Spring Meadows']
Flying_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='Flying Waters']
Sanctuary_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='Ancient Sanctuary']
Gestral_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='Gestral Village']
Nest_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='Esquie’s Nest']
Cliffs_fear=bs.filtered_fear[bs.filtered_fear['chapter']=='Stone Wave Cliffs']

#chapterwise Happiness analysis

gommage_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='The Gommage']
festival_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='Festival de l’Expédition']
spring_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='Spring Meadows']
Flying_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='Flying Waters']
Sanctuary_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='Ancient Sanctuary']
Gestral_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='Gestral Village']
Nest_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='Esquie’s Nest']
Cliffs_happiness=bs.filtered_happiness[bs.filtered_happiness['chapter']=='Stone Wave Cliffs']

#chapterwise Sadness analysis

gommage_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='The Gommage']
festival_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='Festival de l’Expédition']
spring_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='Spring Meadows']
Flying_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='Flying Waters']
Sanctuary_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='Ancient Sanctuary']
Gestral_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='Gestral Village']
Nest_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='Esquie’s Nest']
Cliffs_sadness=bs.filtered_sadness[bs.filtered_sadness['chapter']=='Stone Wave Cliffs']

#chapterwise Surprise analysis

gommage_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='The Gommage']
festival_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='Festival de l’Expédition']
spring_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='Spring Meadows']
Flying_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='Flying Waters']
Sanctuary_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='Ancient Sanctuary']
Gestral_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='Gestral Village']
Nest_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='Esquie’s Nest']
Cliffs_surprise=bs.filtered_surprise[bs.filtered_surprise['chapter']=='Stone Wave Cliffs']

data=np.array([[len(gommage_ambition),len(gommage_anger),len(gommage_fear),len(gommage_happiness),len(gommage_sadness),len(gommage_surprise)],
      [len(festival_ambition),len(festival_anger),len(festival_fear),len(festival_happiness),len(festival_sadness),len(festival_surprise)],
      [len(spring_ambition),len(spring_anger),len(spring_fear),len(spring_happiness),len(spring_sadness),len(spring_surprise)],
      [len(Flying_ambition),len(Flying_anger),len(Flying_fear),len(Flying_happiness),len(Flying_sadness),len(Flying_surprise)],
      [len(Sanctuary_ambition),len(Sanctuary_anger),len(Sanctuary_fear),len(Sanctuary_happiness),len(Sanctuary_sadness),len(Sanctuary_surprise)],
      [len(Gestral_ambition),len(Gestral_anger),len(Gestral_fear),len(Gestral_happiness),len(Gestral_sadness),len(Gestral_surprise)],
      [len(Nest_ambition),len(Nest_anger),len(Nest_fear),len(Nest_happiness),len(Nest_sadness),len(Nest_surprise)],
      [len(Cliffs_ambition),len(Cliffs_anger),len(Cliffs_fear),len(Cliffs_happiness),len(Cliffs_sadness),len(Cliffs_surprise)]
      ])
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
axes = axes.flatten()

for i in range(8):
    axes[i].pie(data[i], labels=['Ambition', 'Anger', 'Fear','Happiness','Sadness','Surprise'], autopct='%1.1f%%')
    axes[i].set_title(chapters[i])

plt.tight_layout()
plt.show()