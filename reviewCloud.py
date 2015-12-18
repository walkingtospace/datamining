import csv
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from util import *

with open('../data/yelp_academic_dataset_user.json') as f:
    users = [json.loads(line) for line in f]
with open('../data/yelp_academic_dataset_review.json') as f:
    reviews = [json.loads(line) for line in f]

userMap = mapUsers(users)
userReviewMap = mapReviewsByUsers(reviews)

eliteReviewText = ""
for u in users:
	if isElite(u):
		for r in userReviewMap[u]:
			eliteReviewText += r['text']

print eliteReviewText
