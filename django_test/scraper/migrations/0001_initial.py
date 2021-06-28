# Generated by Django 3.2 on 2021-04-25 02:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tweet_id', models.BigIntegerField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=140)),
                ('timezone', models.CharField(max_length=140)),
                ('username', models.CharField(max_length=140)),
                ('name', models.CharField(max_length=140)),
                ('tweet', models.TextField()),
                ('link', models.URLField()),
                ('replies_count', models.IntegerField()),
                ('retweets_count', models.IntegerField()),
                ('likes_count', models.IntegerField()),
                ('retweet', models.BooleanField()),
                ('quote_url', models.TextField()),
                ('video', models.IntegerField()),
                ('thumbnail', models.URLField()),
                ('near', models.TextField()),
                ('geo', models.TextField()),
                ('source', models.TextField()),
                ('user_rt_id', models.CharField(max_length=140)),
                ('user_rt', models.CharField(max_length=140)),
                ('retweet_id', models.IntegerField()),
                ('retweet_date', models.DateField()),
                ('translate', models.TextField()),
                ('trans_src', models.TextField()),
                ('trans_dest', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TweetLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('link_type', models.CharField(max_length=140)),
                ('tweet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.tweet')),
            ],
        ),
        migrations.CreateModel(
            name='TweetHashtag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hashtag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.hashtag')),
                ('tweet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.tweet')),
            ],
        ),
    ]