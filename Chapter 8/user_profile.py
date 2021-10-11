def build_profile(first, last, **user_info):
	'''Builds a user dictionary'''
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile("matt", 'fouquier', location='tampa', job="IT", pet='dog')

print(user_profile)