from django.db import connection


def execute(sqlstr_and_params_list, fetchone=False, as_dict=True):
	with connection.cursor() as cursor:
		for sql, params in sqlstr_and_params_list:
			cursor.execute(sql, params)

		if fetchone:
			return cursor.fetchone()
		if as_dict:
			return dictfetchall(cursor)
		return cursor.fetchall()


def dictfetchall(cursor):
	"Return all rows from a cursor as a dict"
	columns = [col[0] for col in cursor.description]
	return [
		dict(zip(columns, row))
		for row in cursor.fetchall()
	]
