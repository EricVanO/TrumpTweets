# TrumpTweets
Which Tweets are Trump's?

Many who follow politics have noticed that the tweets from [@RealDonaldTrump](https://www.twitter.com/RealDonaldTrump) don't seem to be written by just one person. 
Some of them—often written early in the morning—use language that is unique to Donald Trump: 
insults to political opponents, attacks on the media, etc. Others—usually sent during normal working hours—
include language that any President would use: stating policy positions, endorsing other Republicans, etc.

The Jupyter notebook `TrumpTweets.ipynb` is my attempt to distinguish between Tweets worded in a Trumpy way and those worded Presidentially.

## Files
 - `TrumpTweets.json`: Contains information from all tweets from [@RealDonaldTrump](https://www.twitter.com/RealDonaldTrump) sent between Inauguration Day, 2017 to October 11, 2018. Created using the [Trump Twitter Archive](http://www.trumptwitterarchive.com).
 - `preprocessing.py`: Contains helper functions to prepare strings to be used in natural language processing
 - `TrumpTweets.ipynb`: Uses the other two files to analyze Trump's Tweets and see if Trumpy tweets are distinguishable from more presidential tweets.

## Requirements
In order to run `TrumpTweets.ipynb`, you will need:
 - Python 3.6.2
 - iPython 6.1.0
 - Pandas 0.20.3
 - Altair 2.2.2
 - Vega 1.4.0
 - Scikit-learn 0.19.0
 - NLTK 3.2.4
 - Beautiful Soup 4.6.0
