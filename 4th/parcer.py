#!/usr/bin/env python3
import urllib.request as urllib2
import urllib
from bs4 import BeautifulSoup
import queue
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
from igraph import Graph


def check_location(link1, link2):
    netloc_check = urllib.parse.urlparse(link1).netloc == urllib.parse.urlparse(link2).netloc
    scheme_check = urllib.parse.urlparse(link1).scheme == urllib.parse.urlparse(link2).scheme
    return scheme_check and netloc_check


def parse_node(graph, url):
    graph[url] = set()
    responce = urllib2.urlopen(url)

    soup = BeautifulSoup(responce, "lxml")
    for link in soup.find_all('a', href=True):
        goal_link = urllib.parse.urljoin(url, link.get('href'))
        if ():
            graph[url].add(goal_link)


def create_graph(url, depth=100, loggin=False):
    graph = dict()
    qu = queue.Queue()
    qu.put((url, 0))
    link, d = qu.get()
    while d < depth:
        if loggin:
            print("Parce %s" % link)
        if link in graph:
            continue
        parse_node(graph, link)
        for child in graph[link]:
            if child not in graph:
                qu.put((child, d+1))
        if qu.empty():
            break
        link, d = qu.get()
    return graph


def page_rank_algo(graph, damping_factor=0, eps=0.0001):
    page_rank = dict()
    num_urls = len(graph)
    for url in graph:
        page_rank[url] = 1. / num_urls
    diff = eps * 10
    while diff > eps:
        new_pr = dict()
        for url in graph:
            new_pr[url] = damping_factor / num_urls
        for url in graph:
            n_children = len(graph[url])
            if n_children > 0:
                for child in graph[url]:
                    new_pr[child] += (1 - damping_factor) * page_rank[
                        url] / n_children
            else:
                new_pr[url] += (1 - damping_factor) * page_rank[url]
        diff = 0
        for url in graph:
            diff += abs(new_pr[url] - page_rank[url])
        page_rank = new_pr.copy()
    return page_rank


def visualize(graph, root):
    vertexes = list(sorted([list(sorted(graph[v]))[i] for v in graph.keys()
                            for i in range(len(graph[v]))]))
    if root not in vertexes:
        vertexes.append(root)
    network = Graph(edges=[(vertexes.index(a), vertexes.index(v))
                           for v in graph.keys() for a in graph[v]])
    labels = vertexes
    num_of_vertexes = len(labels)
    edges = [e.tuple for e in network.es]
    layt = network.layout('kk')
    type(layt)

    plotly.tools.set_credentials_file(username='roller145', api_key='swY1NuePWATneUKADR4l')

    xn = [layt[k][0] for k in range(num_of_vertexes)]
    yn = [layt[k][1] for k in range(num_of_vertexes)]
    xe = []
    ye = []
    for e in edges:
        xe += [layt[e[0]][0], layt[e[1]][0], None]
        ye += [layt[e[0]][1], layt[e[1]][1], None]

    trace1 = Scatter(x=xe,
                     y=ye,
                     mode='lines',
                     line=Line(color='rgb(210,210,210)', width=1),
                     hoverinfo='none'
                     )
    trace2 = Scatter(x=xn,
                     y=yn,
                     mode='markers',
                     name='ntw',
                     marker=Marker(symbol='dot',
                                   size=5,
                                   color='#6959CD',
                                   line=Line(color='rgb(50,50,50)', width=0.5)
                                   ),
                     text=labels,
                     hoverinfo='text'
                     )

    axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                title=''
                )

    width = 800
    height = 800
    layout = Layout(title="Graph of connected with Math article on wiki",
                    font=Font(size=12),
                    showlegend=False,
                    autosize=False,
                    width=width,
                    height=height,
                    xaxis=XAxis(axis),
                    yaxis=YAxis(axis),
                    margin=Margin(
                        l=40,
                        r=40,
                        b=85,
                        t=100,
                    ),
                    hovermode='closest',
                    annotations=Annotations([
                        Annotation(
                            showarrow=False,
                            text='This igraph.Graph has the Kamada-Kawai layout',
                            xref='paper',
                            yref='paper',
                            x=0,
                            y=-0.1,
                            xanchor='left',
                            yanchor='bottom',
                            font=Font(
                                size=14
                            )
                        )
                    ]),
                    )

    data = Data([trace1, trace2])
    fig = Figure(data=data, layout=layout)

    return py.iplot(fig, filename='Graph')
