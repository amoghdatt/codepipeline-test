from flask import Flask ,request, jsonify,Response

app = Flask(__name__)

@app.route
def test():
    return {'message':'from ec2'}

if __name__ == "__main__":
    app.run()