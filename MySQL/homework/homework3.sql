-- 1. 查詢所有食物名稱、產地編號、產地名稱和價格
SELECT f.fname 食物名稱, p.placeid 產地編號,
p.pname 產地名稱, f.price 價格
FROM food f JOIN place p
ON f.placeid = p.placeid;
-- 2. 查詢所有食物名稱和產地名稱，並串接成一個字串，中間以空白隔開，並將表頭重新命為'Food name & place'
SELECT (f.fname, ' ', p.pname) 'Food name & place'
FROM food f JOIN place p
ON f.placeid = p.placeid;
-- 3. 查詢所有'台灣'生產的食物名稱和價格
SELECT p.pname 產地名稱, f.fname 食物名稱, f.price 價格
FROM food f JOIN place p
ON p.placeid = f.placeid
WHERE p.pname='台灣'
-- 4. 查詢所有'台灣'和'日本'生產的食物名稱、產地名稱和價格，並以價格做降冪排序
SELECT p.pname 產地名稱, f.fname 食物名稱, f.price 價格
FROM food f JOIN place p
ON p.placeid = f.placeid
WHERE p.pname IN ('台灣', '日本')
ORDER BY f.price DESC;
-- 5. 查詢前三個價格最高且'台灣'生產的食物名稱、到期日和價格，並以價格做降冪排序
SELECT p.pname 產地名稱, f.fname 食物名稱, f.expiredate 到期日, f.price 價格
FROM food f JOIN place p
ON p.placeid = f.placeid
WHERE p.pname='台灣'
ORDER BY f.price DESC
LIMIT 3;
-- 6. 查詢每個產地(顯示產地名稱)最高、最低、加總和平均價格，表頭分別命名為'Max'、'Min'、'Sum'和'Avg'，結果皆以四捨五入的整數來顯示
SELECT p.pname 產地名稱, MAX(f.price) Max, MIN(f.price) Min,
SUM(f.price) Sum, ROUND(AVG(f.price)) Avg
FROM food f JOIN place p
ON p.placeid = f.placeid
GROUP BY p.pname;
-- 7. 查詢不同產地(顯示產地名稱)和每個種類的食物數量
SELECT p.pname 產地名稱, f.catalog 食物種類, COUNT(f.catalog) 種類數量
FROM food f JOIN place p
ON f.placeid = p.placeid
GROUP BY p.pname, catalog
ORDER BY p.pname;