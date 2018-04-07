# 臺東縣開放政府資料
- http://www.taitung.gov.tw/opendata/
- https://data.gov.tw/datasets/search?qs=dtid:22022+&order=pubdate

臺東縣開放資料在 2018.04.08 一共在自家平台上有 3574 筆，在國發會開放資料平台上則有 47 筆資料集。

# 資料目錄與清單
- http://www.taitung.gov.tw/opendata/OD_OpenData_Default.aspx?n=4A2DB40EB35F337E

資料目錄與清單可直接修改網頁上顯示資料數量來全部一次取得

完成 :
- 取得完整資料集清單 (2018.04.08) : 資料開放平台-資料目錄.csv
- 取得完整資料集 metadata (2018.04.08) : Datasets\


# 資料內容
平台上的資料內容取得是透過 js/post/form 方式來叫出另一個 popup 視窗，然後下載資料檔案 (.csv)

需求 : 
* 找人幫忙寫出資料內容的 scraper

# 資料優化
3574 筆資料集，如果將不同年份，月份，季的同名資料集整合一下，會只剩下 651
將這 651 依照資料發布的區分（一級，二級，最小統計區）合併，會只剩下 574
依照同一年的季別合併，會只剩下 481
將「鄉鎮市區」「村里」合併，最後只剩下 431

如果再依照資料名稱的相似度來做合併，例如：
臺東縣統計區第一款身障生活輔助統計, 10
臺東縣統計區第二款身障生活輔助統計, 10
臺東縣統計區第三款身障生活輔助統計, 10

那可能最後只剩下不到 300 筆資料集。從 3574 到 300 -
現有的資料不只在內容，查詢，檔案下載，使用都非常不方便也都需要對資料做進一步優化。

需求 :
- 找到人幫忙下載所有資料集
- 依照資料集名稱作合併與彙整
- 建立優化後資料目錄與內容

