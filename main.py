import nltk,glob,os,csv;from nltk.sentiment import SentimentIntensityAnalyzer;nltk.download('vader_lexicon');os.system('clear');sid,scores =SentimentIntensityAnalyzer(),{}
def result(avgscore):
    if avgscore > 0.05 and avgscore < 0.5: return "Positive"
    elif avgscore > 0.5: return "Very Positive"
    elif avgscore < -0.05 and avgscore > -0.5: return "Negative"
    elif avgscore < -0.5: return "Very Negative"
    else: return "Neutral"
def getquery(): 
    return glob.glob("*.txt")
def getinfo(query):
    tweetslst = []
    with open(query, "r") as f:
        for line in f: tweet = line.strip();tweetslst.append(tweet)
    return tweetslst
def average(scores): return sum(scores)/len(scores)
def analyse(name):
    tweets = getinfo(name)
    for tweet in tweets:
        sentiment_scores = sid.polarity_scores(tweet)
        scores[tweet] = sentiment_scores['compound']
    query_,avg = name.replace(".txt", ""),average(scores.values());res=result(avg);scores["Average"],scores["Result"]=avg,res
    with open(f"{query_}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Text", "Score"])
        for tweet in tweets:
            score = scores[tweet]
            writer.writerow([tweet, score])
        writer.writerow(["Average", avg])
        writer.writerow(["Result", res])
    print(f"Item: {query_}\nScore: {avg}\nResult: {res}")
#RUN
if input().lower() == "clear":
    os.system("clear")
    for file in os.listdir():
        if file.endswith(".txt") or file.endswith(".csv"): os.remove(file)
else:
    os.system("clear")
    for name_ in getquery(): analyse(name_);scores={}
