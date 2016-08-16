import csv
import urllib2

url='http://winterolympicsmedals.com/medals.csv'
response=urllib2.urlopen(url)
cr=csv.reader(response)
for rows in cr:
	print rows
