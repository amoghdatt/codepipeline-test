from flask import Flask ,request, jsonify,Response

app = Flask(__name__)

@app.route('/')
def test():
    return {'message':'deployed using CodeDeploy on Ubuntu ec2 instance'}

if __name__ == "__main__":
    app.run()