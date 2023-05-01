
def calculator(string):
	try:
		string = string.lower().replace(' ', '')
		# print(string)
		parts = string.split('+')

		for plus in range(len(parts)):
			if '-' in parts[plus]:
				parts[plus] = parts[plus].split('-')
		# print(parts)

		for plus in range(len(parts)):
			parts[plus] = precalculator(parts[plus])
		# print(parts)
		result = sum(parts)
	except ValueError:
		result = 'Only numbers!!!'
	except ZeroDivisionError:
		result = 'Devesion by zero!!!'
	return result 



def precalculator(part):

	if type(part) is str:

		if '*' in part:
			# parts = part.split('*')
			result = 1
			for subpart in part.split('*'):
				# result *= float(subpart)
				result *= precalculator(subpart)
			return result

		elif '/' in part:
			# parts = list(map(float, part.split('/')) )
			parts = list(map(precalculator, part.split('/')) )
			result = parts[0]
			for subpart in parts[1:]:
				result /= subpart
			return result
		else:
			return float(part)


	elif type(part) is list:
		for i in range(len(part)):
			part[i] = precalculator(part[i])
		return part[0] - sum(part[1:])

	return part




#  10 + 2 * 3 - 4 + 1 / 2
if __name__=="__main__":
	print(calculator('3 / 2 + 10 + 2 * 3 * 2.5 - 4 + 1 / 2'))
	print(calculator('3 / 2 * 6 / 2 + 10'))
	print(calculator('1 - 3 / 2'))


	# print(precalculator('1/2/3'))