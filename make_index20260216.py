import os
from collections import defaultdict

def generate_index():
    # データを フォルダ名: [ファイルリスト] の辞書形式で保持
    structure = defaultdict(list)
    
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".github" in root:
            continue
        for file in files:
            if file.endswith(".html") and file != "index.html":
                rel_path = os.path.relpath(os.path.join(root, file), ".")
                url_path = rel_path.replace(os.sep, '/')
                
                # フォルダ名（年）を取得。直下なら"Others"
                folder_name = url_path.split('/')[0] if '/' in url_path else "Root"
                structure[folder_name].append((file, url_path))

    # 年の順（降順）、中のファイルも降順に並べ替え
    sorted_years = sorted(structure.keys(), reverse=True)

    content = f"""<!DOCTYPE html>
<html lang='ja'>
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>English Journaling Archives</title>
    <style>
        body {{ font-family: 'Helvetica Neue', Arial, sans-serif; background-color: #f0f2f5; margin: 0; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        h1 {{ text-align: center; color: #1a73e8; margin-bottom: 30px; }}
        
        /* フォルダ（年）のスタイル */
        .year-section {{ margin-bottom: 15px; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .year-header {{ 
            padding: 20px; background: #fff; cursor: pointer; display: flex; justify-content: space-between; align-items: center;
            font-size: 1.2rem; font-weight: bold; color: #3c4043; border-bottom: 1px solid #eee;
        }}
        .year-header:hover {{ background-color: #f8f9fa; }}
        .year-header::after {{ content: '▼'; font-size: 0.8rem; transition: transform 0.3s; }}
        
        /* 開閉の仕組み */
        .file-list {{ display: none; padding: 10px 20px; background: #fafafa; }}
        .year-section.open .file-list {{ display: block; }}
        .year-section.open .year-header::after {{ transform: rotate(180deg); }}

        /* ファイル（カード風）のスタイル */
        .file-item {{ 
            display: block; text-decoration: none; color: #5f6368; padding: 12px; margin: 8px 0;
            background: white; border-radius: 6px; border: 1px solid #dadce0; transition: all 0.2s;
        }}
        .file-item:hover {{ border-color: #1a73e8; color: #1a73e8; transform: translateX(5px); background: #e8f0fe; }}
    </style>
</head>
<body>
    <div class='container'>
        <h1>English Journaling Archives</h1>
"""
    
    for year in sorted_years:
        content += f"""
        <div class='year-section'>
            <div class='year-header' onclick="this.parentElement.classList.toggle('open')">{year}年</div>
            <div class='file-list'>"""
        
        # その年の中のファイルを新しい順に並べて表示
        sorted_files = sorted(structure[year], key=lambda x: x[1], reverse=True)
        for filename, path in sorted_files:
            content += f"<a href='{path}' class='file-item'>📄 {filename}</a>"
            
        content += "</div></div>"

    content += """
    </div>
    <script>
        // 最新の年（一番上）だけ最初から開いておく
        document.querySelector('.year-section')?.classList.add('open');
    </script>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Success: Generated index with {len(sorted_years)} folders.")

if __name__ == "__main__":
    generate_index()