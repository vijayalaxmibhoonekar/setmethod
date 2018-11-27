vowels={'a','e','i','u'}
vowels.add('o')
print('vowels are:',vowels)
print("--------------------------------------")

vowels={'a','e','i','o','u'}
print('vowels(before clear):',vowels)
vowels.clear()
print('vowels(after clear):',vowels)
print("--------------------------------------")

numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()

new_numbers.add('5')

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)