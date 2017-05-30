#!/usr/bin/env python3
import urllib.request as urllib2
import urllib
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import queue
import numpy as np
import matplotlib.pyplot as plt
import networkx


def check_location(link1, link2):
    netloc_check = urllib.parse.urlparse(link1).netloc == urllib.parse.urlparse(link2).netloc
    scheme_check = urllib.parse.urlparse(link1).scheme == urllib.parse.urlparse(link2).scheme
    return scheme_check and netloc_check


def parse_node(graph, url, vertexes, links):
    graph[url] = set()
    try:
        response = urllib2.urlopen(url)
    except HTTPError as err:
        print("Error of HTTP parsing %s : %s" % (url, err))
        return graph

    soup = BeautifulSoup(response, "lxml")
    for link in soup.find_all('a', href=True):
        goal_link = urllib.parse.urljoin(url, link.get('href'))
        if check_location(url, goal_link):
            graph[url].add(goal_link)
            links.append((url, goal_link))
            vertexes.add(goal_link)
    return graph


def create_graph(url, depth=100, loggin=False):
    graph = dict()
    vertexes = set()
    links = []
    parsing_queue = queue.Queue()
    parsing_queue.put((url, 0))
    link, depth = parsing_queue.get()
    while depth < depth:
        if loggin:
            print("Parse %s" % link)
        if link in graph:
            link, depth = parsing_queue.get()
            continue
        parse_node(graph, link, vertexes, links)
        for child in graph[link]:
            if child not in graph:
                parsing_queue.put((child, depth + 1))
        if parsing_queue.empty():
            break
        link, depth = parsing_queue.get()
    return graph, vertexes, links


def page_rank_algorithm(web_graph, damping_factor=0.1, eps=0.0001):
    page_rank = dict()
    num_urls = len(web_graph)
    for url in web_graph:
        page_rank[url] = 1. / num_urls
    diff = eps * 10
    while diff > eps:
        new_pr = dict()
        for url in web_graph:
            new_pr[url] = damping_factor / num_urls
        for url in web_graph:
            n_children = len(web_graph[url])
            if n_children > 0:
                for child in web_graph[url]:
                    if child not in new_pr.keys():
                        new_pr[child] = 0
                    new_pr[child] += (1 - damping_factor) * page_rank[url] / n_children
            else:
                new_pr[url] += (1 - damping_factor) * page_rank[url]
        diff = 0
        for url in web_graph:
            diff += abs(new_pr[url] - page_rank[url])
        page_rank = new_pr.copy()
    return page_rank


def plot(vertexes, links, pagerank):
    vertexes = list(vertexes)
    vertex_index = np.arange(0, len(vertexes))
    link_indexes = []

    for from_url, to_url in links:
        link_indexes.append((vertexes.index(from_url), vertexes.index(to_url)))

    Graph = networkx.DiGraph()
    Graph.add_nodes_from(vertex_index)
    Graph.add_edges_from(link_indexes)

    size_const = int(2 * 10 ** 3 / np.mean(list(pagerank.values())))

    plt.figure(figsize=(15, 7))
    plt.axis('off')

    weigths = [size_const * pagerank[vertex] for vertex in vertexes]
    networkx.draw_networkx(Graph, width=0.5, node_size=weigths,
                           node_color=weigths)
    plt.show()

    for i in range(len(vertexes)):
        print("%d: %s" % (i, vertexes[i]))
