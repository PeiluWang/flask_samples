#coding=utf-8
"""
运行说明：
安装Flask添加跨域访问支持:
    pip install flask
    pip install flask_cors
运行simple_server
    python simple_server
服务器已启动，访问http://127.0.0.1:5001/ 即可看到主页面
"""
from flask import Flask
from flask import request
from functools import wraps
from flask import make_response
from flask_cors import CORS, cross_origin
import json

#创建app
app = Flask(__name__)
#支持跨域访问
CORS(app)

#简单页面示例
@app.route("/")
def index():
    return "This is simple sample of Flask server"

#路径参数示例
@app.route("/hello/")
@app.route("/hello/<user_name>")
def hello(user_name=None):
    return "Hello %s"%(user_name)

#get请求
@app.route("/test_get", methods=['GET'])
def test_get():
    print "------request args----------"
    print request.args
    token=request.args.get("token","")
    print "-------token value---------"
    print token
    return "receive token: %s"%(token)

#post请求示例
@app.route("/test_post", methods=['POST'])
def test_post():
    print "-------request data--------"
    print request.data
    return "receive data: %s"%request.data

#post请求，RESTful api示例
@app.route("/test_json", methods=['POST'])
def test_json():
    print "-------request data--------"
    post_data= request.get_json(silent=False)
    print post_data
    return_data={"records":[{"Name":u"阿尔冯斯.霍因海姆","City":"Berlin","Country":"Germany"}]}
    return json.dumps(return_data)

if __name__ == "__main__":
    # 绑定端口：5001
    app.run(host='127.0.0.1', port=5001, debug=True)
