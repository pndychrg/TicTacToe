from flask import Flask, render_template,redirect

BOARD= [0] * 9 # 1-D representation of board
NEXT =  1  #= X, -1 = 0 You, & days ago Working TILL
app = Flask(__name__,
static_folder='assets',
template_folder = "templates")


@app.route('/')
def homepage():
    return render_template("tic.html", board=BOARD, next=NEXT)
def checkstate (board): --

@app.route('/set/<int:i>')
def setvalue(i): -


@app.route('/new')
def newgame (): --


app.run()