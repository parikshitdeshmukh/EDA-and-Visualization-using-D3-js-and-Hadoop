# Big Data processing of Articles and tweets and visualizing in word cloud

This project is a part of Data Intensive Comuting course at University of Buffalo.

#Data Collection:
Used NYTimes API to gather the articles URLs and Beautiful Soup Python library to scrape the articles and relevant data from the URLs.
Used TweetR cran package of R to extract the tweets for 1 day and 1 week and merged into a big text file for feeding it to Map Reducer jobs.

Data has been collected for 1 day and 1 week for below topics:
        "SpaceX", "Tesla", "Elon Musk"

#MapReduce:

There are 2 main types of Mappers and Reducers implemneted in Python according to requirements.
1) Basic processing: Using Map Reduce to count and sort the relevant words from the scraped data according to their occurances in Artciles and Tweets separately.
Eg:

Tesla, 200
Musk, 180
Spacex, 150

2) Co-occurring words: Using Map Reduce to count and sort the two words phrases from the data and sorting by their occurances as in whlole.
Eg:
Falcon Heavy, 150
Elon Musk, 146


#Word Cloud Visualization:

Used D3 js to create a word cloud accordnign to the words and their weightage pf occurrance in the processed data or articles.


































