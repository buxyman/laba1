print('оригинал песни: Земфира - "Хочешь?" ')
print('Пожалуйста не отчисляй')
print('ведь меня прибью все дома')
print('тебе конечно все равно,')
print('а мне казарма станет домом/n')
print('оригинал песни: Stigmata - "Сентябрь"')
print('Сентябрь горит, студентик плачет.')
print('Ведь он не смог допуститься к сдаче.')
print('Прольётся крооооовь, Виталя расскажет')
print('как он уйдет...')

fib1, fib2 = 1, 1
n = 988
while n > 0:
	fib1, fib2 = fib2, fib1 + fib2
	n -= 1
	
print('значение тысячного числа фибоначчи:', fib2)
