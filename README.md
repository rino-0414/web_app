# web-app
データベースの最終課題用のリポジトリーです。  
flaskを使用してindex.htmlを表示させています。 
当環境ではvenvを使用して環境構築を行っています。  
flask run の --debug は開発中のみ使用してください。ページを更新することでリアルタイムで更新されます。  
   
venv\Scripts\Activate.ps1  
cd flaskr  
$env:FLASK_APP="flaskr"  
$env:FLASK_ENV="development"  
flask run --debug  
  
共有の際.envを使用してpostgreSQLにアクセスします。以下のフォーマットでWEB_APP上に.envを用意すること。  
  
DB_HOST=localhost  
DB_NAME=calendar_app  
DB_USER=postgres  
DB_PASSWORD=your_password    
  
この.envファイルは.gitignoreにより、プッシュされないようになっています。  
  
使用しているパッケージは  
Flask  
psycopg2  
python-dotenv  
です。共有した際にインストールしてください。