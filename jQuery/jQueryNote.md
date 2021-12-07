## function call
- 若在function後加上()，則function會立即執行
  - ex: 
  - test() : test這個function，會在網頁開啟時，就直接執行
  - test : test這個function，會在被呼叫時，才會執行

## Element Manipulation
```
<div id="msg"></div>
```
- $("#msg").append("append`<br>`");
  - 在文字欄位**加上**字串"append"，並換行(`<br>`)
- $("#msg").text("text`<br>`");
  - 將文字欄位的內容，**取代**為字串"text`<br>`"
- $("#msg").html("html`<br>`");
  - 將文字欄位的內容，**取代**為字串"html"，並換行`(<br>)`

## HTML font style:
- `<b></b>` : 粗體字
- `<I></I>` : 斜體字
- `<u></u>` : 加底線
- `<em></em>` : 強調文字
- `<spu></spu>`   : 文字上標
- `<sub></sub>`   : 文字下標
- `<font></font>` : 一般文字
- `<code></code>` : 原始碼字串
- `<strong></strong>` : 加強文字
