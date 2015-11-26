_author__ = 'Honam Bang, hobang@ucsd.edu'

"""
simple convention
function name : Carmel
variable name : noun+ "_" noun
class name : start with capital
"""

import urllib
import numpy
from collections import defaultdict

def parseData(fname):
  for l in urllib.urlopen(fname):
    yield eval(l)

def readData(address):
    print "Reading data..."
    X = list(parseData(address))
    print "done"

    return X

def exploreUserData(user_data):
    elite_cnt = 0
    avg_cnt = 0.0
    avg_star = 0.0
    avg_friend = 0.0

    for user in user_data:
        if 'elite' in user and len(user['elite']) > 0:
            elite_cnt += 1
        if 'review_count' in user:
            avg_cnt += user['review_count']
        if 'average_stars' in user:
            avg_star += user['average_stars']
        if 'friends' in user:
            avg_friend += len(user['friends'])

    print "-----------------------user data-------------------------"
    print "The total number of users : " + str(len(user_data))
    print "The total number of elite : " + str(elite_cnt)
    print "The average of review count : " + str(avg_cnt/len(user_data))
    print "The average of star : " + str(avg_star/len(user_data))
    print "The average of friends : " + str(avg_friend/len(user_data))

def exploreReviewData(review_data):
    print "-----------------------review data-------------------------"
    avg_star = 0.0
    for review in review_data:
        if 'stars' in review:
            avg_star += review['stars']

    print "The total number of reviews : " + str(len(review_data))
    print "The average of stars : " + str(avg_star/len(review_data))

def exploreBusinessData(business_data):
    print "-----------------------business data-------------------------"

def exploreTipData(tip_data):
    print "-----------------------tip data-------------------------"

def exploreCheckinData(tip_data):
    print "-----------------------checkin data-------------------------"

if __name__ == '__main__':
    root_address = "../data/"
    business = "yelp_academic_dataset_business.json"
    checkin = "yelp_academic_dataset_checkin.json"
    user = "yelp_academic_dataset_user.json"
    review = "yelp_academic_dataset_review.json"
    tip = "yelp_academic_dataset_tip.json"

    #business_data = readData(root_address + business) # evel() error occur since JSON parsing failure
    user_data = readData(root_address + user)
    checkin_data = readData(root_address + checkin)
    review_data = readData(root_address + review)
    tip_data = readData(root_address + tip)

    exploreUserData(user_data)
    exploreUserData(checkin_data)
    exploreUserData(review_data)
    exploreUserData(tip_data)