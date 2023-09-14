from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('data.csv')
    tables = [df.to_html(classes='data', header="true")]
    return render_template('home.html', tables=tables)

if __name__ == '__main__':
    app.run(debug=True)
