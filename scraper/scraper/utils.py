import ast
from scraper.defaults import TWINT_OPTS
from scraper import defaults


def qs_to_config_opts(qs_dict):
	return {k.capitalize():v for k, v in qs_dict.items() if k.lower() in TWINT_OPTS}


def make_options(opts):
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
