cars_list = [{'name': 'BMW X6', 'model': 'BMW', 'price': 6000111},
            {'name': 'Toyota Corolla', 'model': 'Toyota', 'distance': 72000},
            {'name': 'Haval 7', 'model': 'Haval', 'price': 3500222}]


for car in cars_list:
    print(set(i + '=' + str(car[i]) for i in car))
print(list(i + '=' + str(car[i]) for car in cars_list for i in car))