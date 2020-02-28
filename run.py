from flask import Flask ,request, jsonify,Response

app = Flask(__name__)

@app.route('/')
def test():
    return {'message':'merged to masterd and deployed using CodeDeploy on Ubuntu ec2 instance'}

if __name__ == "__main__":
    app.run(host='0.0.0.0')