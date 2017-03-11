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
    print(person['id'])
    r2 = requests.get(HOST + 'friends.get', timeout = 100, params={'user_id': person['id'], 'fields':'first_name','v': VERSION})
    for i in range(len(r2.json()['response']['items'])):
        if r2.json()['response']['items'][i] in r.json()['response']['items']:
            G.add_edge(r2.json()['response']['items'][i]['last_name'] + ' ' + r2.json()['response']['items'][i]['first_name'], person['last_name'] + ' ' + person['first_name'])


nx.draw_networkx(G, width = 3.0, node_size = 10, alpha = 0.5, font_family = 'Verdana', font_size = 8)
plt.axis('off')
plt.show()

