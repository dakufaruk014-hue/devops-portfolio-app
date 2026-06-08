from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Umar Daku Faruk</h1>
    <p>Cloud & DevOps Engineer</p>
    <p>Deployed via Docker + Azure + GitHub Actions</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)