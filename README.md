# miniprojects
A few of the projects I finished in Summer 2015.

(1) <a href="https://github.com/kkamb/miniprojects/blob/master/NYC_Elite_Graph_Theory.ipynb">Using Graph Theory To Investigate the NYC Social Elite</a>

<a href="http://www.newyorksocialdiary.com/">The New York Social Diary</a> provides a fascinating lens onto New York's socially well-to-do. The data forms a natural social graph for New York's social elite. As shown in <a href="http://www.newyorksocialdiary.com/party-pictures/2014/holiday-dinners-and-doers
">this report of a recent holiday party</a>, almost all the photos have carefully annotated captions labeling their subjects. We can think of this as implicitly implying a social graph: there is a connection between two individuals if they appear in a picture together.

In this project, I investigate these connections between the NYC elite. I determine who the most socially popular and influential people are, as well as the pairs that have the strongest connections. (The latter analysis picks up the obvious  -- marriages and family ties -- as well as connections that are not readily apparent, such as affairs and infidelities.)


(2) Using PostGreSQL To Investigate NYC Restaurants

The city of New York assigns a grade to restaurants after each inspection. Here, I used PostGreSQL to analyze four years worth of raw NYC Restaurant Inspections data. I extracted different slices -- determining the grade distribution by zipcode, borough, and cuisine. I also found which cuisines tended to have a disproportionate number of what which violations.


(3a) <a href="https://github.com/kkamb/miniprojects/blob/master/Yelp_ML.ipynb">Using Semi-Structured Data to Predict Yelp Ratings</a>

(3b) <a href="https://github.com/kkamb/miniprojects/blob/master/Yelp_NLP.ipynb">Using Unstructured Data to Predict Yelp Ratings</a>


(4) Analyzing Wikipedia via MapReduce

I parsed the html and determined what the most frequent words were for the entire English Wikipedia. I then collected link statistics (mean, standard deviations, percentiles, for the unique links on each Wikipedia page). Then I found what the top linked concepts were on Wikipedia via doublelinks.
