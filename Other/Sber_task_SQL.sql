Вообще, мне ближе PostgreSQL диалект, но под рукой оказался только MySQL, поэтому тут нет CTE, FILTER и других
вспомогательных оперантов. Это тяжелее. Также обошёлся без оконных функций, хотя использую их. 

------------
Задача 1

Тут начинаем с подзапроса, который возвращает нам LIMIT 1 курс на последнюю дату date DESC, которая должна быть равна
(если транзакция произошла в рабочий день) или меньше даты транзакции (если транзакция произошла в выходной).
Затем просто делим на это на размер транзакции.
 
SELECT t.Client_id, t.Report_date,  ROUND(t.Txn_amount / (SELECT r.CCy_rate 
FROM Rates r
WHERE r.Report_date <= t.Report_date AND r.Ccy_code = 840
ORDER BY r.Report_date DESC
LIMIT 1), 2) AS txn_usd_amount
FROM transactions t;

-----------
Задача 2
Здесь джойнятся 2 таблицы. В первой мы достаём значения клиент, месяц, сумму дебитов, кредитов и дату последнего
посещения для каждого месяца. Во второй достаём клиента, номер ВСП,  дату репорта по условию нахождения даты 
репорта в подзапросе (списке) последней (MAX) даты посещения по месяцам для всех клиентов. Иннерджойним по
2м условиям: совпадение дат последнего посещени и id клиента.

SELECT q.Client_id, Report_date, Debit_amount, Credit_amount, VSP_Number
FROM (SELECT Client_id, MONTH(Report_date) AS Report_Date,
SUM(CASE WHEN Txn_type = 'debit' THEN Txn_amount ELSE 0 END) AS Debit_amount, 
SUM(CASE WHEN Txn_type = 'credit' THEN Txn_amount ELSE 0 END) AS Credit_amount, 
MAX(Report_date) AS Last_VSP
FROM VSP_oper_data
GROUP BY Client_id, MONTH(Report_date))q INNER JOIN 
(SELECT Client_id, VSP_Number, Report_date AS Last_VSP
FROM vsp_oper_data
WHERE Report_date IN (SELECT MAX(Report_date) FROM vsp_oper_data GROUP BY MONTH(Report_date)))s
ON q.Last_VSP = s.Last_VSP AND q.Client_id = s.Client_id
ORDER BY Client_id ASC;

----------
Задача 3
Инерджойним 2 таблицы. В одной группировка по клиентам, месяцам суммы транзакций с условием = дебит.
В другой группировка по месяцам общей суммы с условием = дебит. Джойним по месяцам, делим дебит
клиента на общий дебит по месяцам.

SELECT Client_id, Mnth AS Report_date, ROUND(Txn_month/Txn_month_am, 2) FROM
(SELECT Client_id, MONTH(Report_date) AS Mnth, SUM(Txn_amount) AS Txn_month
FROM vsp_oper_data
WHERE Txn_type = 'debit'
GROUP BY Client_id, MONTH(Report_date))q INNER JOIN 
(SELECT MONTH(Report_date) AS Mnth, SUM(Txn_amount) AS Txn_month_am
FROM vsp_oper_data
WHERE Txn_type = 'debit' GROUP BY MONTH(Report_date))s USING(Mnth); 
