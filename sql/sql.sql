-- Создание таблицы с настройками челенджей
-- @name: название челенджа,
-- @status:  0 - не активен, 1 - активен
-- @cost - стоимсоть штрафа
-- @time -  дата последней активации. format: HH:MM:SS
CREATE TABLE challenges (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    status INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    fail_time TEXT NOT NULL,
    last_update_time TEXT NOT NULL
);

-- Заполнение БД
INSERT INTO challenges(id, name, status, cost, fail_time, last_update_time)
VALUES (1, "Контроль потребления электричества", 0, 100, "01:00", "23:00");

INSERT INTO challenges(id, name, status, cost, fail_time, last_update_time)
VALUES (2, "Ограничение ночного холодильника", 1, 100, "23:00", "23:00");

