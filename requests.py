headers = """
        PREFIX dct: <http://purl.org/dc/terms/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX lmdb: <https://triplydb.com/Triply/linkedmdb/vocab/>
        
    """

def getActors(movie):
    return """
        SELECT DISTINCT ?film_name ?actors_name
        WHERE {
            ?film rdfs:label \"""" + movie + """\".
            ?film rdfs:label ?film_name.
            ?film lmdb:actor ?actors.
            ?actors rdfs:label ?actors_name.
        }
    """
    
def getMoviesFromDate(date):
    return """
        SELECT DISTINCT ?film_name ?date
        WHERE {
            ?film rdf:type lmdb:Film.
            ?film rdfs:label ?film_name.
            ?film dct:date ?date.
            filter regex(?date, \"""" + date + """\").
        } LIMIT 30
    """