from datetime import datetime, timedelta

def date_range(start, stop, step):

	while start < stop:
		yield start
		start = start + step
        
print('Задайте стартовые числовые значения для точки отсчета: year=..., month=..., day=..., hour=..., minute=... ')
print('(Вводя каждое число с новой строки)')
start_point = datetime(year=int(input()), month=int(input()), day=int(input()), hour=int(input()), minute=int(input()))
print('Аналогичным образом задайте конечные числовые значения')
end_point = datetime(year=int(input()), month=int(input()), day=int(input()), hour=int(input()), minute=int(input()))

your_step = timedelta(days=1, hours=0, minutes=0)

print('Ваши даты с шагом в день:')
for i in date_range(start_point, end_point, your_step):
	print(i)
