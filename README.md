# web-app
データベースの最終課題用のリポジトリーです。  
flaskを使用してindex.htmlを表示させています。 
当環境ではvenvを使用して環境構築を行っています。  
flask run の --debug は開発中のみ使用してください。ページを更新することでリアルタイムで更新されます。  
   
venv\Scripts\Activate.ps1  
cd flaskr  
$env:FLASK_APP="flaskr"  
&env:FLASK_ENV="development"  
flask run --debug  