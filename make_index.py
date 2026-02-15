import os

def generate_index():
    html_links = []
    
    # フォルダ内を再帰的に探索
    for root, dirs, files in os.walk("."):
        # .github などの隠しフォルダは除外
        if ".github" in root or ".git" in root:
            continue
            
        for file in files:
            # HTMLファイルを探す（自分自身は除外）
            if file.endswith(".html") and file != "index.html":
                # index.htmlからの相対パスを取得
                relative_path = os.path.relpath(os.path.join(root, file), ".")
                html_links.append(relative_path)

    # 新しい順（アルファベット逆順）に並べ替え
    html_links.sort(reverse=True)

    # index.htmlの書き出し
    with open("index.html", "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>English Journaling</title></head><body>")
        f.write("<h1>English Journaling 目次</h1><ul>")
        for path in html_links:
            # フォルダ名/ファイル名 という形でリンクが貼られる
            f.write(f'<li><a href="{path}">{path}</a></li>')
        f.write("</ul></body></html>")

if __name__ == "__main__":
    generate_index()