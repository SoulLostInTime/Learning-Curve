import numpy as np
import pandas as pd

def addKey(dictionary,key):
	'''Adds key to dictionary with empty list if
		key not already present.'''
	# no overriding of keys allowed!
	if key.lower() not in dictionary:
		dictionary[key.lower()] = NaN
		print('Key', key,'succesfully added.')
	else:
		print('Key is already present.')

def addValue(dictionary,key,value):
	'''Adds value to a list with specified key
		if the key is present in the dictionary.'''
	try:
		value = int(value)
	except:
		print('Value must be a number.')
		return

	if key.lower() in dictionary:
		dictionary[key] = dictionary[key] + value
		print('Value succesfully added.\n')
	else:
		print('Key not found.')

def removeKey(dictionary, key, confirm):
	'''Remove the given key and all corresponding data
		from the dictionary'''
	if key.lower() in dictionary:
		if confirm.lower() == 'true':
			del dictionary[key.lower()]
			print('Key', key, 'deleted succesfully.')
		else:
			print('Action aborted.')
	else:
		print('Key not found.')

def removeValue(dictionary, key):
	'''Removes the given value from the key in the
		dictionary.'''
	try:
		value = int(value)
	except:
		print('Value must be a number.')
		return

	if key.lower() in dictionary:
		dictionary[key] = 0
	else:
		print('Key not found.')


main_df = pd.read_csv('haushaltsplan.csv', index_col=0)
main_df = main_df.fillna(0)
main_dict = main_df.to_dict()
print(main_dict)
main_user_input = ''

while main_user_input != 'quit':
	user_input = ''
	print(main_df)
	main_user_input = input('Select month: ').lower()

	while user_input != 'quit' and main_user_input != 'quit':
		main_df = pd.DataFrame(main_dict)
		print(main_df)

		user_input = input('Select action: ')

		if user_input == 'add key':
			# add key to main_dict
			key_input = input('Specifiy key name: ')
			addKey(main_dict[main_user_input], key_input)

		elif user_input == 'add value':
			# add value to a key, key must be in main_dict
			key_input = input('Specify key: ')
			value_input = input('Specify value: ')
			addValue(main_dict[main_user_input], key_input, value_input)

		elif user_input == 'remove key':
			# delete key and corresponding data from main_dict, ask for confirmation
			key_input = input('Specify key: ')
			confirm_input = input('Confirm deletion of' + str(key_input) + 'and all corresponding data? ')
			removeKey(main_dict[main_user_input], key_input, confirm_input)

		elif user_input == 'remove value':
			# delete value from key
			key_input = input('Specify key: ')
			value_input = input('Specify value: ')
			removeValue(main_dict[main_user_input], key_input, value_input)

		elif user_input == 'print dict':
			print(main_dict)

		elif user_input == 'print df':
			print(main_df)

main_df.to_csv('haushaltsplan.csv')
#todo: add key and remove key to outer most loop. keys are applicable only on
#		the whole row