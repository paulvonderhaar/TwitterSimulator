import tweepy 
import csv
import pandas as pd
import demoji

def main(): 
		with open("tweets.csv","w",newline='') as csvfile:
			auth = tweepy.OAuthHandler('Enter Your Own')
			auth.set_access_token('Enter your Own')

			api=tweepy.API(auth)
			#####United Airlines
			# Open/Create a file to append data
			csvFile = open('blacklivesmatter.csv', 'a')
			#Use csv Writer
			csvWriter = csv.writer(csvFile)
			count=0

			for tweet in tweepy.Cursor(api.search,q="blacklivesmatter",count=100,
			                      ).items():
				#Monitor the tweets as they come in
				#print(tweet.text)
				#grab the tweet text, and start cleaning it
				cleanedText=tweet.text
				words=cleanedText.split()
				for i in range (len(words)):
					#Remove a couple of common but meaningless phrases

					if(words[i][0]=="@" or words[i][0:4]=="&amp" or  words[i][0:2]=="RT"):
						words[i]=""
					#Remove all emojiis and links
					demoji.replace(words[i])
					words[i]=(words[i].split('\\')[0])
					words[i]=(words[i].split("https")[0])
				CleanedTweet=''
				#Reconstruct the words
				for word in words:
					CleanedTweet=CleanedTweet+" "+word
				#Remove white space, quotes, and any other unknown ascii characters that were missed, and make all letters lower case
				CleanedTweet=(CleanedTweet.strip())
				CleanedTweet=CleanedTweet.strip('"')
				CleanedTweet=CleanedTweet.strip("'")
				CleanedTweet=CleanedTweet.encode('ascii',errors='ignore')
				CleanedTweet=CleanedTweet.decode('ascii')
				CleanedTweet=CleanedTweet.lower()
				print(CleanedTweet)
				#Put the Cleaned Tweet into a CSV, which can be grabbed by pands
				csvWriter.writerow((CleanedTweet))
main()
