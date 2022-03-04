import os
import networkx as nx

from flask import Flask, render_template
from pyvis.network import Network

from sparql import SparQL

template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/date/<date>')
def date(date):
    reference = "film_name"
    research_word = date
    spql = SparQL(reference, research_word)
    spql.execute()
    
    G = nx.Graph()
    G.add_node(research_word)
    
    for item in spql.data[reference]:
        G.add_node(item.movie)
        G.add_edge(research_word, item.movie)
    
    nt = Network(bgcolor="#222222", font_color="white")
    nt.from_nx(G)
    nt.save_graph("./templates/network.html")
    return render_template('visualization.html')

@app.route('/movie/<movie>')
def visualization(movie):
    reference = "actors_name"
    research_word = movie
    spql = SparQL(reference, research_word)
    spql.execute()
    
    G = nx.Graph()
    G.add_node(research_word)
    
    for item in spql.data[reference]:
        G.add_node(item.name)
        G.add_edge(research_word, item.name)
        
    nt = Network(bgcolor="#222222", font_color="white")
    nt.from_nx(G)
    nt.save_graph("./templates/network.html")
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(debug=True)
