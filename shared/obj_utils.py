from django.core.exceptions import ValidationError


def keys_to_number(obj, keys, to_int=False, to_float=False):
	new_dict = {}
	for k, v in obj.items():
		try:
			if k in keys and to_int:
				new_dict[k] = int(v)
			elif k in keys and to_float:
				new_dict[k] = float(v)
			else:
				new_dict[k] = v
		except ValueError as e:
			raise ValidationError(f"'{k}' should be a valid number")
	return new_dict


def as_map(arr, key):
	"""Converts a list of dict or object into a map"""

	def get_key(obj, key):
		return obj[key] if type(obj) == dict else getattr(obj, key)

	return {get_key(element, key): element for element in arr}
