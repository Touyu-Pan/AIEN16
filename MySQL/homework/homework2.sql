-- INSERT INTO food VALUES ('CK001', '曲奇餅乾', '2022/01/10', 'TH', 250, '點心');
-- INSERT INTO food VALUES ('CK002', '蘇打餅乾', '2021/10/12', 'TW', 80, '點心');
-- INSERT INTO food VALUES ('DK001', '高山茶', '2022/05/23', 'TW', 780, '飲料');
-- INSERT INTO food VALUES ('DK002', '綠茶', '2021/06/11', 'JP', 530, '飲料');
-- INSERT INTO food VALUES ('OL001', '苦茶油', '2023/03/16', 'TW', 360, '調味品');
-- INSERT INTO food VALUES ('OL002', '橄欖油', '2022/07/25', 'TH', 420, '調味品');
-- INSERT INTO food VALUES ('CK003', '仙貝', '2021/11/01', 'JP', 270, '點心');
-- INSERT INTO food VALUES ('SG001', '醬油', '2023/05/05', 'JP', 260, '調味品');
-- INSERT INTO food VALUES ('OL003', '葡萄子油', '2023/05/05', 'JP', 550, '調味品');
-- INSERT INTO food VALUES ('CK004', '鳳梨酥', '2021/04/12', 'TW', 340, '點心');
-- INSERT INTO food VALUES ('CK005', '太陽餅', '2021/08/27', 'TW', 150, '點心');
-- INSERT INTO food VALUES ('DK003', '紅茶', '2023/11/12', 'TH', 260, '飲料');
-- INSERT INTO food VALUES ('SG002', '醋', '2022/09/18', 'TW', 60, '調味品');

-- INSERT INTO place VALUES ('TW', '台灣');
-- INSERT INTO place VALUES ('JP', '日本');
-- INSERT INTO place VALUES ('TH', '泰國');
-- INSERT INTO place VALUES ('US', '美國');

-- 1. 查詢所有食物表格中所有欄位的資料
-- 2. 查詢所有食物名稱、到期日和價格
-- 3. 查詢所有食物名稱、到期日和價格，並將表頭重新命為'名稱'、'到期日'和'價格'
-- 4. 查詢所有食物的種類有哪些？(重覆的資料只顯示一次)
SELECT COUNT(DISTINCT catalog) FROM food;
-- 5. 查詢所有食物名稱和種類，並串接成一個字串，中間以空白隔開，並將表頭重新命為'Food name & catalog'
SELECT CONCAT(fname, ' ', catalog) 'Food name & catalog'
FROM food;
-- -- WHERE子句
-- 6. 查詢所有食物價格超過400的食物名稱和價格
SELECT fname, price
FROM food
WHERE price > 400;
-- 7. 查詢所有食物價格介於250~530之間的食物名稱和價格
SELECT fname, price
FROM food
WHERE price BETWEEN 250 AND 530;
-- 8. 查詢所有食物價格不介於250~530之間的食物名稱和價格
SELECT fname, price
FROM food
WHERE price NOT BETWEEN 250 AND 530;
-- 9. 查詢所有食物種類為'點心'的食物名稱和價格
SELECT fname, price
FROM food
WHERE catalog = '點心';
-- 10. 查詢所有食物種類為'點心'和'飲料'的食物名稱、價格和種類
SELECT fname, price
FROM food
WHERE catalog IN ('點心', '飲料');
-- 11. 查詢所有食物產地為'TW'和'JP'的食物名稱、價格和產地編號
SELECT fname, price, placeid
FROM food
WHERE placeid IN ('TW', 'JP');
-- 12. 查詢所有食物名稱有'油'字的食物名稱、到期日和價格
SELECT fname, price, placeid
FROM food
WHERE fname LIKE '%油%';
-- 13. 查詢所有食物未過期且到期日在今年底以前到期的食物名稱、到期日和價格
SELECT fname, expiredate, price
FROM food
WHERE expiredate BETWEEN CURDATE() AND '2021/12/31';
-- 14. 查詢所有食物未過期且到期日在明年6月底以前到期的食物名稱、到期日和價格
SELECT fname, expiredate, price
FROM food
WHERE expiredate BETWEEN CURDATE() AND '2022/06/30';
-- 15. 查詢所有食物未過期且6個月內到期的食物名稱、到期日和價格
SELECT fname, expiredate, price
FROM food
WHERE expiredate
BETWEEN CURDATE() AND ADDDATE(CURDATE(), interval 6 month);

-- -- ORDER BY子句
-- 16. 查詢所有食物名稱、到期日和價格，並以價格做降冪排序
SELECT fname, expiredate, price
FROM food
ORDER BY expiredate DESC;
-- 17. 查詢前三個價格最高的食物名稱、到期日和價格，並以價格做降冪排序
SELECT fname, expiredate, price
FROM food
ORDER BY expiredate DESC
LIMIT 3;
-- 18. 查詢種類為'點心'且價格低於等於250的食物名稱和價格，並以價格做升冪排序
SELECT fname, expiredate, price
FROM food
WHERE catalog = '點心' AND price < 250
ORDER BY price;
-- 19. 顯示所有食物名稱、價格和增加5%且四捨五入為整數後的價格，新價格並將表頭命名為'New Price'
SELECT fname, price, ROUND(price*1.05) 'New Price'
FROM food
ORDER BY price;
-- 20. 接續上題，再增加一個表頭命名為'Increase'，顯示New price減去price的值
SELECT fname, price, ROUND(price*1.05) 'New Price',
(ROUND(price*1.05) - price) Increase
FROM food
ORDER BY price;
-- 21. 顯示所有食物名稱、價格和整數後的價格，新價格並將表頭命名為'New Price'；按價格分250以下、251~500和501以上三種分別增加8%,5%和3%且價格無條件捨去成整數
SELECT fname, price,
  CASE
    WHEN price <= 250 THEN FLOOR(price*(1.08))
    WHEN price BETWEEN 251 AND 500 THEN FLOOR(price*(1.05))
    ELSE FLOOR(price*(1.03))
  END 'New Price'
FROM food;
-- 22. 查詢所有食物名稱、到期日、距離今天尚有幾天到期(正數表示)或已過期幾天(負數表示)和註記(有'已過期'或'未過期'兩種)，並將後兩者表頭分別命名為'Days of expired'和'expired or not'
SELECT fname, expiredate,
DATEDIFF(CURDATE(), expiredate) 'Days of expired',
IF(DATEDIFF(CURDATE(), expiredate) > 0, 'not', 'expired') 'expired or not'
FROM food;
-- 23. 接續上題，並以過期天數做升冪排序
SELECT fname, expiredate,
DATEDIFF(CURDATE(), expiredate) 'Days of expired',
IF(DATEDIFF(CURDATE(), expiredate) > 0, 'not', 'expired') 'expired or not'
FROM food
ORDER BY DATEDIFF(CURDATE(), expiredate);

-- -- GROUP BY & HAVING子句
-- 24. 查詢所有食物最高、最低、加總和平均價格，表頭分別命名為'Max'、'Min'、'Sum'和'Avg'，結果皆以四捨五入的整數來顯示
SELECT MAX(price) Max, MIN(price) Min,
  SUM(price) Sum, ROUND(AVG(price)) Avg
FROM food;
-- 25. 接續上題，查詢每個種類
SELECT catalog 種類, MAX(price) Max, MIN(price) Min,
  SUM(price) Sum, ROUND(AVG(price)) Avg
FROM food
GROUP BY catalog;
-- 26. 接續上題，查詢每個種類且平均價格超過300，並以平均價格做降冪排序
SELECT catalog 種類, MAX(price) Max, MIN(price) Min,
  SUM(price) Sum, ROUND(AVG(price)) Avg
FROM food
GROUP BY catalog
HAVING ROUND(AVG(price))>300
ORDER BY ROUND(AVG(price))>300 DESC;
-- 27. 顯示查詢每個種類的食物數量
SELECT catalog 種類, count(fname) 種類數量
FROM food
GROUP BY catalog;
-- 28. 查詢不同產地和每個種類的食物數量
SELECT placeid 產地, catalog 種類, COUNT(catalog) 種類數量
FROM food
GROUP BY placeid, catalog
ORDER BY placeid;