import requests, time
import pandas as pd

import matplotlib.pyplot as plt
import random

# this function counts the amount of repositories for each different language in github url

def search_github(keyword):
    url = "https://api.github.com/search/repositories?q={}".format(keyword)
    data = requests.get(url).json()
    repos_count = data['total_count']
    return repos_count

# after returning the count above we retive the results and print them, results are described as keywords
def retrieve_repositories_results(keywords):
    repos_results = {}
    
    # loop through each keyword and classify count of repositories to each language as keyword. 
    for keyword in keywords:
        repos_count = search_github(keyword)
        print("{} repositories results found: {}".format(keyword, repos_count))
        repos_results[keyword] = repos_count
        time.sleep(3)

    # return dicts
    return repos_results

# Now let us add Pandas module that retrieve the results after keywords to print out the data as a table.

# function that prints Pandas dataframe

def print_repos_results(repos_results):
    df = pd.DataFrame(repos_results, index=['Repository results'])
    print(df)

# And finnally lets use matplotlib to get chart from our code

# A function that generate the colour of each bar in the graph

def generate_random_colors(number_of_colors):
    colors = []

    for x in range(number_of_colors):
        rgb = (random.random(), random.random(), random.random())
        colors.append(rgb)

    return colors

# a function to generate the graph
def print_graph(repos_results, graph_type, title):
    keywords = repos_results.keys()
    results = repos_results.values()

    plt.figure(figsize=(9, 3))
    colors = generate_random_colors(len(keywords)) 

    if graph_type == "bar":
        plt.bar(keywords, results, color=colors)
    else:
        plt.scatter(keywords, results, color=colors)
    
    plt.suptitle(title)
    plt.show()
# example usage
languages = ['Python', 'Java', 'Ruby', 'Javascript', 'PHP', 'Objective-C', 'Golang', 'Bash', 'Rust', 'Powershell']
languages_results = retrieve_repositories_results(languages)
# Pandas table frame
print_repos_results(languages_results)
# matplotlib dataframe table generator
print_graph(languages_results, "bar", "programming languages")





