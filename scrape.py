import praw
import pandas as pd

def scrape(subName):
    
    # create reddit instance
    reddit = praw.Reddit(
        client_id="pB9MUejeyq28DAbqhPTPdw",
        client_secret="DjtWE0kvFBtO3jllv80JjcXbPs8MZg",
        user_agent="dulien",
    )

    # create dataframe
    data = {
        'TITLE': [],
        'TEXT': [],
        'REPLIES': [],
        'SCORE': [],
        'FLAIR': [],
        'URL': []
    }

    # create entries for MLMRecovery subreddit
    submissions = reddit.subreddit(subName).new(limit=None)

    # iterate through submissions and filter those containing "story"
    for submission in submissions:
        if "story" in submission.title.lower() or "story" in submission.selftext.lower() or submission.link_flair_text == "Story":
            print(submission.title)
            # add title, text, replies, score, flair, and url to dataframe
            data['TITLE'].append(submission.title)
            data['TEXT'].append(submission.selftext)
            data['REPLIES'].append(submission.num_comments)
            data['SCORE'].append(submission.score)
            data['FLAIR'].append(submission.link_flair_text)
            data['URL'].append(submission.url)
        else:
            print("Does not fit criteria")
        
    # convert data to csv file    
    df = pd.DataFrame(data)
    df.to_csv('{}.csv'.format(subName), index=False)


#Run the script once for each subreddit you want to scrape
scrape("MLMRecovery")
scrape("antiMLM")