import os

def generate_index():
    # HTMLファイルを探す（自分自身とindex.htmlは除外）
    files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    # 日付順などに並び替え
    files.sort(reverse=True)

    # index.htmlの内容を作成
    content = "<html><head><meta charset='utf-8'><title>Journal Index</title></head><body>"
    content += "<h1>English Journaling Index</h1><ul>"
    for f in files:
        content += f'<li><a href="{f}">{f}</a></li>'
    content += "</ul></body></html>"

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_index()