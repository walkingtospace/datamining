import itertools
import networkx as nx

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