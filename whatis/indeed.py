#!/usr/bin/env python

#import sys
#from os.path import isfile
import sqlite3
import csv

'''
def getDistinctJobTitles(xmlRoot):
    jobTitles = []
    return jobTitles
        
def getNumDuplicates(xmlRoot):
    jobkeys = []
    # root is <xmlRoot>
    for child in xmlRoot:
        # child is <result>
        totalCount = totalCount + 1        
'''
 
if __name__ == "__main__":
    keywords = ['big data', 'data mining', 'machine learning', 'classification', 'neural net', 'deep learning', 'computer science', 'statistic', 'predict', 'hadoop', 'python', 'SAS', 'SPSS', 'quantitative', 'analysis']
    counts = []
    conn = sqlite3.connect('indeed_datascientist.db')
    c = conn.cursor()
    
    for keyword in keywords:
        c.execute("SELECT count(1) FROM indeed_datascientist WHERE snippet like :keyword", {"keyword": '%'+keyword+'%'})
        counts.append(c.fetchone()[0])
        
    with open('keywordCounts.csv', 'wb') as keywordCountsFile:
        writer = csv.writer(keywordCountsFile, delimiter=',')
        writer.writerow(['keyword', 'count'])
        for row in zip(keywords, counts):
            writer.writerow(row)
    
    
    