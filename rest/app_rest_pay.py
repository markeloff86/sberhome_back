# -*- coding: utf-8 -*-

import requests
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
base_url = 'https://gate.vp.ru'
# base_url = 'https://testgate.vseplatezhi.ru'
header = {'Content-Type': 'application/x-www-form-urlencoded'}


# Успешно:
# Отображение страницы с
# формой оплаты (формой ввода
# данных карты).
# Ошибка:
# Отображение страницы с
# описанием ошибки и HTTPкодом,
# соответствующем типу
# ошибки.
@app.route('/pay', methods=['GET', 'POST'])
def post_request_pay():
    request_pay = base_url + '/main'
    res = requests.post(request_pay, data='amount=155.00&orderId=29735370&terminal=10000003&merchant=20000001&userid=&description=%D0%9F%D0%BB%D0%B0%D1%82%D0%B5%D0%B6+%D0%B2+%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B5+%D0%92%D1%81%D0%B5%D0%9F%D0%BB%D0%B0%D1%82%D0%B5%D0%B6%D0%B8&clientBackUrl=https%3A%2F%2Fvp.ru%2Fcommon-modal%2F%3Faction%3Dgwsuccess%26request_number%3D29735370&sign=898fa1a668319295ae1c9a9cbf6538ce7fac86baf20074ec8f2db6f856e277d5', headers=header)
    print('post_request_pay status code:', res.status_code)
    print(res.text)
    return res


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    # post_request_pay()
    # post_request_status()
