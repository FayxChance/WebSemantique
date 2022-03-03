import json
import ssl

from SPARQLWrapper import SPARQLWrapper, JSON
from classes import Actor, Date
import requests

class SparQL():
    def __init__(self, call_reference, research_word) -> None:
        self.call_reference = call_reference
        self.research_word = research_word
        self.data = {"actors_name": [], "film_name": []}
        self.switch = {"actors_name" : lambda movie: requests.getActors(movie), "film_name": lambda date: requests.getMoviesFromDate(date)}

    def sparql_call(self, reference):
        sparql = SPARQLWrapper("https://api.triplydb.com/datasets/Triply/linkedmdb/services/linkedmdb/sparql")
        
        request = requests.headers
        
        request += self.switch[reference](self.research_word)

        sparql.setQuery(request)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    def getDataFromJson(self, dict, reference):
        lambdaSwitch = {
            "actors_name": lambda: self.data[reference].append(Actor(result[reference]["value"], [])),
            "film_name": lambda: self.data[reference].append(Date(result[reference]["value"], result["film_name"]["value"]))
        }
        for result in dict["results"]["bindings"]:
            lambdaSwitch[reference]()
            
    def prettyPrintDictAsJson(self, dict):
        print(json.dumps(dict, indent=4, sort_keys=True))

    def execute(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        
        dict = self.sparql_call(self.call_reference)
        print(len(self.data[self.call_reference]))
        
        self.getDataFromJson(dict, self.call_reference)