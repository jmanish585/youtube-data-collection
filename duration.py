import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import isodate
from googleapiclient.discovery import build

API_KEY =  'AIzaSyCct3byElq54qWQD0L4KD6R6a5p-C8JzgY'
youtube = build('youtube', 'v3', developerKey=API_KEY)

trending_videos = pd.read_csv(r"C:\Users\hp\Documents\Projects\youtube-data-collection\trending_videos.csv")

trending_videos['duration_seconds'] = trending_videos['duration'].apply(lambda x: isodate.parse_duration(x).total_seconds())
trending_videos['duration_range'] = pd.cut(trending_videos['duration_seconds'], bins=[0, 300, 600, 1200, 3600, 7200], labels=['0-5 min', '5-10 min', '10-20 min', '20-60 min', '60-120 min'])

# scatter plot for video length vs view count
plt.figure(figsize=(10, 6))
sns.scatterplot(x='duration_seconds', y='view_count', data=trending_videos, alpha=0.6, color='purple')
plt.title('Video Length vs View Count')
plt.xlabel('Video Length (seconds)')
plt.ylabel('View Count')
plt.show()

# bar chart for engagement metrics by duration range
length_engagement = trending_videos.groupby('duration_range')[['view_count', 'like_count', 'comment_count']].mean()

fig, axes = plt.subplots(1, 3, figsize=(18, 8))

# view count by duration range
sns.barplot(y=length_engagement.index, x=length_engagement['view_count'], ax=axes[0], palette='magma')
axes[0].set_title('Average View Count by Duration Range')
axes[0].set_xlabel('Average View Count')
axes[0].set_ylabel('Duration Range')

# like count by duration range
sns.barplot(y=length_engagement.index, x=length_engagement['like_count'], ax=axes[1], palette='magma')
axes[1].set_title('Average Like Count by Duration Range')
axes[1].set_xlabel('Average Like Count')
axes[1].set_ylabel('')

# comment count by duration range
sns.barplot(y=length_engagement.index, x=length_engagement['comment_count'], ax=axes[2], palette='magma')
axes[2].set_title('Average Comment Count by Duration Range')
axes[2].set_xlabel('Average Comment Count')
axes[2].set_ylabel('')

plt.tight_layout()
plt.show()

# calculate the number of tags for each video
trending_videos['tag_count'] = trending_videos['tags'].apply(len)

# scatter plot for number of tags vs view count
plt.figure(figsize=(10, 6))
sns.scatterplot(x='tag_count', y='view_count', data=trending_videos, alpha=0.6, color='orange')
plt.title('Number of Tags vs View Count')
plt.xlabel('Number of Tags')
plt.ylabel('View Count')
plt.show()




# #Now, let’s analyze the content and the duration of videos:
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=['duration_seconds'], y=['view_count'], data=trending_videos, alpha=0.6, color='purple')
# plt.title('Video Length vs View Count')
# plt.xlabel('Video Length (seconds)')
# plt.ylabel('View Count')
# plt.show()



# # bar chart for engagement metrics by duration range
# length_engagement = trending_videos.groupby('duration_range')[['view_count', 'like_count', 'comment_count']].mean()
# fig, axes = plt.subplots(1, 3, figsize=(18, 8))

# # view count by duration range
# sns.barplot(y=length_engagement.index, x=length_engagement['view_count'], ax=axes[0], palette='magma')
# axes[0].set_title('Average View Count by Duration Range')
# axes[0].set_xlabel('Average View Count')
# axes[0].set_ylabel('Duration Range')

# # like count by duration range
# sns.barplot(y=length_engagement.index, x=length_engagement['like_count'], ax=axes[1], palette='magma')
# axes[1].set_title('Average Like Count by Duration Range')
# axes[1].set_xlabel('Average Like Count')
# axes[1].set_ylabel('')

# # comment count by duration range
# sns.barplot(y=length_engagement.index, x=length_engagement['comment_count'], ax=axes[2], palette='magma')
# axes[2].set_title('Average Comment Count by Duration Range')
# axes[2].set_xlabel('Average Comment Count')
# axes[2].set_ylabel('')
# plt.tight_layout()
# plt.show()