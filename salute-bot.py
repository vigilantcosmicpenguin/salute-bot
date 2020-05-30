import praw

#connects to the API
reddit = praw.Reddit(client_id = "UCjdr4Hd5GOjBw",
                     client_secret = "sYRrIaerHR_NnUSnOxgnOUh7ckU",
                     username = "salute-bot",
                     password = "Private Information!",
                     user_agent = "salute-bot (by u/vigilantcomicpenguin)")

#the subreddit the bot is on
subreddit = reddit.subreddit('himym')

#phrases that the bot reads
ranks = ["General", "Major", "Private", "Corporal", "Colonel", "Officer", "Lieutenant", "Captain", "Admiral", "Commander", "Kernel"]
for rank in ranks:
    ranks = ranks + rank.upper() + rank.lower()

#reads comments and replies
for comment in subreddit.stream.comments():
    commentWords = comment.body.split()
    for rank in ranks:
        if rank in commentWords:
            nextWord = commentWords[commentWords.index(rank) + 1]
            try:
                comment.reply("*salutes*\n\n" + rank + " " + nextWord)
                print(True)
            except:
                print(False)
