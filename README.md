# miniprojects
A few of the projects I finished in Summer 2015.

(1) <a href="https://github.com/kkamb/miniprojects/blob/master/NYC_Elite_Graph_Theory.ipynb">Using Graph Theory To Investigate the NYC Social Elite</a>

<a href="http://www.newyorksocialdiary.com/">The New York Social Diary</a> provides a fascinating lens onto New York's socially well-to-do. The data forms a natural social graph for New York's social elite. As shown in <a href="http://www.newyorksocialdiary.com/party-pictures/2014/holiday-dinners-and-doers
">this report of a recent holiday party</a>, almost all the photos have carefully annotated captions labeling their subjects. We can think of this as implicitly implying a social graph: there is a connection between two individuals if they appear in a picture together.

In this project, I investigate these connections between the NYC elite. I determine who the most socially popular and influential people are, as well as the pairs that have the strongest connections. (The latter analysis picks up the obvious  -- marriages and family ties -- as well as connections not readily apparent, such as affairs and infidelities.)


(2) Using PostGreSQL To Investigate NYC Restaurants

The city of New York assigns a grade to restaurants after each inspection. Here, I used PostGreSQL to analyze four years worth of raw NYC Restaurant Inspections data. I extracted different slices -- determining the grade distribution by zipcode, borough, and cuisine. I also found which cuisines tended to have a disproportionate number of which violations.


(3a) <a href="https://github.com/kkamb/miniprojects/blob/master/Yelp_ML.ipynb">Using Semi-Structured Data to Predict Yelp Ratings</a>

I attempted to predict a new venue's popularity from information available when the venue opens. The dataset contains meta data about the venue (city, latitude/longitude, category descriptions, etc), and a star rating. I used Python's Scikit libraries to train and test several different Machine Learning algorithms, yet still only managed to get a score of .2.

(3b) <a href="https://github.com/kkamb/miniprojects/blob/master/Yelp_NLP.ipynb">Using NLP to Predict Yelp Ratings</a>

I then explored how much information was contained in the review texts, whether they could more accurately predict ratings. Since I was working with over one million reviews and a design matrix of over a million feature-words, scalability was an overriding factor when chosing which algorithms to use, especially since the models had to fit within Heroku's memory constraints. However, the predictive power of this very simple model was magnitudes greater than that of the models in the previous section (yielding a score of over .6).


(4) Analyzing Wikipedia via MapReduce

I scraped the entire English Wikipedia to determine its most frequently used words. I then collected link statistics (mean, standard deviations, percentiles, etc) for the unique links on each page, and found what the top linked concepts were via doublelinks.
