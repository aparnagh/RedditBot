import praw
import operator
import nltk

nltk.download("stopwords")
nltk.download('punkt')
nltk.download("words")

reddit = praw.Reddit('bot1')
stop_word_list = """.,--,\'s,?,),(,:,\',\'re,",-,},{,!,...,\'\',\'ve,n\'t,%,``,#,],[,&,;,\'m,=,\'ll""".split(',')
all_stop_words = nltk.corpus.stopwords.words('english') + stop_word_list
all_stop_words.append(",")

subreddit = reddit.subreddit("learnprogramming")

for submission in subreddit.hot(limit=5):
    print("---" * 20)
    print(submission.title)
    print("FREQUENT WORDS: ")
    post = reddit.submission(id=submission.id)
    flattened_comments = list(post.comments)
    all_comments = ""
    for comment in flattened_comments:
        all_comments += comment.body
    comment_sentences = nltk.tokenize.sent_tokenize(all_comments)


    words = [word.lower() for sentence in comment_sentences for word in 
        nltk.tokenize.word_tokenize(sentence)]

    freq = nltk.FreqDist(words)

    freq_words = [word for word in freq.items() if word[0] not in all_stop_words][:15]

    print(freq_words)
