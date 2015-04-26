from SPARQLWrapper import SPARQLWrapper, JSON
import sys, json, unicodedata, re

def checkExists(word):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	queryString = 'select DISTINCT ?a where { <'+word+'> ?a ?r }'
	sparql.setQuery(queryString)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	if len(results["results"]["bindings"]) > 0:
		return 1
	else:
		return 0
	 
def getWord4Matches(word3,predicateList):
	extractedResult = list()
	for predicate in predicateList:
		sparql = SPARQLWrapper("http://dbpedia.org/sparql")
		queryString = "PREFIX schema: <http://schema.org/> "
		queryString += "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "
		queryString += "PREFIX dbpedia-owl: <http://dbpedia.org/ontology/> "
		queryString += "SELECT DISTINCT ?x "
		queryString += "WHERE "
		queryString += "{ <"+word3+"> <"+predicate+"> ?x. "
		queryString += "} "

		sparql.setQuery(queryString)
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		
		for result in results["results"]["bindings"]:
			#s = result["x"]["value"]
			s = str(unicodedata.normalize('NFKD', result["x"]["value"]).encode('ascii','ignore'))
			if s.count('/')>0:
				s = s[s.rfind('/')+1:]
			s = s.replace('_',' ')
			s = ' '.join(s.split())
			if s.count(' ')<10 and not word3[word3.rfind('/')+1:].replace('_',' ') in s:
				#print word3[word3.rfind('/')+1:]
				#print s
				extractedResult.append(s)
	return extractedResult

def getPredicates(word1,word2):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	queryString = "PREFIX schema: <http://schema.org/> "
	queryString += "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "
	queryString += "PREFIX dbpedia-owl: <http://dbpedia.org/ontology/> "
	queryString += "SELECT DISTINCT ?x "
	queryString += "WHERE "
	queryString += "{ <"+word1+"> "
	queryString += "?x ?y. "
	queryString += '?y bif:contains "'+word2+'" . '
	queryString += "} "

	sparql.setQuery(queryString)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	
	extractedResult = list()
	for result in results["results"]["bindings"]:
		extractedResult.append(result["x"]["value"])
	return extractedResult


def getPriorityPredicates(word1,word2):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	queryString = "PREFIX schema: <http://schema.org/> "
	queryString += "PREFIX schema: <http://schema.org/> "
	queryString += "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "
	queryString += "PREFIX dbpedia-owl: <http://dbpedia.org/ontology/> "
	queryString += "SELECT DISTINCT ?x "
	queryString += "WHERE "
	queryString += "{ <"+word1+"> "
	queryString += "?x ?y. "
	queryString += 'FILTER (?y = "'+word2+'" or ?y = <http://dbpedia.org/resource/'+word2+'>)'
	queryString += "} ";

	sparql.setQuery(queryString)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	
	extractedResult = list()
	for result in results["results"]["bindings"]:
		extractedResult.append(result["x"]["value"])
	return extractedResult

def title_except_helpers(s):
	helpers = ['a', 'an', 'of', 'the', 'is']
	word_list = re.split(' ', s)
	final = [word_list[0].capitalize()]
	for word in word_list[1:]:
		s = word
		if word not in helpers:
			s = word.capitalize()
		final.append(s)
   	return " ".join(final)

def main():
	word1 = raw_input()
	word2 = raw_input()
	word3 = raw_input()

	word1 = ' '.join(word1.split())
	word2 = ' '.join(word2.split())
	word3 = ' '.join(word3.split())

	word1 = title_except_helpers(word1)
	word2 = title_except_helpers(word2)
	word3 = title_except_helpers(word3)

	word1 = word1.replace(' ','_')
	word2 = word2.replace(' ','_')
	word3 = word3.replace(' ','_')

	word1 = "http://dbpedia.org/resource/"+word1
	word3 = "http://dbpedia.org/resource/"+word3

	flag1 = checkExists(word1)
	flag3 = checkExists(word3)
	finalList = list()

	if(flag1 and flag3):
		pred = getPredicates(word1,word2)
		priorityPred = getPriorityPredicates(word1,word2)

		#print "----------------"
		priorityAns = getWord4Matches(word3,priorityPred)
		priorityAns = list(set(priorityAns))
		#print "----------------"
		otherAns = getWord4Matches(word3,pred)
		otherAns = list(set(otherAns))

		for s in priorityAns:
			if s in otherAns:
				otherAns.remove(s)

		# print "----------------"
		# print priorityAns
		# print otherAns

		
		finalList.extend(priorityAns)
		finalList.extend(otherAns)

	print finalList
        
if __name__ == "__main__":
    main()
 