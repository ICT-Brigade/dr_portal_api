import twint
from . import utils


def get_tweets(**opts):
	"""
		Returns a list of tweets(of type dict) that satisfies the parametes in opts dict
		:param opts: dict
			A dictionary with the ff. structure:
			{
				'from_date': '2021-01-01',
				'to_date': '2021-07-25',
				'limit': '1000',
				'hashtags': '#fabianph relief OR donation OR rescue OR volunteer OR donasyon'
			}
		:return : list of dict
	"""
	opts = utils.qs_to_config_opts(opts)
	opts = utils.make_options(opts)
	c = twint.Config(**opts)
	twint.run.Search(c)
	Tweets_df = twint.storage.panda.Tweets_df
	return Tweets_df.to_dict("records")
