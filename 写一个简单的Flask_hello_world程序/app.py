"""
Flask Hello World 应用
一个简单但完整的 Flask Web 应用示例
"""

from flask import Flask, render_template, jsonify

# 创建 Flask 应用实例
app = Flask(__name__)

# 应用配置
app.config['DEBUG'] = True
app.config['APP_NAME'] = 'Flask Hello World'


@app.route('/')
def index():
    """
    首页路由
    返回欢迎页面
    """
    return render_template('index.html', app_name=app.config['APP_NAME'])


@app.route('/hello')
def hello():
    """
    简单的 Hello World 路由
    """
    return '<h1>Hello, World!</h1><p>欢迎使用 Flask</p>'


@app.route('/hello/<name>')
def hello_name(name):
    """
    个性化问候路由
    
    Args:
        name: 用户名称
    
    Returns:
        个性化的问候信息
    """
    return f'<h1>Hello, {name}!</h1><p>欢迎来到 Flask 应用</p>'


@app.route('/api/info')
def api_info():
    """
    API 接口
    返回 JSON 格式的应用信息
    """
    return jsonify({
        'app_name': app.config['APP_NAME'],
        'status': 'running',
        'version': '1.0.0',
        'endpoints': [
            {'url': '/', 'description': '首页'},
            {'url': '/hello', 'description': 'Hello World'},
            {'url': '/hello/<name>', 'description': '个性化问候'},
            {'url': '/api/info', 'description': 'API 信息'}
        ]
    })


if __name__ == '__main__':
    print(f"\n{'='*50}")
    print(f"🚀 {app.config['APP_NAME']} 正在启动...")
    print(f"{'='*50}")
    print(f"📍 访问地址: http://127.0.0.1:5000/")
    print(f"📍 API信息: http://127.0.0.1:5000/api/info")
    print(f"{'='*50}\n")
    
    # 运行开发服务器
    app.run(host='0.0.0.0', port=5000, debug=True)