#!/usr/bin/python
import csv
import sys
import couchdb
import json

def get_first(iterable, default=None):
    if iterable:
	print iterable['c_id']
        return iterable['c_id']
    return default
	
def csv2Couch(csvfile,dbname,delim=',',qcr='"'):
	csvcont = csv.DictReader(open(csvfile, 'r'), delimiter = delim, quotechar = qcr)
	datas = [cont for cont in csvcont]
	server = couchdb.Server(url='https://aiyarankith.cloudbees.cloudant.com', full_commit=True, session=None)
	server.resource.credentials = ("aiyarankith.cloudbees", "bs5854fh4I3nnGYJQ5e58FML")
	#couchdb runs on https cloud server
	db = server[dbname]
	#assumes that db is already created

	for data in datas:
		document = data
		print document
		db[str(get_first(document))] = document
		#to assign a unique id for each document

if __name__ == '__main__':
	fname = sys.argv[1]
	dbname = sys.argv[2]
	csv2Couch(fname,dbname)
