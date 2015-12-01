import itertools
import networkx as nx
from collections import defaultdict
from collections import Counter
from scipy.cluster.vq import kmeans2, whiten
import numpy as np

"""X = [tempFeat(u) for u in users]"""
def getPearsonCorrelation(userId, X):
    y = [isElite(u) for u in users] 
    pc = np.corrcoef(X, y)
    print pc[0][1]
    
def isElite(user):
	"""True if user has ever been elite."""
	return True if user['elite'] else False

def isEliteYear(user, year):
	"""True if user is elite in the given year."""
	return year in user['elite']

def mapUsers(users):
	"""Index users into a map by their user id."""
	return {u['user_id']: u for u in users}

def mapBusinesses(businesses):
	"""Index businesses into a map by their business id."""
	return {b['business_id']: b for b in businesses}

def mapReviewsByUsers(reviews):
	"""Returns a map of list where keys are users and values
	are list of reviews made by that user."""
	sr = sorted(reviews, key=lambda r: (r['user_id'], r['date']))
	return {k: list(v) for k, v in itertools.groupby(sr, key=lambda r: r['user_id'])}

def graphUsers(users, attrs=['elite', 'review_count', 'type', 'compliments', 'votes', 'yelping_since']):
	"""Graph users by friends."""
	g = nx.Graph()
	for u in users:
		userID = u['user_id']
		g.add_node(userID)
		friendEdges = ((userID, f) for f in u['friends'])
		g.add_edges_from(friendEdges)
		for a in attrs:
			g.node[userID][a] = u[a]
	return g

def mostCommon(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

def getKmeans(reviews, businesses):
    geo_data = []

    for review in reviews:
        business_id = review['business_id']
        lat = businesses[business_id]['latitude']
        lon = businesses[business_id]['longitude']

        geo_data.append([lat, lon])
    centroid, label = kmeans2(whiten(geo_data), 10, iter = 50, minit='points') # clustering into 10 groups
    
    return centroid, label

def getLocalEliteFriends(reviews, users, label):
    user_group = defaultdict(list)
    elite_friends = defaultdict(list)
    idx = 0
    
    for review in reviews:
        user_id = review['user_id']
        group_num = label[idx]
        user_group[user_id].append(group_num)

        idx += 1

    for user_id in user_group:
        user_group[user_id] = mostCommon(user_group[user_id])

    for user_id in users:
        friends = users[user_id]['friends']

        same_group_cnt = 0
        for friend_id in friends:
            if friend_id not in user_group:
                print("none existing user" + friend_id)
                continue

            if user_group[friend_id] == user_group[user_id]:
                same_group_cnt += 1
        elite_friends[user_id] = same_group_cnt
        
    return elite_friends
