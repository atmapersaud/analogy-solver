import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.openrdf.model.Value;
import org.openrdf.query.BindingSet;
import org.openrdf.query.QueryLanguage;
import org.openrdf.query.TupleQuery;
import org.openrdf.query.TupleQueryResult;
import org.openrdf.repository.Repository;
import org.openrdf.repository.RepositoryConnection;
import org.openrdf.repository.RepositoryException;
import org.openrdf.repository.sparql.SPARQLRepository;


public class SemanticAnalysisModule {

	public static void main(String[] args) throws RepositoryException, FileNotFoundException {
		// TODO Auto-generated method stub
		System.out.println("test");
//		String word1 = "Los_Angeles", word2 = "university_of_southern_california";
//		List<String> linksWord1 = getResourceLinksForWord(word1);
//		List<String> linksWord2 = getResourceLinksForWord(word2);
//		Set<String> word1ToWord2 = new HashSet<String>();
//		Set<String> word2ToWord1 = new HashSet<String>();
//		int count = 1;
//		
//		linksWord1.add("http://dbpedia.org/resource/"+word1);
//		linksWord2.add("http://dbpedia.org/resource/"+word2);
//		
//		for(String s : linksWord1){
//			for(String s2 : linksWord2){
//				word1ToWord2.addAll(directRelations(s,s2));
//				word2ToWord1.addAll(directRelations(s2,s));
//				System.out.println(count++);
//			}
//		}
//		PrintWriter out = new PrintWriter("temp.txt");
//		out.println(word1+" - "+word2);
//		for(String s : word1ToWord2)
//			out.println(s);
//		out.println("--------------------------");
//		out.println(word2+" - "+word1);
//		for(String s : word2ToWord1)
//			out.println(s);
//		out.close();
		
		String word1 = "Bill_Gates";
		List<String> linksWord1 = getResourceLinksForWord(word1);
		Boolean flag = checkExists("http://dbpedia.org/resource/"+word1);
		System.out.println(flag);
 	}
	
public static Boolean checkExists(String word) throws RepositoryException{
		
		//endpointUrl should be initially asked from the user and saved as a global parameter or user-settings-parameter
		String endpointUrl = "http://dbpedia.org/sparql"; 
		Repository repo = new SPARQLRepository(endpointUrl);
		repo.initialize();
		RepositoryConnection con = repo.getConnection();
		
		String query = "select DISTINCT ?a where "
			+ "{ <"+word+"> ?a ?r }";
		
		try {
			String queryString = query;

			TupleQuery tupleQuery = con.prepareTupleQuery(QueryLanguage.SPARQL, queryString);
			TupleQueryResult result = tupleQuery.evaluate();
			
			try {
				if(result.equals(null))
					return false;
				else return true;
//				while (result.hasNext()) { // iterate over the result
//					BindingSet bindingSet = result.next();
//					if(bindingSet.size()>0)
//						return true;
//					else return false;
//				}
			} catch (Exception e) {
				e.printStackTrace();
				return false;
			} finally {
				result.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		} finally {
			con.close();
		}
	}
	
public static List<String> directRelations(String url1, String url2) throws RepositoryException{

	//endpointUrl should be initially asked from the user and saved as a global parameter or user-settings-parameter
	String endpointUrl = "http://dbpedia.org/sparql"; 
	Repository repo = new SPARQLRepository(endpointUrl);
	repo.initialize();
	RepositoryConnection con = repo.getConnection();
	List<String> relations = new ArrayList<String>();
	
	String query = "PREFIX schema: <http://schema.org/> "
		+ "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "
		+ "PREFIX dbpedia-owl: <http://dbpedia.org/ontology/> "
		+ "SELECT ?x"
		+ "WHERE "
		+ "{ <"+url1+"> "
		+ "?x <"+url2+">. "
		+ "} ";
	

		
	try {
		String queryString = query;

		TupleQuery tupleQuery = con.prepareTupleQuery(QueryLanguage.SPARQL, queryString);
		TupleQueryResult result = tupleQuery.evaluate();
		List<String> columnNames = result.getBindingNames();
		
		try {
			while (result.hasNext()) { // iterate over the result
				BindingSet bindingSet = result.next();
				for(String s : columnNames){
					Value val = bindingSet.getValue(s);
					System.out.println(" | " + val.stringValue() +" | ");	
					relations.add(val.stringValue());
				}
			}
			return relations;
		} finally {
			result.close();
		}
	} catch (Exception e) {
		e.printStackTrace();
		return relations;
	} finally {
		con.close();
	}
}
	
public static List<String> getResourceLinksForWord(String word) throws RepositoryException{
		
		//endpointUrl should be initially asked from the user and saved as a global parameter or user-settings-parameter
		String endpointUrl = "http://dbpedia.org/sparql"; 
		Repository repo = new SPARQLRepository(endpointUrl);
		repo.initialize();
		RepositoryConnection con = repo.getConnection();
		List<String> links = new ArrayList<String>();
		
		String query = "SELECT DISTINCT ?s WHERE { "
	        	+ "?s rdfs:label ?label . "
	        	+ "FILTER (lang(?label) = 'en'). "
	        	+ "?label bif:contains \""+word+"\" . "
	        	+ "?s dcterms:subject ?sub"
				+ "}";
		
		try {
			String queryString = query;

			TupleQuery tupleQuery = con.prepareTupleQuery(QueryLanguage.SPARQL, queryString);
			TupleQueryResult result = tupleQuery.evaluate();
			List<String> columnNames = result.getBindingNames();
			
			try {
				while (result.hasNext()) { // iterate over the result
					BindingSet bindingSet = result.next();
					for(String s : columnNames){
						Value val = bindingSet.getValue(s);
						System.out.println(" | " + val.stringValue() +" | ");	
						links.add(val.stringValue());
					}
				}
				return links;
			} finally {
				result.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
			return links;
		} finally {
			con.close();
		}
	}

}
