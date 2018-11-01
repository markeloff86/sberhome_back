# -*- coding: utf-8 -*-

import uuid
from datetime import datetime, timedelta

import dateutil.parser as parser
from flask import Flask, jsonify
from flask_cors import CORS

import db_helper as db

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


# Заглушки. Эмулириют СБОЛ, возвращают название копилки, описание и кол-во денег
def get_name():
    return ['Контроль потребления электричества', 'Ограничение ночного холодильника']


def get_info():
    return ['Потребление электричества выше среднего, откладываем на оплату',
            'Холодильник был открыт во время запрета, откладываем на тренировки']


def get_cash():
    return [200, int(db.select_challenges("cash"))]


@app.route('/pushNotification', methods=['GET', 'POST'])
def push_notification():
    if not is_fail():
        return jsonify({})
    new_cash = int(db.select_challenges("cash")) + int(db.select_challenges("cost"))
    db.update_challenges("cash", str(new_cash))
    random_uuid = str(uuid.uuid4())
    notification = {
        "id": random_uuid,
        "name": get_name()[1],
        "info": get_info()[1],
        "cash": str(get_cash()[1]) + ' ₽'
    }
    return jsonify(notification=notification)


@app.route('/getMoneyBoxes', methods=['GET', 'POST'])
def get_cli_commands():
    try:
        boxes_list = []
        for i in (0, len(get_name()) - 1):
            emp_dict = {
                'name': get_name()[i],
                'cash': str(get_cash()[i]) + ' ₽'
            }
            boxes_list.append(emp_dict)
    except:
        return "Ошибка получения списка умных копилок"
    return jsonify(smart_box=boxes_list)


def is_fail():
    last_update_time = db.select_challenges("last_update_time")
    fail_time = db.select_challenges("fail_time")
    # если last_update_time > fail_time и last_update_time < 6:00 следующего дня, return true
    return (parser.parse(last_update_time) > parser.parse(fail_time)) and parser.parse(last_update_time) < parser \
        .parse(datetime.strftime(datetime.now() + timedelta(days=1), "%Y.%m.%d 06:00:00"))


if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.150')
    # app.run(debug=True, host='127.0.0.1')
