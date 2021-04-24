from requests import get, post, delete

# получение одного участника
print(get('http://127.0.0.1:5000/api/users/1').json())

# получение всех участников
print(get('http://127.0.0.1:5000/api/prod').json())



# добавление пользователя
print(post('http://127.0.0.1:5000/api/users',
           json={
                 'surname': 'программист',
                 'name': 'artem',
                 'address': 'белгород',
                 'pass': '123',
                 'email': 'abcd@mail.ru',
           "tel": "8952436289"}).json())

# добавление товара
print(post('http://127.0.0.1:5000/api/prod',
           json={
                 'product': 'программ',
                 'price': 500,
                 'leader': 1,
                 'opisanie': '28895243628895243362889524362889524362889524362889524362889524362889524362823',
                 }).json())



# получение всех товаров
print(get('http://127.0.0.1:5000/api/prod').json())