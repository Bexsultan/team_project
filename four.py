str = input("Напишите предложение: ")
splitting = str.split(" ")
length = len(splitting)

for i in range(0, length):
	if i != 6:
		print(str)
	else:
		breakinput1 = input("Введите дату в формате 2020-10-24 18:30: ")

year_idx = input1[0:4]
month_idx = input1[5:7]
day_idx = input1[8:10]
time_idx = input1[11:17]

dict1 = { "year" : year_idx,
          "month" : month_idx,
          "day" : day_idx,
          "time" : time_idx
}
print(dict1)
