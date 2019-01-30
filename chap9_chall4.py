import csv

list1 = ['トップガン', 'リスキービジネス', 'マイノリティリポート']
list2 = ['タイタニック', 'ザ　レブナント', 'インセプション']
list3 = ['トレーニングデイ', 'マン　オン　ファイア', 'フライト']

with open('movies2.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)
