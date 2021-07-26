import re
from jsonschema import (
	exceptions,
	Draft7Validator
)


def get_validator(schema):
	def validator(*args, **kwargs):
		def _get_error(err):
			return {
				"message": err.message,
				"key": get_offending_key(err),
				"context": err.validator
			}

		try:
			v = Draft7Validator(
				schema,
				format_checker=kwargs.get("format_checker")
			)
			errors = sorted(v.iter_errors(kwargs.get("data")), key=str)

			return list(
				map(lambda err: _get_error(err), errors)
			) if len(errors) else None
		except exceptions.ValidationError as v:
			raise v

	return validator


def get_offending_key(err):
	return (re.findall(r"\'.*?\'", err.message)[0].replace("'", "") or "") \
		if not len(err.path) else "".join(
			map(
				lambda part: str("[{}]".format(part) if isinstance(part, int) else part),
				err.path
			)
		)
