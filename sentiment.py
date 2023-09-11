import pandas as pd
from transformers import pipeline

def sentiment(text):
    classifier = pipeline("sentiment-analysis")
    return classifier(text)[0]['label']

def main(file):

    df=pd.read_excel(file)
    flname=str(file.name).strip('.xlsx')
    batch=''
    for i in flname:
        if i !='-':
            batch+=i
        else:
            break
    date=flname.strip(batch).strip('-')

    df['Batch']=batch
    df['Date']=date
    df.drop(['Email','Mobile'],axis=1,inplace=True)
    M_senti=list(map(sentiment,df['Mentor Feedback']))
    df['Mentor Feedback Sentiment']=M_senti
    S_senti=list(map(sentiment,df['Session Feedback']))
    df['Session Feedback Sentiment']=S_senti
    
    return df

if __name__=='__main__':
    file='File path'
    df=main(file)
    