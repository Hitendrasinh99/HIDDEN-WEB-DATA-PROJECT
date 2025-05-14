from flask import Flask, send_from_directory
import os


app = Flask(__name__)

@app.route('/index.html')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/Xindex.html')
def xindex():
    return send_from_directory('.', 'Xindex.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
