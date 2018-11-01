# -*- coding: utf-8 -*-

import random
import sqlite3
import uuid
from datetime import datetime, timedelta

import dateutil.parser as parser
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


def get_param_from_db(param):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    sql = "SELECT " + param + " FROM challenges"
    cursor.execute(sql)
    print(cursor.fetchone()[0])
    return cursor.fetchone()[0]


# Заглушки. Эмулириют СБОЛ, возвращают название копилки, описание и кол-во денег
def get_name():
    return ['Контроль потребления электричества', 'Ограничение ночного холодильника']


def get_info():
    return ['Потребление электричества выше среднего, откладываем на оплату',
            'Холодильник был открыт во время запрета, откладываем на тренировки']


def get_cash():
    return [200, 100]


@app.route('/pushNotification', methods=['GET', 'POST'])
def push_notification():
    if not is_fail():
        return jsonify({})
    random_uuid = str(uuid.uuid4())
    random_id = random.randint(0, len(get_name()) - 1)
    notification = {
        "id": random_uuid,
        "name": get_name()[random_id],
        "info": get_info()[random_id],
        "cash": str(get_cash()[random_id]) + ' ₽'
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
    last_update_time = get_param_from_db("last_update_time")
    fail_time = get_param_from_db("fail_time")
    # если last_update_time > fail_time и last_update_time < 6:00 следующего дня, return true
    return (parser.parse(last_update_time) > parser.parse(fail_time)) and parser.parse(last_update_time) < parser \
        .parse(datetime.strftime(datetime.now() + timedelta(days=1), "%Y.%m.%d 06:00:00"))


if __name__ == '__main__':
    # app.run(debug=True, host='192.168.43.150')
    app.run(debug=True, host='127.0.0.1')
