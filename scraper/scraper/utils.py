import ast
from scraper.defaults import TWINT_OPTS
from scraper import defaults


def qs_to_config_opts(qs_dict):
	"""
		Returns a dictionary whose keys are valid twint search param
		:param qs_dict: dict
			A dictionary with the ff. structure:
			{
				'from_date': '2021-01-01',
				'to_date': '2021-07-25',
				'limit': '1000',
				'hashtags': '#fabianph relief OR donation OR rescue OR volunteer OR donasyon',
				'random_key_1': '',
				'random_key_2': ''
			}
		:return : dict
			{
				'From_date': '2021-01-01',
				'To_date': '2021-07-25',
				'Limit': '1000',
				'Hashtags': '#fabianph relief OR donation OR rescue OR volunteer OR donasyon'
			}
	"""
	return {k.capitalize():v for k, v in qs_dict.items() if k.lower() in TWINT_OPTS}


def make_options(opts):
	"""
		Transforms opts dict in a format that can be recognize by twint.Config()
		:param opts: dict
			A dictionary with the ff. structure:
			{
				'From_date': '2021-01-01',
				'To_date': '2021-07-25',
				'Limit': '1000',
				'Hashtags': '#fabianph relief OR donation OR rescue OR volunteer OR donasyon'
			}
		:return : dict
			{
				'Limit': '1000',
				'Retweets': False,
				'Filter_retweets': True,
				'Pandas': True,
				'Hide_output': True,
				'Stats': False,
				'Since': '2021-01-01',
				'Until': '2021-07-25',
				'Search': '#fabianph relief OR donation OR rescue OR volunteer OR donasyon'
			}
	"""
	new_opts = opts.copy()
	new_opts = set_default_options(new_opts)
	for k, v in opts.items():
		if k in defaults.QS_OPTS_MAP:
			operation = defaults.QS_OPTS_MAP[k]["operation"]
			if operation == "concat":
				new_opts[defaults.QS_OPTS_MAP[k]["key"]] = v + defaults.QS_OPTS_MAP[k]["default"]
			elif operation == "ignore_fields":
				fields = defaults.QS_OPTS_MAP[k]["fields"]
				for field in fields:
					if field in new_opts:
						del new_opts[field]
				new_opts[defaults.QS_OPTS_MAP[k]["key"]] = v
				continue
			else:
				new_opts[defaults.QS_OPTS_MAP[k]["key"]] = v
			del new_opts[k]
	return new_opts


def set_default_options(opts):
	new_opts = opts.copy()
	for k, v in defaults.DEFAULT_OPTS.items():
		if k not in new_opts or k in new_opts and not v:
			new_opts[k] = v
	return new_opts
