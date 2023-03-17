from flask import Flask, render_template

static_folder = 'static'
template_folder = 'templates'

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


@app.route('/')
def warning():
    return '<a href="/home">hello there</a>'

@app.route('/snake')
def snake():
    return render_template('snake.html')


@app.route('/fun_fact')
def fun_fact():
    return render_template('mario.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/game')
def game():
    return render_template('game.html')



app.run(host="0.0.0.0", port=5000, debug=True)

