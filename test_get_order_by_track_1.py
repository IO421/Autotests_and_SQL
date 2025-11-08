# Овчаренко Ирина, 37-я когорта финальный проект. Инженер по тестированию плюс


import data_1
import configuration_1
import sender_stand_request_1

def test_create_and_get_order():
    # Шаг 1: Создаём заказ
    create_response = sender_stand_request_1.create_order()
    
    # Шаг 2: Сохраняем трек‑номер из ответа
    track_number = create_response.json()["track"]
    
    
    # Шаг 3: Получаем заказ по трек‑номеру
    get_response = sender_stand_request_1.get_order_by_track(track_number)
    
    
    # Шаг 4: Проверяем, что код ответа равен 200
    assert get_response.status_code == 200

