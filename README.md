# web-app
データベースの最終課題用のリポジトリーです。  
flaskを使用して表示させています。 
当環境ではvenvを使用して環境構築を行っています。  
flask run の --debug は開発中のみ使用してください。ファイルを更新することでリアルタイムで更新されます。  
   
python -m venv venv

venv\Scripts\Activate.ps1  
cd flaskr  
$env:FLASK_APP="flaskr"  
$env:FLASK_ENV="development"  
flask run --debug  
  
共有の際.envを使用してpostgreSQLにアクセスします。以下のフォーマットでWEB_APP上に.envを用意すること。  
  
DB_HOST=localhost  
DB_NAME=your_database_name  
DB_USER=postgres  
DB_PASSWORD=your_password   
  
この.envファイルは.gitignoreにより、プッシュされないようになっています。  
  
使用しているパッケージは  
Flask  
psycopg2  
python-dotenv  
です。共有した際にインストールしてください。
  
このWebアプリはタスク管理カレンダーです。  
トップ画面にある日付をクリックすることでその日のタスクを確認、追加することができます。画面上部の日付の左右（<>）をクリックすることで月を変えられます。　　
期限の近いタスクをクリックすることで完了済みタスクに移動させます。  
タスク一覧からはタイトルをクリックすることで完了済みにできる他、タスクの編集が行えます。削除も編集画面から行えます。  
