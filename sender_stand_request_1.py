
import configuration_1
import data_1
import requests

def create_order():
    return requests.post(
        configuration_1.URL_SERVICE + configuration_1.CREATE_ORDER_PATH,
        json=data_1.order_body
    )
    
    
def get_order_by_track(track_number):
    url = configuration_1.URL_SERVICE + configuration_1.GET_ORDER_PATH
    params = {"t": track_number}
    return requests.get(url, params=params)
