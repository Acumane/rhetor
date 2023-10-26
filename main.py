import praw
from credentials import ID, SECRET
from praw.models import MoreComments as more

reddit = praw.Reddit(
    client_id=ID,
    client_secret=SECRET,
    user_agent="The Rhetor Project"
)

# Get this week's top 5 posts
cmv = reddit.subreddit("changemyview").top(time_filter="week", limit=5)
top = [post for post in cmv if not post.stickied]
print("Choose a post #: ")
for i, post in enumerate(top):
    print(f"{i+1}. {post.title[5:]}")

choice = int(input("\n"))-1
topic = top[choice].title[5:]
desc = top[choice].selftext

# https://praw.readthedocs.io/en/latest/tutorials/comments.html
comments = top[choice].comments

print(topic)
# print(desc)

# Ex. explore first comment and its immediate replies
for c in comments:
    # Skip "load more" objects and stickied
    if isinstance(c, more) or c.stickied: continue
    print(f"\nAuthor: {c.author}")
    print(f"\tMinds changed: {c.author_flair_text[:-1] if c.author_flair_text else '0'}")
    print(c.body)
    if c.score_hidden: print ("Score hidden")
    else: print(f"Score: {c.score}")

    for r in c.replies:
        if isinstance(r, more): continue
        print(f"\n\tAuthor: {r.author}")
        print(f"\tMinds changed: {r.author_flair_text[:-1] if r.author_flair_text else '0'}")
        print("\t",r.body)
        if r.score_hidden: print ("\tScore hidden")
        else: print(f"\tScore: {r.score}")
    break
