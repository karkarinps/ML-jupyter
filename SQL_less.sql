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