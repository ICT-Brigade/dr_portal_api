# from django.db import models
# import uuid


# class Tweet(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	tweet_id = models.BigIntegerField()
# 	date = models.DateField()
# 	time = models.CharField(max_length=140)
# 	timezone = models.CharField(max_length=140)
# 	user_id =  models.BigIntegerField(),
# 	username = models.CharField(max_length=140)
# 	name = models.CharField(max_length=140)
# 	tweet = models.TextField()
# 	link = models.URLField()
# 	replies_count = models.IntegerField()
# 	retweets_count = models.IntegerField()
# 	likes_count = models.IntegerField()
# 	retweet = models.BooleanField()
# 	quote_url = models.TextField()
# 	video = models.IntegerField()
# 	thumbnail = models.URLField()
# 	near = models.CharField(max_length=140)
# 	geo = models.TextField()
# 	source = models.TextField()
# 	user_rt_id = models.CharField(max_length=140)
# 	user_rt = models.CharField(max_length=140)
# 	retweet_id = models.IntegerField()
# 	retweet_date = models.DateField()
# 	translate = models.TextField()
# 	trans_src = models.TextField()
# 	trans_dest = models.TextField()


# class TweetLink(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	tweet_id = models.ForeignKey(
# 		'Tweet',
# 		on_delete=models.CASCADE,
# 	)
# 	link = models.URLField()
# 	link_type = models.CharField(max_length=140)


# class Hashtag(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	name = models.CharField(max_length=140)


# class TweetHashtag(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	tweet_id = models.ForeignKey(
# 		'Tweet',
# 		on_delete=models.CASCADE,
# 	)
# 	hashtag_id = models.ForeignKey(
# 		'Hashtag',
# 		on_delete=models.CASCADE,
# 	)
