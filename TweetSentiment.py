#Nicholas Gardi   ASSIGNMENT #3
#Part A
#import happy histogram functions for part b
from happy_histogram import drawSimpleHistogram
#setting all the lists used below
keywordListWithValue = []
keywordList = []
keywordList1 = []
keywordList5 = []
keywordList10 = []
pacificTweetList = []
mountainTweetList = []
centralTweetList = []
easternTweetList = []
allTweetList = []
goodTweetList = []
import sys

#opening and reading the keywords.txt file
keywordsFile = input("Enter the name of the file that contains the keywords: ")
try:
    keywordsFile = open(keywordsFile, "r", encoding="utf-8")
    for line in keywordsFile:
        keywordListWithValue.append(line)
        keywordList.append(line.split(",")[0])

except FileNotFoundError:
    print("File not found error. Program quitting...")
    sys.exit(0)
#splitting the keywords up in to their lists
for x in keywordListWithValue:
    if x[-2] == "1":
        keyword = x.split(",")[0]
        keywordList1.append(keyword)
    if x[-2] == "5":
        keyword = x.split(",")[0]
        keywordList5.append(keyword)
    if x[-2] == "0":
        keyword = x.split(",")[0]
        keywordList10.append(keyword)


#opening and reading the tweets.txt file
tweetsFile = input("Enter the name of the file that contains the tweets: ")
try:
    tweetsFile = open(tweetsFile, "r", encoding="utf-8")
    for line in tweetsFile:
        tweets = line.split()
        allTweetList.append(tweets)
except FileNotFoundError:
    print("File not found error. Program quitting...")
    sys.exit(0)

#defining the function that filters out tweets with 0 keywords
def keywordTest(tweet):
    tweetText = tweet[5:]
    tweetTextString = " ".join(str(x) for x in tweetText)
    tweetTextString = tweetTextString.lower()                                                         #see comment
    tweetTextString = "".join([ x if x.isalpha() else " " for x in tweetTextString ])                 #  below
    tweetTextString = tweetTextString.split()
    setText = set(tweetTextString)
    setKeyword = set(keywordList)
    if (len(setText.intersection(setKeyword))) > 0:
        goodTweetList.append(tweet)




#defining the function that puts tweets with keywords into 4 lists corresponding to their timezone
def timezoneTest(tweet):
    tweetLat = float(((tweet)[0]).replace("[", "").replace(",", ""))
    tweetLong = float(((tweet)[1]).replace("]", ""))
    if tweetLat > 24.660845 and tweetLat < 49.189787:
        if tweetLong > -125.242264 and tweetLong < -115.236428:
            pacificTweetList.append(tweet)
        if tweetLong > -115.236428 and tweetLong < -101.008892:
            mountainTweetList.append(tweet)
        if tweetLong > -101.008892 and tweetLong < -87.518395:
            centralTweetList.append(tweet)
        if tweetLong > -87.518395 and tweetLong < -67.444574:
            easternTweetList.append(tweet)


#defining the function to add up the total sentiment value per timezone
def sentimentTest(timezone):
    sentiment = 0
    for tweet in timezone:
        tweetText = tweet[5:]
        tweetTextString = " ".join(str(x) for x in tweetText)
        tweetTextString = tweetTextString.lower()                                                   #see comment
        tweetTextString = "".join([ x if x.isalpha() else " " for x in tweetTextString ])           #   below
        tweetTextWords = tweetTextString.split()
        setText = set(tweetTextWords)
        set1 = set(keywordList1)
        set5 = set(keywordList5)
        set10 = set(keywordList10)
        if len(setText.intersection(set1)) > 0:
            sentiment = sentiment + (1 * (len(setText.intersection(set1))))
        if len(setText.intersection(set5)) > 0:
            sentiment = sentiment + (5 * (len(setText.intersection(set5))))
        if len(setText.intersection(set10)) > 0:
            sentiment = sentiment + (10 * (len(setText.intersection(set10))))
    return sentiment


#running keywordTest function for all tweets
for tweet in allTweetList:
    keywordTest(tweet)

#deleting duplicate tweets in the list
goodTweetListNoDuplicates = []
[goodTweetListNoDuplicates.append(item) for item in goodTweetList if item not in goodTweetListNoDuplicates]

#runnning timezoneTest function for all tweets that still remain after the keywordTest
for tweet in goodTweetListNoDuplicates:
    timezoneTest(tweet)


#running the sentimentTest function to get the total sentiment number for each timezone
mountainTotalSentiment = sentimentTest(mountainTweetList)
pacificTotalSentiment = sentimentTest(pacificTweetList)
easternTotalSentiment = sentimentTest(easternTweetList)
centralTotalSentiment = sentimentTest(centralTweetList)

#length of tweets in each list is the total amount of tweets with keywords from that timezone
numberOfMountainTweets = (len(mountainTweetList))
numberOfPacificTweets = (len(pacificTweetList))
numberOfCentralTweets = (len(centralTweetList))
numberOfEasternTweets = (len(easternTweetList))

#calculationg average sentiment per timezone
mval = ( mountainTotalSentiment / numberOfMountainTweets )
eval = ( easternTotalSentiment / numberOfEasternTweets )
cval = ( centralTotalSentiment / numberOfCentralTweets )
pval = ( pacificTotalSentiment / numberOfPacificTweets )

#printing the end results
print("")
print("Total number of mountain tweets: ", numberOfMountainTweets)
print("Mountain happiness score: ", mval)
print("")
print("Total number of pacific tweets: ", numberOfPacificTweets)
print("Pacific happiness score: ", pval)
print("")
print("Total number of eastern tweets: ", numberOfEasternTweets)
print("Eastern happiness score: ", eval)
print("")
print("Total number of central tweets: ", numberOfCentralTweets)
print("Central happiness score: ", cval)

#Part B
drawSimpleHistogram(eval,cval,mval,pval)



'''
#lines 58/59 and 90/91 strip everything that isnt a letter and make all the letters lowercase, there's so many different ways to do this assignment and not
stripping punctuation and leaving the letter case alone got my answers much closer to the ranges posted on owl. The assignment pdf said to strip and lower
while prof posts in the forum and in emails said otherwise. If we're not supposed to strip non-letters and leave the case alone then those 4 lines can be deleted
'''
