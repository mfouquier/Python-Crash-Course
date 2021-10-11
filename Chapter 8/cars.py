def car_data(make, model, **car_info):
	car_info['make'] = make
	car_info['model'] = model
	return car_info

car_type = car_data('subaru', 'outback', color='blue', tow_package=True)
print(car_type)