# My 1st "Flask" / 初めての Flask

## System Requirements / 前提条件

- Python v.3.4
- virtualenv ( `> pip install virtualenv`)

## How to build & run it / ビルド&実行方法

### Build environment / 環境構築

example on PowerShell of Windows OS:
```
PS> git clone https://github.com/codejp/code2015-my-1st-flask.git
PS> cd ./code2015-my-1st-flask
PS> virtualenv -p <path to python v.3.4> env
PS> ./env/Scripts/activate.ps1
(env)PS> pip install -r requirements.txt
```

### run / 実行
example on PowerShell of Windows OS:
```
(env)PS> python app.py
```

after this, open `http://localhost:5000`

### Deactivate environment / 環境の復帰
example on PowerShell of Windows OS:
```
(env)PS> ./env/Scripts/deactivate.bat
PS>
```
