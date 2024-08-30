from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_file():
    return send_file('C:/Users/weai.42191/Desktop/Uteis/Gerador de senha.html')

if __name__ == '__main__':
    app.run(debug=True)
