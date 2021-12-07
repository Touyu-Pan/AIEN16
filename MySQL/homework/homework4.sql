-- 1. 查詢所有比'鳳梨酥'貴的食物名稱、到期日和價格
SELECT  fname 食物名稱, expiredate 到期日, price 價格
FROM    food
WHERE   price > (SELECT   price
                 FROM     food
                 WHERE    fname='鳳梨酥');
-- 2. 查詢所有比'曲奇餅乾'便宜且種類是'點心'的食物名稱、到期日和價格
SELECT  fname 食物名稱, expiredate 到期日, price 價格
FROM    food
WHERE   catalog='點心'
HAVING  price < (SELECT   price
                 FROM     food
                 WHERE    fname='曲奇餅乾');
-- 3. 查詢所有和'鳳梨酥'同一年到期的食物名稱、到期日和價格
SELECT  fname 食物名稱, expiredate 到期日, price 價格
FROM    food
WHERE   YEAR(expiredate) = (SELECT	YEAR(expiredate)
							FROM	food
                            WHERE	fname='鳳梨酥'
                            LIMIT	1);
-- 4. 查詢所有比平均價格高的食物名稱、到期日和價格
SELECT  fname 食物名稱, expiredate 到期日, price 價格
FROM    food
WHERE   price > (SELECT AVG(price)
				 FROM food);
-- 5. 查詢所有比平均價格低的'台灣'食物名稱、到期日和價格
SELECT  f.fname 食物名稱, f.expiredate 到期日, f.price 價格
FROM    food f JOIN place p
ON	f.placeid = p.placeid WHERE p.pname='台灣'
AND	f.price < (SELECT AVG(price)
			  FROM food);
-- 6. 查詢所有種類和'仙貝'相同且價格比'仙貝'便宜的食物名稱、到期日和價格
SELECT  fname 食物名稱, expiredate 到期日, price 價格
FROM    food
WHERE   catalog = (SELECT catalog
				   FROM food
				   WHERE fname='仙貝')
AND		price > (SELECT price
				 FROM food
				 WHERE fname='仙貝');
-- 7. 查詢所有產地和'仙貝'相同且過期超過1個月以上的食物名稱、到期日和價格
SELECT  f.fname 食物名稱, f.expiredate 到期日, f.price 價格
FROM    food f JOIN place p
ON	f.placeid = p.placeid
WHERE p.placeid = (SELECT placeid
				  FROM food
                  WHERE fname='仙貝')
AND	DATEDIFF(CURDATE(), f.expiredate) > (30);
select fname, expiredate, DATEDIFF(CURDATE(), expiredate)
from food;
-- 8. 查詢所有種類不是'點心'但比所有'點心'都貴的種類、食物名稱和價格，並以價格做降冪排序
SELECT  fname 食物名稱, expiredate 到期日, price 價格
FROM    food
WHERE	catalog != '點心'
AND		price > (SELECT MAX(price)
				FROM	food
                WHERE	catalog='點心')
ORDER BY price DESC;
-- 9. 查詢每個種類的食物數量的百分比，百分比以小數點一位四捨五入
SELECT	f.catalog, CONCAT(ROUND(COUNT(f.fname)/f1.cnt*100, 1), '%') Scale
FROM	food f
JOIN	(SELECT	COUNT(fname) cnt
		FROM food) f1
GROUP BY f.catalog;