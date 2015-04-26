from SPARQLWrapper import SPARQLWrapper, JSON
import sys, json

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
		
		extractedResult = list()
		for result in results["results"]["bindings"]:
		    extractedResult.append(result["x"]["value"])
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

def main():
	word1 = raw_input()
	word2 = raw_input()
	#word3 = raw_input()
	word1 = word1.replace(' ','_')
	word2 = word2.replace(' ','_')
	#word3 = word3.replace(' ','_')
	word1 = "http://dbpedia.org/resource/"+word1

	flag1 = checkExists(word1)
	# flag3 = checkExists("http://dbpedia.org/resource/"+word3)

	if(flag1):
		p1 = getPredicates(word1,word2)
		p2 = getPriorityPredicates(word1,word2)
		print(getWord4Matches(word1,p1))
        
if __name__ == "__main__":
    main()
 