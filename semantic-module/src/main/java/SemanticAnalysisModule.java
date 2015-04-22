import java.util.ArrayList;
import java.util.List;

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

	public static void main(String[] args) throws RepositoryException {
		// TODO Auto-generated method stub
		System.out.println("test");
		
		List<String> linksWord1 = getResourceLinksForWord("man");
		List<String> linksWord2 = getResourceLinksForWord("woman");
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
				+ "} ";
		
		try {
			String queryString = query;

			TupleQuery tupleQuery = con.prepareTupleQuery(QueryLanguage.SPARQL, queryString);
			TupleQueryResult result = tupleQuery.evaluate();
			List<String> columnNames = result.getBindingNames();
			
			//insert code to create a new table in this new query for the given columns
			
			try {
				while (result.hasNext()) { // iterate over the result
					BindingSet bindingSet = result.next();
					for(String s : columnNames){
						Value val = bindingSet.getValue(s);
						System.out.println(" | " + val.stringValue() +" | ");	
						links.add(val.stringValue());
						//save this value in db table
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
