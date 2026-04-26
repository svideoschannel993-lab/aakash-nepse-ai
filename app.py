from flask import Flask, render_template, request
from core.analyzer import analyze_stock

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    stock = request.form['stock']
    result = analyze_stock(stock)
    return render_template('result.html', data=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
