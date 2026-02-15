import os

# HTMLファイルの一覧を取得
files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
files.sort(reverse=True)

# index.htmlを書き換える
with open("index.html", "w", encoding="utf-8") as f:
    f.write("<html><head><meta charset='utf-8'></head><body>")
    f.write("<h1>English Journaling Index</h1><ul>")
    for file in files:
        f.write(f'<li><a href="{file}">{file}</a></li>')
    f.write("</ul></body></html>")