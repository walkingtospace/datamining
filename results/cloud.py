import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def invertWeights(wordFreqs):
	return [(f, w * -1) for f, w in wordFreqs]

with open('log_weights.tsv') as f:
	weights = [row for row in csv.reader(f, delimiter='\t')]

cities = [(f.split('/')[1], float(w)) for f, w in weights if f.startswith('cities') and f != 'cities/Montreal']
cats = [(f.split('/')[1], float(w)) for f, w in weights if f.startswith('category')]
comps = [(f.split('/')[1], float(w)) for f, w in weights if f.startswith('compliments')]

wc = WordCloud().generate_from_frequencies(cities)
wc.to_file("elite_cities.png")

wc = WordCloud().generate_from_frequencies(invertWeights(cities))
wc.to_file("nonelite_cities.png")

wc = WordCloud().generate_from_frequencies(cats)
wc.to_file("elite_cats.png")

wc = WordCloud().generate_from_frequencies(invertWeights(cats))
wc.to_file("nonelite_cats.png")

wc = WordCloud().generate_from_frequencies(comps)
wc.to_file("elite_comps.png")

