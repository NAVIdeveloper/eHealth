import math
from .models import *

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

def check_algoritm(obj):
    if obj.height % 2 != 0:
        obj.height = obj.height -1
    normals = Normal.objects.filter(age_start__lte=obj.age,age_end__gte=obj.age,height=obj.height)
    norma = normals[0]
    if obj.gender == 1:
        if norma.male_weight < obj.height:
            return norma.male_weight
        else:
            return False
    else:
        if norma.female_weight < obj.height:
            return norma.female_weight
        else:
            return False


def algoritm_loss(days:int,kg:int):
    one_kg_kk = 3500
    have_to_loss_a_day = int(int(kg*one_kg_kk) / days)
    
    return have_to_loss_a_day


# print(is_normal(weight=51,age=20,height=149,male=True)) #True normal #False bunday norma mavjud emas #int ozishi kerak
# print(calorie_male(weight=51,age=20,height=149)) # kunlik kaloriya
# print(calorie_female(weight=48,age=20,height=149)) # kunlik kaloriya


def date_week(value:str):
	years = [1,9999]
	months = [1,12]
	days = [1,31]
	DAYS = ["Shanba","Yakshanba","Dushanba","Seshanba","Chorshanba","Payshanba","Juma"]
	index_day = 0
	run = True
	p = 0
	for y in range(years[0],years[1]+1):
		if run == False:
			break
		y = str(y)
		if len(y) != 4:
			while len(y) != 4:
				y = "0"+y
		for m in range(months[0],months[1]+1):
			m = str(m)
			if len(m) != 2:
				m = "0"+m
			if m[1] == '2' and m[0] == '0':
				y1 = y
				if y1[0] == "0":
					y1 = y1[1:]
				if y1[0] == '0':
					y1 = y1[1:]
				if y1[0] == '0':
					y1 = y1[1:]
				p = int(y1)
				if p % 4 == 0:
					days[1] = 29
				else:
					days[1] = 28
			elif m[1] in ['4','6','9'] and m[0] == '0':
				days[1] = 30
			elif m == '11':
				days[1] = 30
			else:
				days[1] = 31

			for d in range(days[0],days[1]+1):
				d = str(d)
				if len(d) != 2:
					d = "0"+d
				index_day += 1
			
				if index_day == 7:
					index_day = 0
				if f"{y}-{m}-{d}" == value:
					run = False
					return DAYS[index_day]
