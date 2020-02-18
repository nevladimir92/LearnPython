city_temp = {'city': 'Moscow', 'temperature': '20'}
print(city_temp['city'])
city_temp['temperature'] = int(city_temp['temperature']) - 5 # или city_temp['temperature'] = '15'
print(city_temp)

print(city_temp.get('counrty', 'Russia'))

city_temp['date'] = '27.05.2019'
print(len(city_temp))