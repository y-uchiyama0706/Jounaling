import os
from pathlib import Path

def generate_index():
    html_links = []
    
    # 現在のディレクトリ以下を探索
    for root, dirs, files in os.walk("."):
        # 隠しフォルダを除外
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith(".html") and file != "index.html":
                # 相対パスを取得
                rel_path = os.path.relpath(os.path.join(root, file), ".")
                # Windowsパスを/に統一
                rel_path = rel_path.replace("\\", "/")
                html_links.append(rel_path)
    
    # 新しい順にソート
    html_links.sort(reverse=True)
    
    # index.htmlを生成
    with open("index.html", "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Journaling Index</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>English Journaling 目次</h1>
    <p>Total entries: """ + str(len(html_links)) + """</p>
    <ul>
""")
        
        for path in html_links:
            # フォルダ名/ファイル名の形式で表示
            display_name = path.replace("./", "")
            f.write(f'        <li><a href="{path}">{display_name}</a></li>\n')
        
        f.write("""    </ul>
</body>
</html>
""")
    
    print(f"Generated index.html with {len(html_links)} entries")

if __name__ == "__main__":
    generate_index()