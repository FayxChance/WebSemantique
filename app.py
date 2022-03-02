from flask import Flask, render_template
from pyvis.network import Network
import networkx as nx
import os

template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualization')
def visualization():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (5, 7), (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (8, 9), (8, 10), (9, 10)])
    nt = Network(height="50vh", width="50vw", bgcolor="#222222", font_color="white", heading="Network")
    nt.from_nx(G)
    nt.save_graph("./templates/network.html")
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(debug=True)
