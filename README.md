# miniprojects
A few projects I finished in Summer 2015.

(1) <a href="https://github.com/kkamb/miniprojects/blob/master/NYC_Elite_Graph_Theory.ipynb">Using Graph Theory To Investigate the NYC Social Elite</a>

<a href="http://www.newyorksocialdiary.com/">The New York Social Diary</a> provides a fascinating lens onto New York's socially well-to-do. As shown in <a href="http://www.newyorksocialdiary.com/party-pictures/2014/holiday-dinners-and-doers
">this report of a recent holiday party</a>, almost all the photos have annotated captions labeling their subjects. We can think of this as implicitly implying a social graph: there is a connection between two individuals if they appear in a picture together.

In this project, I investigate these connections between the NYC elite. I determine who the most socially popular and influential people are, as well as pairs with the strongest connections. (The latter analysis picks up the obvious  -- marriages and family ties -- as well as connections not readily apparent, such as affairs and infidelities.)


(2) Using PostGreSQL To Investigate NYC Restaurants

The city of New York assigns a grade to restaurants after each inspection. I used PostGreSQL to parse and analyze four years worth of  NYC Restaurant Inspections data. I extracted different slices -- determining the grade distribution by zipcode, borough, and cuisine. I also found which cuisines tended to have a disproportionate number of which violations.

<center><img src="https://github.com/kkamb/miniprojects/blob/master/carto_map.png"></center><br>
A map view of scores by zipcode, where higher intensity reds are equivalent to higher scores, via <a href="http://cdb.io/1dkAG2o">cartodb</a>.

(3a) <a href="https://github.com/kkamb/miniprojects/blob/master/Yelp_ML.ipynb">Using Semi-Structured Data to Predict Yelp Ratings</a>

I attempted to predict a new venue's popularity from information available when the venue opens. The dataset contains meta data about each venue (city, latitude/longitude, category descriptions, etc), and a star rating. I used Python's Scikit libraries to train and test several different Machine Learning algorithms, yet still only managed to get a score of .2.

(3b) <a href="https://github.com/kkamb/miniprojects/blob/master/Yelp_NLP.ipynb">Using NLP to Predict Yelp Ratings</a>

I then explored how much information was contained in the review texts, whether they could more accurately predict ratings. Since I was working with over one million reviews and a design matrix of over a million feature-words, scalability was an overriding factor during model selection, especially since the model had to fit within Heroku's memory constraints. However, the predictive power of even a basic out-of-the-box ridge regression was magnitudes greater than that of the models in the previous section (yielding a score of over .6).


(4) <a href="https://github.com/kkamb/miniprojects/tree/master/Wikipedia_EMR">Analyzing Wikipedia via MapReduce</a>

I scraped the entire English Wikipedia to determine its <a href="https://github.com/kkamb/miniprojects/blob/master/Wikipedia_EMR/mrjob_top_100_words.py">most frequently used words</a>. I then collected <a href="https://github.com/kkamb/miniprojects/blob/master/Wikipedia_EMR/mrjob_linkstats.py">link statistics</a> (mean, standard deviations, percentiles) for the unique links on each page, and <a href="https://github.com/kkamb/miniprojects/blob/master/Wikipedia_EMR/mrjob_doublelinks.py">found the top linked concepts</a> by examining doublelinks.
