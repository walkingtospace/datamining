import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class SelectKeys(BaseEstimator, TransformerMixin):
	"""Transforms a list of a dictionaries into a list of subset dictionaries.
	For each dictionary, select a subset of their key and values."""
	def __init__(self, keys):
		self.keys = keys
	def fit(self, x, y=None):
		return self
	def transform(self, data):
		return np.array([{k: d[k] for k in self.keys} for d in data])

class SelectValue(BaseEstimator, TransformerMixin):
	"""Transforms a list of dictionaries into a list of values by selecting the value 
	of the given key for each dictionary."""
	def __init__(self, key):
		self.key = key
	def fit(self, x, y=None):
		return self
	def transform(self, data):
		return [d[self.key] for d in data]

class ApplyFunc(BaseEstimator, TransformerMixin):
	"""Transforms a list of values by apply the function to each value."""
	def __init__(self, f):
		self.f = f
	def fit(self, x, y=None):
		return self
	def transform(self, data):
		return [self.f(d) for d in data]

class IdentityVectorizer(BaseEstimator, TransformerMixin):
	"""Wraps data values in a list."""
	def __init__(self):
		pass
	def fit(self, x, y=None):
		return self
	def transform(self, data):
		return [[d] for d in data]

class UserReviews(BaseEstimator, TransformerMixin):
	"""Wraps data values in a list."""
	def __init__(self, userReviewMap):
		self.userReviewMap = userReviewMap
	def userReviews(self, user):
		return self.userReviewMap[user['user_id']]
	def fit(self, x, y=None):
		return self
	def transform(self, users):
		return [self.userReviews(u) for u in users]

class UserReviewText(BaseEstimator, TransformerMixin):
	"""Wraps data values in a list."""
	def __init__(self, userReviewMap):
		self.userReviewMap = userReviewMap
	def userReviews(self, user):
		return self.userReviewMap[user['user_id']]
	def concatReviewText(self, reviews):
		return " ".join((r['text'] for r in reviews))
	def fit(self, x, y=None):
		return self
	def transform(self, users):
		return [self.concatReviewText(self.userReviews(u)) for u in users]
    
class UserEliteFriends(BaseEstimator, TransformerMixin):
	"""Wraps data values in a list."""
	def __init__(self, localEliteFriends):
		self.localEliteFriends = localEliteFriends
	def fit(self, x, y=None):
		return self
	def transform(self, users):
		return [self.localEliteFriends[u['user_id']] for u in users]