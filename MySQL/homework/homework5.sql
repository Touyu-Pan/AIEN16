-- 1. 以不列舉欄位的方式新增一筆食物資料
INSERT INTO food
VALUES ('DK004', '可樂', '2022/12/02', 'TW', 39, '飲料');
-- 2. 以列舉欄位的方式新增一筆食物資料
INSERT INTO food(foodid, fname, expiredate, placeid, price)
VALUES ('DK005', '百事可樂', '2022/12/02', 'TW', 39);
-- 3. 以不列舉欄位的方式新增多產地資料
INSERT INTO place
VALUES ('TT', '踢踢'), ('PP', '批批');
-- 4. 修改一筆食物資料的價格
UPDATE food
SET price=49, catalog='飲料'
WHERE foodid='DK005';
-- 5. 按價格分250以下、251~500和501以上三種分別增加8%,5%和3%且價格無條件捨去成整數
-- 6. 刪除一筆食物資料
DELETE FROM food
WHERE foodid='DK005';