import twint
from . import utils


def get_tweets(**opts):
	opts = utils.qs_to_config_opts(opts)
	opts = utils.make_options(opts)
	c = twint.Config(**opts)
	twint.run.Search(c)
	Tweets_df = twint.storage.panda.Tweets_df
	return Tweets_df.to_dict("records")
