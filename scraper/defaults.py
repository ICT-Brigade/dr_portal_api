import twint
from datetime import timedelta
from shared.date_utils import nowdate

DATE_TODAY = nowdate()
DEFAULT_SEARCH = " volunteer OR donation OR donasyon OR in kind OR relief OR rescue"
QS_OPTS_MAP = {
	"Hashtags": {
		"key": "Search",
		"operation": "concat",
		"default": DEFAULT_SEARCH
	},
	"From_date": {
		"key": "Since",
		"operation": None,
		"default": (DATE_TODAY - timedelta(days=365)).strftime("%Y-%m-%d")
	},
	"To_date": {
		"key": "Until",
		"operation": None,
		"default": DATE_TODAY.strftime("%Y-%m-%d")
	},
	"Year": {
		"key": "Year",
		"operation": "ignore_fields",
		"fields": ["Since", "Until"],
		"default": DATE_TODAY.strftime("%Y")
	}
}
TWINT_OPTS = [k.lower() for k in list(twint.Config().__dataclass_fields__.keys()) + list(QS_OPTS_MAP.keys())]
DEFAULT_OPTS = {
	"Retweets": False,
	"Filter_retweets": True,
	"Pandas": True,
	"Hide_output": True,
	"Stats": False,
	"Limit": 20,
	"Since": (DATE_TODAY - timedelta(days=365)).strftime("%Y-%m-%d"),
	"Until": DATE_TODAY.strftime("%Y-%m-%d"),
	# "Year": DATE_TODAY.strftime("%Y")
}
