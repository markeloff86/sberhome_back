-- Создание таблицы с настройками челенджей
-- @name: название челенджа,
-- @status:  0 - не активен, 1 - активен
-- @cost - стоимсоть штрафа
-- @last_update_time -  дата последней активации. format: HH:MM
CREATE TABLE challenges (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    status INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    cash INTEGER NOT NULL,
    fail_time TEXT NOT NULL,
    last_update_time TEXT NOT NULL
);

-- Заполнение БД
--INSERT INTO challenges(id, name, status, cost, fail_time, last_update_time)
--VALUES (1, "Контроль потребления электричества", 0, 100, "01:00", "23:00");

INSERT INTO challenges(id, name, status, cost, cash, fail_time, last_update_time)
VALUES (1, "Ограничение ночного холодильника", 1, 100, 0, "23:00", "23:00");

