# API-Practice
We are requesting data using an github api call.
We are using 'https://api.github.com/search/repositories?q=language:python&sort=stars'
This call return the pythons currently hosted on github.
https://api.github.com/ - Direct the request to the part of Github's website that respond to Api call
search/repositories - Tell the API to conduct a search through all repositories on Github
?q=language:python&sort=stars - question mark sign indicate we're about to pass an argument. "q" stand for query and "=" let's us begin specifying a query

When we resquest we get a json response which is basically a dictionary. 

We are using REQUEST, PYGAL libraries.

Later we make an instance of pygal.Config() class. And in that we specify all the configuration for the graph.

We have created several graph using the data we received from the API.




