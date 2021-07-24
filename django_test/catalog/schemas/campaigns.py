import datetime
from shared.date_utils import nowdate


CAMPAIGN_QS = {
	"$schema":"http://json-schema.org/draft-07/schema#",
	"title":"Campaigns Query String",
	"type" : "object",
	"properties" : {
		"hashtags" : {
			"type" : "string",
			"minLength": 2
		},
		"near": {
			"type" : "string",
			"minLength": 2 
		},
		"from_date": {
			"type" : "string",
			"format": "date",
			"default": (nowdate() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
		},
		"to_date": {
			"type" : "string",
			"format": "date",
			"default": nowdate().strftime("%Y-%m-%d")
		},
		"year": {
			"type" : "string",
			"format": "date",
			"default": nowdate().strftime("%Y")
		},
		"limit": {
			"type" : "integer",
			"minimum": 1,
			"maximum": 100,
			"multipleOf" : 20,
			"default": 20
		}
	},
	"additionalProperties": False,
	"required": ["hashtags"]
}
