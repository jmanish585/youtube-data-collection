import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import isodate
from googleapiclient.discovery import build

API_KEY =  'AIzaSyCct3byElq54qWQD0L4KD6R6a5p-C8JzgY'
youtube = build('youtube', 'v3', developerKey=API_KEY)

trending_videos = pd.read_csv(r"C:\Users\hp\Documents\Projects\youtube-data-collection\trending_videos.csv")
trending_videos['published_at'] = pd.to_datetime(trending_videos['published_at'])

# extract hour of publication
trending_videos['publish_hour'] = trending_videos['published_at'].dt.hour

# bar chart for publish hour distribution
plt.figure(figsize=(12, 6))
sns.countplot(x='publish_hour', data=trending_videos, palette='coolwarm')
plt.title('Distribution of Videos by Publish Hour')
plt.xlabel('Publish Hour')
plt.ylabel('Number of Videos')
plt.show()

# scatter plot for publish hour vs view count
plt.figure(figsize=(10, 6))
sns.scatterplot(x='publish_hour', y='view_count', data=trending_videos, alpha=0.6, color='teal')
plt.title('Publish Hour vs View Count')
plt.xlabel('Publish Hour')
plt.ylabel('View Count')
plt.show()