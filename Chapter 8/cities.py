def describe_city(name, country="France"):
	"""Prints the name of a city and a country. Default country is France"""
	msg = (f"\n{name.title()} is in {country.title()}.")
	print(msg)

describe_city("paris")
describe_city("amsterdam")
describe_city("reykjavik", "iceland")