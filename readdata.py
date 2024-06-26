import pandas as pd 

tranding_videos = pd.read_csv(r"E:\Study Mateiral\python projects\youtube data collection\trending_videos.csv")

# print(newfile.head())


tranding_videos['description'].fillna('No description',inplace=True)

tranding_videos['published_at'] = pd.to_datetime(tranding_videos['published_at'])

tranding_videos['tags']= tranding_videos['tags'].apply(lambda x : eval(x) if isinstance(x,str) else x)

missing_values = tranding_videos.isnull().sum()
data_types = tranding_videos.dtypes
# print(missing_values)
# print("\n")
# print(data_types)

descripted_stats = tranding_videos[['view_count', 'like_count', 'dislike_count', 'comment_count']].describe()

print( descripted_stats)







