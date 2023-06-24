from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
app.static_folder = 'templates/assets'

if __name__ == '__main__':
    app.run()
