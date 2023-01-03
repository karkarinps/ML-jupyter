/* вывести название, авторов, жанр, цену и кол-во книг написанных в самом популярном жанр(e)/ах */
/* 6. Выводим нужные столбцы, объединяя информацию по ключевым столбцам из разных таблиц */
SELECT title, name_author, name_genre, price, amount
FROM genre g INNER JOIN book b ON g.genre_id = b.genre_id
     INNER JOIN author a ON a.author_id = b.author_id
WHERE g.genre_id IN ( /* 7. Задаём условие, по которому будут выводится данные (жанр должен совпадать с жанром из предыдущих запросов (самым популярным)) */
/* 3. Объединяем значения из двух запросов, выводя самый популярный жанр(ы). */
    SELECT q1.genre_id
FROM
/* 1. Выводим жанры и общее количество книг, написанных в этих жанрах */
    (SELECT genre_id, SUM(amount) AS amount FROM book GROUP BY genre_id)q1
INNER JOIN /* 4. джойним все значения из запросов */
/* 2. Выводим самый поппулярный жанр (изменяем порядок запроса 1 по снижению числа книг, написанных в жарнрах и ставим ограничение на показ первого -
 самого популярного, который имеет наибольшее число написаных книг) */
    (SELECT genre_id, SUM(amount) AS amount FROM book GROUP BY genre_id ORDER BY amount DESC LIMIT 1)q2
ON q1.amount = q2.amount) /* 5. общий стобец - количество книг. Нам нужны только те жанры, количество книг которых совпадает в обоих запросах (то есть максимально, 
исходя из второго запроса с LIMIT 1 по убыванию числа книг в жанре) */
ORDER BY title ASC; /* 8. Изменяем порядок вывода по названию в алфавитном порядке */

/* Вывести данные для тех книг, названия и цена которых одинаковы в таблицах supply и book */
SELECT b.title AS Название, name_author AS Автор, (b.amount+s.amount) AS Количество /* 1. Выводим столбцы под нужными именами, складываем колв-во из 2х таблиц */
FROM book b INNER JOIN author a /* 2. соединяем первую пару таблиц (чтобы получить имена авторов вместо id) */
USING (author_id)/* 3. соединение по стобцам author_id обеих таблиц */
INNER JOIN supply s /* 4. соединяем предыдущую пару с третьей таблицей supply */
ON s.title=b.title and s.price=b.price /* 5. соединяем по столбцам название и цена, которые должны быть одинаковы, чтобы попасть в итоговую таблицу */


SELECT bb.buy_id, name_client, SUM(bb.amount*b.price) AS Стоимость
FROM book b INNER JOIN buy_book bb ON b.book_id=bb.book_id
INNER JOIN buy ON buy.buy_id=bb.buy_id
INNER JOIN client c ON c.client_id=buy.client_id
GROUP BY buy_id
ORDER BY buy_id ASC;


UPDATE book
SET genre_id = (SELECT genre_id FROM genre WHERE name_genre = 'Поэзия')
WHERE book_id = 10;


UPDATE book
SET genre_id = (SELECT genre_id FROM genre WHERE name_genre = 'Приключения')
WHERE book_id = 11;
 

DELETE FROM author
WHERE author_id IN (SELECT author_id FROM book GROUP BY author_id HAVING SUM(amount) < 20);
 
 
DELETE FROM author
USING author INNER JOIN book ON author.author_id=book.author_id
WHERE book.author_id IN (SELECT author_id FROM book INNER JOIN genre ON book.genre_id=genre.genre_id WHERE name_genre =
                  'Поэзия');
 
SELECT * FROM book;
 
 
SELECT buy.buy_id, b.title, b.price, bb.amount
FROM book b INNER JOIN buy_book  bb ON b.book_id = bb.book_id
INNER JOIN buy ON buy.buy_id = bb.buy_id
INNER JOIN client c ON c.client_id = buy.client_id
WHERE name_client = 'Баранов Павел'
ORDER BY buy_id ASC, title ASC;
 
 
SELECT a.name_author, b.title, COUNT(bb.amount) AS Количество
FROM author a INNER JOIN book b ON a.author_id = b.author_id
LEFT JOIN buy_book bb ON b.book_id = bb.book_id
GROUP BY name_author, title
ORDER BY name_author ASC, title ASC;
 

SELECT c.name_city, COUNT(buy.client_id) AS Количество
FROM buy RIGHT JOIN client cl ON buy.client_id = cl.client_id
INNER JOIN city c ON c.city_id = cl.city_id
GROUP BY c.name_city
ORDER BY Количество DESC, name_city ASC;


SELECT title, SUM(Количество) AS Количество, SUM(Сумма) AS Сумма
FROM
(SELECT title, SUM(bb.amount) AS Количество, SUM(b.price*bb.amount) AS Сумма
FROM book b INNER JOIN buy_book bb USING(book_id)
INNER JOIN buy_step bs USING(buy_id)
WHERE step_id=1 AND date_step_end IS NOT NULL
GROUP BY title
UNION ALL
SELECT title, SUM(ba.amount) AS Количество, SUM(ba.price*ba.amount) AS Сумма
FROM buy_archive ba INNER JOIN book b USING(book_id)
GROUP BY title)query_in
GROUP BY title
ORDER BY Сумма DESC;
 
 
SELECT YEAR(date_step_end) AS Год, MONTHNAME(date_step_end) AS Месяц, SUM(b.price*bb.amount) AS Сумма
FROM book b INNER JOIN buy_book bb USING(book_id)
INNER JOIN buy USING(buy_id)
INNER JOIN buy_step bs USING(buy_id)
INNER JOIN step s USING(step_id)
WHERE step_id = 1 AND date_step_end IS NOT NULL
GROUP BY MONTHNAME(date_step_end), YEAR(date_step_end)
UNION
SELECT YEAR(date_payment) AS Год, MONTHNAME(date_payment) AS Месяц, SUM(ba.price*ba.amount) AS Сумма
FROM buy_archive ba
GROUP BY MONTHNAME(date_payment), YEAR(date_payment)
ORDER BY Месяц ASC, Год ASC;
 

SELECT name_genre, SUM(bb.amount) AS Количество
FROM genre g INNER JOIN book b ON g.genre_id=b.genre_id
INNER JOIN buy_book bb ON b.book_id=bb.book_id
GROUP BY name_genre
HAVING SUM(bb.amount) IN (SELECT MAX(Количество) FROM (SELECT SUM(bb.amount) AS Количество FROM genre g INNER JOIN book b ON g.genre_id=b.genre_id
INNER JOIN buy_book bb ON b.book_id=bb.book_id GROUP BY name_genre)query_in);



UPDATE buy_step
SET date_step_end = '2020-04-13'
WHERE buy_id = 5 and step_id = 1;
 
UPDATE buy_step
SET date_step_beg = '2020-04-13'
WHERE buy_id = 5 and step_id = (SELECT step_id + 1
FROM step
WHERE name_step = 'Оплата');
 
 
INSERT INTO buy_step(buy_id, step_id)
SELECT buy_id, step_id
FROM step s CROSS JOIN buy b
WHERE buy_id = 5;



SELECT name_student, date_attempt, result
FROM attempt a INNER JOIN student USING(student_id)
INNER JOIN subject ns USING(subject_id)
WHERE name_subject = 'Основы баз данных'
ORDER BY result DESC;
 
 
SELECT name_subject, COUNT(a.subject_id) AS Количество, ROUND(AVG(result), 2) AS Среднее
FROM attempt a RIGHT JOIN subject s USING(subject_id)
GROUP BY name_subject
ORDER BY Среднее DESC;


SELECT name_student, name_subject, date_attempt, ROUND((SUM(answer.is_correct)/3)*100, 2) AS Результат
FROM attempt JOIN student USING(student_id)
JOIN subject USING(subject_id)
JOIN testing USING(attempt_id)
JOIN answer USING(answer_id)
GROUP BY name_student, name_subject, date_attempt
ORDER BY name_student ASC, date_attempt DESC;
 
SELECT name_question, name_answer, IF(is_correct = 0, 'Неверно', 'Верно') AS Результат
FROM question q INNER JOIN answer a USING(question_id)
INNER JOIN testing t USING(answer_id)
WHERE attempt_id = 7;
 
 
SELECT question_id, name_question
FROM question q INNER JOIN subject s USING(subject_id)
WHERE name_subject = 'Основы баз данных'
ORDER BY RAND()
LIMIT 3;
 
SELECT name_subject, COUNT(DISTINCT student_id) AS Количество
FROM attempt a RIGHT JOIN subject s USING(subject_id)
GROUP BY subject_id
ORDER BY Количество DESC, name_subject;


UPDATE attempt
SET result = (SELECT ROUND((SUM(answer.is_correct)/3)*100, 2) AS Результат
FROM testing
    JOIN answer USING(answer_id)
             WHERE attempt_id = 8)
WHERE attempt_id = 8;
 

INSERT INTO testing(attempt_id, question_id)
SELECT attempt_id, question_id
FROM attempt a INNER JOIN question q USING(subject_id)
WHERE attempt_id = (SELECT MAX(attempt_id) FROM attempt)
ORDER BY RAND()
LIMIT 3;


SELECT name_program, name_enrollee, SUM(result) AS itog
FROM enrollee INNER JOIN program_enrollee USING(enrollee_id)
INNER JOIN program USING(program_id)
INNER JOIN program_subject USING(program_id)
INNER JOIN subject USING(subject_id)
INNER JOIN enrollee_subject ON subject.subject_id = enrollee_subject.subject_id
AND enrollee_subject.enrollee_id = enrollee.enrollee_id
GROUP BY name_program, name_enrollee
ORDER BY name_program ASC, itog DESC;
 
 
SELECT name_program
FROM (SELECT name_program, COUNT(name_subject) AS Количество
FROM program p INNER JOIN program_subject ps USING(program_id)
INNER JOIN subject s USING(subject_id)
WHERE name_subject IN ('Информатика', 'Математика')
GROUP BY name_program, name_subject)query_in
GROUP BY name_program
HAVING COUNT(Количество) = 2
ORDER BY name_program ASC;
 
 
SELECT name_department, name_program, plan, COUNT(program_id) AS Количество, ROUND(COUNT(program_id)/plan, 2) AS Конкурс
FROM program_enrollee pe INNER JOIN program p USING(program_id)
INNER JOIN department d USING(department_id)
GROUP BY name_department, name_program, plan
ORDER BY Конкурс DESC;
 
 
SELECT name_enrollee, IF(SUM(bonus) IS NULL, 0, SUM(bonus)) AS Бонус  
FROM enrollee e LEFT JOIN enrollee_achievement ea USING(enrollee_id)
LEFT JOIN achievement a USING(achievement_id)
GROUP BY name_enrollee
ORDER BY name_enrollee ASC;
 
 
SELECT name_program
FROM program_subject ps INNER JOIN program p USING(program_id)
GROUP BY name_program
HAVING MIN(min_result)>=40
ORDER BY name_program ASC;
 
 
SELECT name_subject, COUNT(subject_id) AS Количество, MAX(result) AS Максимум,
MIN(result) AS Минимум, ROUND(AVG(result), 1) AS Среднее
FROM subject s INNER JOIN enrollee_subject USING(subject_id)
GROUP BY name_subject
ORDER BY name_subject ASC;
 
 
SELECT name_program
FROM program p INNER JOIN program_subject ps USING(program_id)
INNER JOIN subject s USING(subject_id)
WHERE name_subject = 'Информатика'
ORDER BY name_program DESC;
 
 
SELECT name_enrollee
FROM program p INNER JOIN program_enrollee pe USING(program_id)
INNER JOIN enrollee e USING(enrollee_id)
WHERE name_program = 'Мехатроника и робототехника'
ORDER BY name_enrollee ASC;


SELECT DISTINCT(name_program), name_enrollee
FROM enrollee INNER JOIN program_enrollee USING(enrollee_id)
INNER JOIN program USING(program_id)
INNER JOIN program_subject USING(program_id)
INNER JOIN subject USING(subject_id)
INNER JOIN enrollee_subject ON subject.subject_id = enrollee_subject.subject_id
AND enrollee_subject.enrollee_id = enrollee.enrollee_id
WHERE result<min_result
ORDER BY name_program, name_enrollee;
----
CREATE TABLE applicant AS
SELECT pe.program_id, es.enrollee_id, SUM(result) AS itog
FROM enrollee INNER JOIN program_enrollee pe USING(enrollee_id)
INNER JOIN program USING(program_id)
INNER JOIN program_subject USING(program_id)
INNER JOIN subject USING(subject_id)
INNER JOIN enrollee_subject es ON subject.subject_id = es.subject_id
AND es.enrollee_id = enrollee.enrollee_id
GROUP BY program_id, enrollee_id
ORDER BY program_id, itog DESC;
 
SELECT * FROM applicant
 
---
DELETE FROM applicant
WHERE (program_id, enrollee_id) IN (SELECT p.program_id, e.enrollee_id
FROM enrollee e INNER JOIN program_enrollee USING(enrollee_id)
INNER JOIN program p USING(program_id)
INNER JOIN program_subject USING(program_id)
INNER JOIN subject USING(subject_id)
INNER JOIN enrollee_subject ON subject.subject_id = enrollee_subject.subject_id
AND enrollee_subject.enrollee_id = e.enrollee_id
WHERE result<min_result);
 
SELECT * FROM applicant
 
--
UPDATE applicant
JOIN
(SELECT enrollee_id, SUM(bonus) AS Бонус  
FROM enrollee_achievement ea
LEFT JOIN achievement a USING(achievement_id)
GROUP BY enrollee_id)query_in USING(enrollee_id)
SET itog = itog + Бонус;
 
SELECT * FROM applicant
 
--
CREATE TABLE applicant_order AS
SELECT * FROM applicant
ORDER BY program_id, itog DESC;
 
DROP TABLE applicant
 
--
 
ALTER TABLE applicant_order ADD str_id NUMERIC FIRST;
 
SELECT * FROM applicant_order
 
--
SET @counter := 1;
SET @id_pr_counter := 0;
 
UPDATE applicant_order
SET str_id = IF(program_id = @id_pr_counter, @counter := @counter + 1, @counter := 1 AND @id_pr_counter := @id_pr_counter + 1);
 
SELECT * FROM applicant_order
 
--
CREATE TABLE student AS
SELECT name_program, name_enrollee, itog
FROM program p INNER JOIN applicant_order ao USING(program_id)
INNER JOIN enrollee e USING(enrollee_id)
WHERE str_id <= plan
ORDER BY name_program ASC, itog DESC;


SELECT product_id, name, price,
CASE
WHEN name IN ('сахар', 'сухарики', 'сушки', 'семечки',
'масло льняное', 'виноград', 'масло оливковое',
'арбуз', 'батон', 'йогурт', 'сливки', 'гречка',
'овсянка', 'макароны', 'баранина', 'апельсины',
'бублики', 'хлеб', 'горох', 'сметана', 'рыба копченая',
'мука', 'шпроты', 'сосиски', 'свинина', 'рис',
'масло кунжутное', 'сгущенка', 'ананас', 'говядина',
'соль', 'рыба вяленая', 'масло подсолнечное', 'яблоки',
'груши', 'лепешка', 'молоко', 'курица', 'лаваш', 'вафли', 'мандарины') THEN ROUND((price * 10 / 110), 2)
ELSE ROUND((price * 20 / 120), 2)
END AS tax
, CASE
WHEN name IN ('сахар', 'сухарики', 'сушки', 'семечки',
'масло льняное', 'виноград', 'масло оливковое',
'арбуз', 'батон', 'йогурт', 'сливки', 'гречка',
'овсянка', 'макароны', 'баранина', 'апельсины',
'бублики', 'хлеб', 'горох', 'сметана', 'рыба копченая',
'мука', 'шпроты', 'сосиски', 'свинина', 'рис',
'масло кунжутное', 'сгущенка', 'ананас', 'говядина',
'соль', 'рыба вяленая', 'масло подсолнечное', 'яблоки',
'груши', 'лепешка', 'молоко', 'курица', 'лаваш', 'вафли', 'мандарины') THEN ROUND((price - (price * 10 / 110)), 2)
ELSE ROUND((price - (price * 20 / 120)), 2)
END AS price_before_tax
FROM products
ORDER BY price_before_tax DESC;
 
SELECT COUNT(order_id) AS orders_count
FROM orders
WHERE array_length(product_ids, 1) >= 9;
 
 
SELECT ROUND(AVG(price), 2) AS avg_price
FROM products
WHERE (name NOT LIKE '%иван-чай%' AND name NOT LIKE '%чайный гриб%') AND (name LIKE '%чай%' OR name LIKE '%кофе%')


SELECT SUM(CASE
WHEN name = 'сухарики' THEN 3*price
WHEN name = 'чипсы' THEN 2*price
WHEN name = 'энергетический напиток' THEN 1*price
END) AS order_price
FROM products
 
 
SELECT (COUNT(DISTINCT user_id) FILTER (WHERE action = 'create_order') - COUNT(DISTINCT user_id) FILTER
(WHERE action = 'cancel_order')) AS users_count
FROM user_actions
 
 
SELECT sex, COUNT(DISTINCT courier_id) AS couriers_count
FROM couriers
GROUP BY sex
ORDER BY couriers_count ASC;
 
 
SELECT DATE_PART('year', AGE(current_date, birth_date)) AS age, COUNT(DISTINCT user_id) AS users_count, sex
FROM users
WHERE birth_date IS NOT NULL
GROUP BY age, sex
ORDER BY age ASC;


SELECT DATE_PART('year', AGE(current_date, birth_date)) AS age, sex, COUNT(DISTINCT user_id) AS users_count
FROM users
WHERE birth_date IS NOT NULL
GROUP BY age, sex
ORDER BY age ASC;
 
SELECT DATE_TRUNC('month', time) AS month, action, COUNT(order_id) AS orders_count
FROM user_actions
GROUP BY month, action
ORDER BY month, action;
 
SELECT array_length(product_ids, 1) AS order_size, COUNT(order_id) AS orders_count
FROM orders
GROUP BY order_size
HAVING COUNT(order_id) > 5000
ORDER BY order_size ASC;
 
SELECT courier_id, COUNT(order_id) AS delivered_orders
FROM courier_actions
WHERE DATE_PART('month', time) = 9 AND DATE_PART('year', time) = 2022
AND action = 'deliver_order'
GROUP BY courier_id
ORDER BY delivered_orders DESC
LIMIT 5;
 
SELECT courier_id, COUNT(order_id) AS delivered_orders
FROM courier_actions
WHERE DATE_PART('month', time) = 9 AND DATE_PART('year', time) = 2022
AND action = 'deliver_order'
GROUP BY courier_id
HAVING COUNT(order_id) = 1;
 
SELECT user_id
FROM user_actions
WHERE action = 'create_order'
GROUP BY user_id
HAVING DATE_PART('month', MAX(time)) < 9 AND DATE_PART('year', MAX(time)) = 2022
ORDER BY user_id ASC;
 
SELECT user_id, ROUND(COUNT(action) FILTER (WHERE action = 'cancel_order')/CAST(COUNT(DISTINCT user_id) AS DECIMAL), 2) AS cancel_rate
FROM user_actions
GROUP BY user_id
ORDER BY cancel_rate DESC;
 
SELECT CASE
WHEN DATE_PART('year', AGE(current_date, birth_date)) BETWEEN 19 AND 24 THEN '19-24'
WHEN DATE_PART('year', AGE(current_date, birth_date)) BETWEEN 25 AND 29 THEN '25-29'
WHEN DATE_PART('year', AGE(current_date, birth_date)) BETWEEN 30 AND 35 THEN '30-35'
WHEN DATE_PART('year', AGE(current_date, birth_date)) BETWEEN 36 AND 41 THEN '36-41'
END AS group_age, COUNT(DISTINCT user_id) AS users_count
FROM users
WHERE DATE_PART('year', AGE(current_date, birth_date)) BETWEEN 19 AND 41
GROUP BY group_age
ORDER BY group_age ASC;

/* ТЕСТОВОЕ ДАТА-АНАЛИТИК */
SELECT Vendor 
FROM T1 
UNION SELECT Vendor 
FROM T2;


SELECT * FROM BOOKS WHERE PUBLISHER IN (‘Мысль’, ‘Азбука’);
SELECT * FROM BOOKS WHERE PUBLISHER =‘Мысль’ or PUBLISHER = ‘Азбука’;
SELECT * FROM BOOKS WHERE PUBLISHER =‘Мысль’ UNION select * from BOOKS where PUBLISHER = ‘Азбука’;


WITH subq AS (SELECT NUM 
FROM T2)
SELECT DISTINCT NUM
FROM T1
WHERE NUM NOT IN (SELECT * FROM subq);


SELECT DISTINCT T1.NUM
FROM T1 LEFT JOIN 
T2 ON T1.NUM = T2.NUM
WHERE T2.NUM IS NULL;


WITH CTE AS
(SELECT *,ROW_NUMBER() OVER (PARTITION BY NUM ORDER BY NUM) AS RN
FROM T)
DELETE FROM CTE WHERE RN<>1;


WITH CTE AS (SELECT Fil, SUM(Sales) AS Sales, SUM(Plan, %) AS Plan
FROM T1
GROUP BY Fil
ORDER BY Plan DESC
LIMIT 3)
SELECT *, ROW_NUMBER() OVER (ORDER BY Plan DESC) AS Place
FROM CTE;


WITH CTE AS (SELECT Department, COUNT(id) AS cnt_id 
FROM Employees GROUP BY Department)
SELECT Department FROM CTE 
WHERE cnt_id IN ((SELECT MAX(cnt_id) FROM CTE), (SELECT MAX(cnt_id) FROM CTE));


SELECT DATE_PART(‘month’, Date::DATE) AS Months, SUM(Salary) AS Month_salary
FROM Salary
GROUP BY Months
ORDER BY Months DESC;


SELECT DISTINCT CASE WHEN Salary < 50000 THEN FullName END AS Less50,
CASE WHEN Salary > 50000 THEN FullName END AS More50
FROM Salary s INNER JOIN Employees e ON s.Employeeid = e.id;


RENAME TABLE Employees TO Workers;
ALTER TABLE Workers ADD Comment nvarchar(255) NULL;


SELECT Employeeid, ROW_NUMBER() OVER (ORDER BY Salary DESC) AS seq_num 
FROM Salary
WHERE DATE_PART(‘month’, Date::DATE) = 4







