@echo off
cd /d %~dp0
echo 目次を更新しています...

python make_index.py

echo 更新が完了しました。
echo ブラウザで目次を起動します...

:: 生成された index.html を既定のブラウザで開く
start "" "index.html"

timeout /t 3