import os
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME') # Email sender dari environment variable
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD') # Password dari environment variable
mail = Mail(app)

# Database connection details
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def connect_db():
    return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hobi')
def hobi():
    return render_template('hobi.html')

@app.route('/pekerjaan')
def pekerjaan():
    return render_template('pekerjaan.html')

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        isi_pesan = request.form['isi_pesan']

        # Insert data into the database
        cur.execute("INSERT INTO laman_kontak (nama, email, isi_pesan) VALUES (%s, %s, %s)", (nama, email, isi_pesan))
        conn.commit()

        # Send email
        msg = Message('Pesan Baru dari Kontak', sender='azzuriptr@gmail.com', recipients=[email])
        msg.body = f"Nama: {nama}\nEmail: {email}\nPesan: {'Terimakasih sudah submit pesanmu :) Nanti kubaca deh wkwk'}"
        mail.send(msg)

    # Retrieve data from the database to display in the table
    cur.execute("SELECT nama, email, isi_pesan FROM laman_kontak")
    pesan_list = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('kontak.html', pesan_list=pesan_list)

@app.route('/pendidikan')
def pendidikan():
    return render_template('pendidikan.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)