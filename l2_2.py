def averageResult(n1,n2,n3,n4,n5):
	n1 = convertToNumber(n1)
	n2 = convertToNumber(n2)
	n3 = convertToNumber(n3)
	n4 = convertToNumber(n4)
	n5 = convertToNumber(n5)
	result = getAverage(n1,n2,n3,n4,n5)
	return obtainAverageString(result)

def convertToNumber(number):
	return float(number)

def getAverage(n1,n2,n3,n4,n5):
	return (n1 + n2 + n3 + n4 + n5 - max(n1,n2,n3,n4,n5) - min(n1,n2,n3,n4,n5)) / 3

def obtainAverageString(number):
	if number < 1 :
		return "Horrible"
	elif number < 2 :
		return "Bad"
	elif number < 3 :
		return "Ok"
	elif number < 4 :
		return "Nice"
	elif number <= 5:
		return "Excelent"


print(averageResult(5,2,3,"26",3.2))