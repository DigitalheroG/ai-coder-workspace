"""
Flask Hello World - 增强版本
包含多个路由和模板渲染示例
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """首页"""
    return render_template('index.html')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    """问候页面"""
    return render_template('hello.html', name=name or "World")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    """问候表单"""
    greeting = None
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        greeting = f"Hello, {name}!"
    return render_template('greet_form.html', greeting=greeting)


@app.route('/about')
def about():
    """关于页面"""
    return "<h1>About</h1><p>This is a Flask Hello World application.</p>"


@app.route('/api/hello')
def api_hello():
    """API接口 - 返回JSON"""
    return {
        "message": "Hello, World!",
        "status": "success",
        "version": "1.0.0"
    }


if __name__ == '__main__':
    print("🚀 启动 Flask 应用...")
    print("📍 访问地址: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)