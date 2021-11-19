import praw
import pandas as pd

# Change the following dictionary to add/remove whatever information you want to scrape
# Append the information to the correct column of the dictionary 
# e.g. data['title'].append("My subreddit title")

# Enter the subreddit title that you are scraping
subreddit = "subreddit"

data = {
    'title': [],
    'replies': [],
    'upvotes': [],
    'downvotes': [],
    'flair': []
}

# Your code HERE!!!


df = pd.DataFrame(data)
df.to_csv(subreddit + '.csv')

#Run the script once for each subreddit you want to scrape
