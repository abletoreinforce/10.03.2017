import matplotlib.pyplot as plt
import networkx as nx
import requests

HOST = 'https://api.vk.com/method/'
VERSION = '5.62'

font = {'family': 'Verdana',
        'weight': 'normal'}

r = requests.get(HOST + 'friends.get', timeout = 100, params={'user_id': 264251957, 'fields': 'first_name', 'v': VERSION})

G = nx.Graph()

for person in r.json()['response']['items']:
    G.add_node(person['last_name'] + ' ' + person['first_name'])
    r2 = requests.get(HOST + 'friends.get', timeout = 100, params={'user_id': person['id'], 'fields':'first_name','v': VERSION})
    for friend_of_friend in r2.json()['response']['items']:
        if friend_of_friend in r.json()['response']['items']:
            G.add_edge(friend_of_friend['last_name'] + ' ' + friend_of_friend['first_name'], person['last_name'] + ' ' + person['first_name'])


nx.draw_networkx(G, edge_color='r', node_color='b', node_size = 20, alpha = 0.5, font_family = 'Verdana', font_size = 8)
plt.axis('off')
plt.show()

