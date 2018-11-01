# -*- coding: utf-8 -*-

import random
import uuid
import sqlite3

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


def get_last_active(param):
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
    return ['5 дней подряд расход электричества не выше среднего',
            '4 дня подряд без открывния холодильника после ограниченного времени']


def get_cash():
    return [0, 100]


@app.route('/pushNotification', methods=['GET', 'POST'])
def push_notification():
    random_uuid = str(uuid.uuid4())
    random_id = random.randint(0, len(get_name()) - 1)
    notification = {"id": random_uuid, "name": get_name()[random_id], "info": get_info()[random_id],
                    "cash": get_cash()[random_id]}
    return jsonify(notification=notification)


@app.route('/getMoneyBoxes', methods=['GET', 'POST'])
def get_cli_commands():
    try:
        boxes_list = []
        for i in (0, len(get_name()) - 1):
            emp_dict = {
                'name': get_name()[i],
                'cash': get_cash()[i],
                'info': get_info()[i]}
            boxes_list.append(emp_dict)
    except:
        return "Error read JSON"
    return jsonify(smart_box=boxes_list)


@app.route('/checkDate', methods=['GET', 'POST'])
def date_compare():
    time_one = get_last_active("last_update_time")
    time_two = get_last_active("fail_time")
    return "last_update_time - " + time_two + " | exception time - " + time_one


if __name__ == '__main__':
    # app.run(debug=True, host='192.168.43.150')
    app.run(debug=True, host='127.0.0.1')
