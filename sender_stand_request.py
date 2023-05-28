import requests
import configuration
import data


# Функция для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER_PATH,
                         json=body)
response = post_new_order(data.order_body);
print(response.status_code)
print(response.json())

# Функция для получения информации о заказе
def get_order(track):
    return requests.get(configuration.URL_SERVICE+configuration.GET_ORDER_PATH, track)
track = response.json()["track"]
resp_order = get_order(track)
print(resp_order.status_code)
print(resp_order.json())
assert resp_order.status_code==200






