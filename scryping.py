import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# スクレイピング対象のURL
urls = [
    "https://example.com/article1",
    "https://example.com/article2",
    # 他のURLをここに追加
]

data = []

for url in urls:
    try:
        # HTTP GETリクエストを送信
        response = requests.get(url)
        response.raise_for_status()
        
        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # タイトルを取得
        title = soup.find('h1').text if soup.find('h1') else 'No title'
        
        # 記事内容を取得
        content = soup.find('div', class_='article-content').text if soup.find('div', class_='article-content') else 'No content'
        
        # データをリストに追加
        data.append([title, content, url])
        
        # 少し待機してから次のリクエストを送信
        time.sleep(1)
        
        # 100件に達したら終了
        if len(data) >= 100:
            break
    
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        continue

# データをCSV形式で保存
df = pd.DataFrame(data, columns=['Title', 'Content', 'URL'])
df.to_csv('scraped_articles.csv', index=False, encoding='utf-8-sig')

print("スクレイピングが完了し、結果が'scraped_articles.csv'に保存されました。")