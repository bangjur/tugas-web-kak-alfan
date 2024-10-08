from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hobi')
def hobi():
    return render_template('hobi.html')

@app.route('/pekerjaan')
def pekerjaan():
    return render_template('pekerjaan.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/pendidikan')
def pendidikan():
    return render_template('pendidikan.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
