import pandas as pd
import csv
def main():
	#Create a Dataframe to pull the tweets into
	column_names = [i for i in range(0, 300)]
	df=pd.read_csv("blacklivesmatter.csv",names=column_names)
	#Remove all duplicate tweets
	df=df.drop_duplicates()
	df=df.dropna(axis=1, how='all')
	#Put the data into a csv if that is convient
	df.to_csv('temp.csv',header=None,index=None)
	#Open the CSV, and write the data to a text file, which can be more convient.
	f=open("temp.csv","r")
	myfile=[]
	for line in f:
		temp=(line.strip())
		temp=temp.replace(",","")
		myfile.append([temp])
	f.close()
	f=open("blackLivesMatter.txt","w")
	
	for line in myfile:
		f.write(line[0]+"\n")
main()
