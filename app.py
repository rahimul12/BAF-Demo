from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Default MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Default MySQL password
app.config['MYSQL_DB'] = 'baganbari_agro_farm'

mysql = MySQL(app)

@app.route('/')
def index():
    # MySQL থেকে গরুর তথ্য নেওয়া
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cows")
    cows = cur.fetchall()
    
    return render_template('index.html', cows=cows)

if __name__ == '__main__':
    app.run(debug=True)
