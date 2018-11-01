-- Создание таблицы с настройками челенджей
-- @name: название челенджа,
-- @status:  0 - не активен, 1 - активен
-- @cost - стоимсоть штрафа
-- @time -  дата последней активации. format: YYYY-MM-DD HH:MM:SS.SSS
CREATE TABLE challenges (
	id INTEGER PRIMARY KEY NOT NULL,
	name TEXT NOT NULL,
	status INTEGER NOT NULL,
	cost INTEGER NOT NULL,
	fail_time TEXT NOT NULL,
	last_update_time TEXT NOT NULL
);

-- Заполнение БД
INSERT INTO challenges(id, name, status, cost, time)
VALUES (1, "Ограничение ночного холодильника", 1, 100, "23:00:00", "2018-11-01 23:00:05.123");

INSERT INTO challenges(id, name, status, cost, time)
VALUES (2, "Контроль потребления электричества", 0, 100, "01:00:00", "2018-11-01 23:00:05.123");