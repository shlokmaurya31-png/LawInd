from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/roi')
def roi():
    return send_from_directory('.', 'roi.html')

@app.route('/roi/law-firm')
def roi_firm():
    return send_from_directory('.', 'roi-firm.html')

@app.route('/roi/in-house')
def roi_inhouse():
    return send_from_directory('.', 'roi-inhouse.html')

@app.route('/blog')
def blog():
    return send_from_directory('.', 'blog.html')

@app.route('/resources')
def resources():
    return send_from_directory('.', 'resources.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
