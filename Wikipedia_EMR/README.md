Analyzing Wikipedia via MapReduce

(1) <a href="https://github.com/kkamb/miniprojects/blob/master/Wikipedia_EMR/mrjob_top_100_words.py">The most frequently used words in the entire English Wikipedia</a>

I scraped and parsed the text from each Wikipedia page (eliminating xml tags, hyperlink urls, etc). To obtain the most frequent n words, I obtained the largest n elements per chunk from each mapper, output them to the same key (reducer), and collected the largest n elements from the reducer. I used <a href="https://docs.python.org/2/library/heapq.html">heapq</a>, Python's <a href="http://en.wikipedia.org/wiki/Heap_(data_structure)">heap</a> <a href="http://en.wikipedia.org/wiki/Priority_queue">priority queue</a> structure, for this step. Since I was using a priority queue, I had to first initialize it, add for each record, and output top n after seeing each record (corresponding to 'mapper_init', 'mapper', and 'mapper_final').


(2) Entropy calculations for the English Wikipedia and the Thai Wikipedia

The <a href="https://en.wikipedia.org/wiki/Entropy_(information_theory)">Shannon Entropy</a> is the number of bits needed to store things if we had perfect compression. There are also <a href="http://www.johndcook.com/blog/2013/08/17/calculating-entropy/">methods of calculating this more efficiently</a>.

In this part, I calculated the Shannon entropy of English and Thai based off their Wikipedias. I needed to use mapreduce because there were over 320 million characters in this dataset. I first calculated the entropy of a single n-gram, and then divided by n to get the per-character entropy, using n-grams of size 1, 2, 3, 4, 5, 10 and 15. 


(3) <a href="https://github.com/kkamb/miniprojects/blob/master/Wikipedia_EMR/mrjob_linkstats.py">Link statistics for the English Wikipedia</a>

Here I gathered summary statistics on the number of unique links on a Wikipedia article to other Wikipedia articles. The EMR job returns the total number of English Wikipedia articles (~15 million at this time of calculation), average number of links per article (18), standard deviation, and various quantiles. I calculated the first three by looking at the first few moments of the distribution; and the quantiles via reservoir sampling.


(4) <a href="https://github.com/kkamb/miniprojects/blob/master/Wikipedia_EMR/mrjob_doublelinks.py">Top linked concepts in the English Wikipedia</a>

Finally, I looked at double links (pages A and C that are connected through many pages B where there is a link 'A -> B -> C' or 'C -> B -> A'). I found the 100 most tightly related concepts (the pairs (A,C) that had the most connections). Some notes:

  1. This is essentially a Matrix Multiplication problem.  If the adjacency
  matrix is denoted <i>M</i> (where <i>M_(ij)</i> represents the link between <i>i</i> an
  <i>j</i>), we are looking for the highest 100 elements of the matrix <i>M*M</i>.

  2. A lot of Category pages (denoted "Category:.*") have a high
  link count and rank very highly according to this metric.  Wikipedia
  also has `Talk:` pages, `Help:` pages, static resource `Files:`, etc. I had to filter out all 
  such non-content pages for this analysis.

  3. Some pages have more links than others.  If I'd just counted the number of
  double links between pages, I'd have ended up gathering links that appear on articles with
  many links, rather than concepts that are tightly connected. 

  One strategy is to weight each link as <i>1/n</i> where <i>n</i> is the
  number links on the page.  This way, an article has to spread its
  "influence" over all <i>n</i> of its links.  However, this can throw off the
  results for small <i>n</i>. To control for pages with few links, I added a somewhat arbitrary constant <i>10</i>, and weighted each link as <i>1/(n+10)</i>. My final "count" for 
  a pair (A,C) was the product of their two link weights, 
  summed over all their shared connections.

