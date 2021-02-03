password = 'a123456'
i = 3
while i > 0:
	pwd = input('Please enter password:')
	if pwd == password:
		print('Login successful!')
		break
	else:
		i = i - 1
		print('Login unsucessful. You still have', i, 'attempts')
