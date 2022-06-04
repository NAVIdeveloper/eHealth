import math


DATA = [
	{
		"id":1,
		"female-weight":48,
		"male-weight":51,
		"age-start":20,
		"age-end":29,
		"height":148,
	}
]

def calorie_male(weight,height,age):
	return (10 * weight) + (6.25 * height) - (5 * age) + 5

def calorie_female(weight,height,age):
	return (10 * weight) + (6.25 * height) - (5 * age) - 161

def is_normal(weight,age,height,male=False):
	norm = False
	looks_like = None
	if male:
		for d in DATA:
			if d['height'] == height or height - 1 == d['height']:
				if d['age-start'] <= age and age <= d['age-end']:
					looks_like = d
					if d['male-weight'] == weight:
						norm = True
						break
	else:
		for d in DATA:
			if d['height'] == height or height - 1 == d['height']:
				if d['age-start'] <= age and age <= d['age-end']:
					looks_like = d
					if d['female-weight'] == weight:
						norm = True
						break
	if norm:
		return True
	else:
		if looks_like != None:
			if male:
				if looks_like['male-weight'] < weight:
					return weight - looks_like['male-weight']
				else:
					return True
			else:
				if looks_like['female-weight'] < weight:
					return weight - looks_like['female-weight']
				else:
					return True
		else:
			return False




# print(is_normal(weight=51,age=20,height=149,male=True)) #True normal #False bunday norma mavjud emas #int ozishi kerak
# print(calorie_male(weight=51,age=20,height=149)) # kunlik kaloriya
# print(calorie_female(weight=48,age=20,height=149)) # kunlik kaloriya

