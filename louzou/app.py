from flask import Flask, render_template, url_for
from db import db_conn

app = Flask(__name__)

@app.route('/')
def calendar():
    
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT date, medication, hours FROM intake")
    hours_data = cursor.fetchall()

    conn.close()

    # Generate the URL for 'intake.png' in the 'static' folder
    intake_image_url = url_for('static', filename='intake1.png')

    intake_image_url2 = url_for('static', filename='intake2.png')

    return render_template('calendar.html', hours_data=hours_data, intake_image_url=intake_image_url, intake_image_url2=intake_image_url2)

if __name__ == '__main__':
    app.run(debug=True)
