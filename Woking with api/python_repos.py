from base64 import encode
from urllib import response
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as Ls



url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url) # get request
print("status code:", r.status_code)
response_dict = r.json()
print(response_dict.keys())

print('total repositeries', response_dict['total_count'])
repo_dic = response_dict['items']
print('repositeries returned:', len(repo_dic))
# examine the first reporsitory

names, stars, plot_dicts = [], [], []

for repo_dict in repo_dic:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        #adding clickeable links
        'xlink':repo_dict['html_url'],

    }
    plot_dicts.append(plot_dict)

    # print('Repository:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at'])
    # print('Updated:', repo_dict['updated_at'])
    # print('Description:', repo_dict['description'])
    # print('Owner:', repo_dict['owner']['login'])


my_style = Ls('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-starred Python Projects on Github'
chart.x_labels = names
#chart.add('', stars) python_repos, python_repos_1
chart.add('', plot_dicts)

chart.render_to_file('Woking with api/python_repos_3.svg')
