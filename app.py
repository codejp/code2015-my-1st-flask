#coding: utf-8
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
app.debug = True

# routing basic
@app.route("/omikuji")
def omikuji():
    return '<h1>omikuji</h1>'

# using template engine
@app.route("/")
def hello():
    greetings = [u'Hello', u'こんにちは', u'你好']
    return render_template('index.html',
                           title=u'挨拶',
                           greetings=greetings)

# retrieve routing parameter & redirect
@app.route('/num/<int:x>')
def number(x):
    if x == 1234:
        return redirect(url_for('hello'))
    return '<h1>{0}</h1>'.format(x)

# retrieve URLquery parameters
@app.route('/getdemo')
def getdemo():
    html = ''
    for key, val in request.args.items():
        html = html + '{0}:{1}<br/>'.format(key, val)
    return html

if __name__ == '__main__':
    app.run()
