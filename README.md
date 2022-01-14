<h1 align="center">
  <br>
  [指定專題作品] 外匯資料的即時擷取 (網路爬蟲應用1)
</h1>


## 目錄
* [摘要](#摘要)
* [重點說明](#重點說明)
* [系統環境](#系統環境)
* [聯絡資料](#聯絡資料)
* [致謝](#致謝)
* [權限](#權限)


## 摘要 (本作品含 網路爬蟲技術 (urllib.request/bs4)，可自動擷取目前臺灣銀行的即時外匯資料。)
### 1. 使用網路爬蟲技術 (urllib.request/bs4)，自動抓取目前臺灣銀行的外匯資料。
### 2. 使用者輸入欲兌換的 (1)臺幣金額 與 (2)貨幣種類，即可計算出兌換後的該貨幣金額。

  ![conversion_images](images/conversion.gif)

<strong><em>若您有興趣想更了解此程式，請參考下方的聯絡方式，進一步聯絡作者，謝謝參閱。</em></strong>


## 重點說明
### 1. 使用網路爬蟲技術 (urllib.request/bs4)，自動抓取目前臺灣銀行的外匯資料。
  
* 於臺灣銀行外匯網頁，檢視網頁的程式碼，找到需要擷取的類別資料，放入`find_all()`函式內
* 外匯相關資料，請參考臺灣銀行網站：https://rate.bot.com.tw/xrt?Lang=zh-TW
  ```python
  html_page = urllib.request.urlopen(url)
  sp = BeautifulSoup(html_page, 'html.parser')
  row_with_currency_names = sp.find_all(貨幣)
  cash_rates = sp.find_all(匯率)
  ```
  
* 從爬蟲獲取的外匯資料中，擷取需要的貨幣名稱和匯率
  ```python
  for index in range(len(row_with_currency_names)):
    for key in currency_rates:
      if key in row_with_currency_names[index].text:
        currency_rates[key] = float(cash_rates[index * 2 + 1].string)
  ```
  
### 2. 使用者輸入欲兌換的 (1)臺幣金額 與 (2)貨幣種類，即可計算出兌換後的該貨幣金額。
#### 使用 while 迴圈達到循環輸入，並於迴圈內部，設立 3 個節點，目的：使用過程中如果使用者輸入錯誤，提示輸入錯誤，請再輸入一次；如果輸入正確，則前往下個節點，直到計算出結果，並回到第一個節點。
* 第 1 個節點：檢查使用者輸入欲兌換的新臺幣金額
  ```python
  while True:
    # 設立第 1 個節點
    if check_point == 1:
      input_NTD = input('提示使用者輸入臺幣')

      if counter > 1:
        # 判斷：若使用者輸入 Q 或 q 字元，則退出程式
        if input_NTD.lower() == 'q':
          print('提示使用者即將退出程式')
          break

      # 使用者輸入僅限為整數或浮點數
      try: input_NTD = float(input_NTD) 
      except: 
        print('提示使用者輸入錯誤') 
        continue

      # 判斷：若使用者輸入的金額小於零，則顯示輸入錯誤
      if (0 > input_NTD):
        print('提示使用者輸入錯誤')
        continue
      
      # 若以上皆輸入正確，則前往下個節點
      check_point = 2
  ```

* 第 2 個節點：檢查使用者輸入欲兌換的貨幣
  ```python
  elif check_point == 2:
    # 使用者輸入貨幣名稱
    input_currency = input()

    # 使用者輸入僅限為整數
    try: input_currency = int(input_currency)
    except:
      print('提示使用者輸入錯誤')
      continue

    # 判斷：若使用者輸入的貨幣名稱不在設定範圍內，則顯示輸入錯誤
    if not (1 <= input_currency <= len(currency_names)):
      print('提示使用者輸入錯誤')
      continue
      
    # 若以上皆輸入正確，則前往下個節點
    check_point = 3
  ```

* 第 3 個節點：計算出兌換後的外幣金額
  ```python
  elif check_point == 3:
    exchanged_amount = input_NTD / currency_rates[currency_names[input_currency - 1]]
    print('顯示結果')
    
    check_point = 1
    counter += 1
  ```


## 系統環境
### 作業系統
* OS：Windows 7 / 10 (Mac OS、Linux 系統亦可相容)

### 相關套件
* Python 核心：3.10
* Beautiful soup：4.9


## 聯絡資料
👤 **Larry Jhuang**
  * Email: larry30500@gmail.com


## 致謝
*非常感謝指導老師提供靈感和方向。3-5行*

*如果您喜歡此專案，記得點擊⭐️支持作者。*


## 權限
目前設定為 MIT 權限。請參閱 `LICENSE`，了解更多相關 MIT 權限的規定。

<br><br>[返回目錄](#目錄)

