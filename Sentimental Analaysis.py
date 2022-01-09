import boto3
from botocore.exceptions import ClientError
import pandas as pd
import json
import tarfile
data = "C:/Users/Admin/Desktop/Asia University final project/Sentiment Analysis (Amazon Comprehend)/amazon_tweets.csv"

df = pd.read_csv(data, header = None, dtype = 'str', encoding = 'utf-8') 

text = df.loc[12].item()
print(text)
print(" ")
print("##################### ANALYSIS#############################")

# carry out the translation
comprehend = boto3.client('comprehend','us-east-1')
print('Calling DetectSentiment')
sentiment = json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
print(sentiment)
print('End of DetectSentiment\n')

print('Calling DetectDominantLanguage')
print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))
print("End of DetectDominantLanguage\n")

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectEntities\n')

print('Calling DetectKeyPhrases')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectKeyPhrases\n')

print('Calling PII entities')
print(json.dumps(comprehend.detect_pii_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of PII entities\n')

print('Calling DetectSyntax')
print(json.dumps(comprehend.detect_syntax(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSyntax\n')
      

