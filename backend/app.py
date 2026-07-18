"""
甲骨文创意学习与文创平台 - Flask后端
提供用户认证、购物车/订单、游戏排行、甲骨文数据API
"""
import os
import json
import time
import uuid
import hashlib
from functools import wraps
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=None)
CORS(app, supports_credentials=True)

# ===== 数据存储路径 =====
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
ORDERS_FILE = os.path.join(DATA_DIR, 'orders.json')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')
SESSIONS = {}  # token -> username 映射（内存存储）

# 确保数据目录和文件存在
os.makedirs(DATA_DIR, exist_ok=True)
for f in [USERS_FILE, ORDERS_FILE, SCORES_FILE]:
    if not os.path.exists(f):
        with open(f, 'w', encoding='utf-8') as fp:
            json.dump([], fp, ensure_ascii=False)


# ===== 工具函数 =====
def load_data(filepath):
    """加载JSON数据"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(filepath, data):
    """保存JSON数据"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def hash_password(password):
    """密码哈希（SHA-256 + 盐值）"""
    salt = 'oracle_platform_2025'
    return hashlib.sha256((password + salt).encode()).hexdigest()

def generate_token():
    """生成访问令牌"""
    return uuid.uuid4().hex + uuid.uuid4().hex

def require_auth(f):
    """认证装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token or token not in SESSIONS:
            return jsonify({'success': False, 'message': '未登录或登录已过期'}), 401
        request.current_user = SESSIONS[token]
        return f(*args, **kwargs)
    return decorated


# ===== 甲骨文数据API =====
ORACLE_CHARS_DATA = [
    {
        "id": 1, "char": "人", "pinyin": "rén",
        "svg": '<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="8" stroke-linecap="round" fill="none"><path d="M60 30 L60 90"/><path d="M30 90 Q30 150 60 150 Q90 150 90 90"/></g></svg>',
        "meaning": "人，象形字。像侧面站立的人形，本义为人。",
        "category": "象形", "strokeCount": 2,
        "examples": ["大人", "小人", "众人"]
    },
    {
        "id": 2, "char": "日", "pinyin": "rì",
        "svg": '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="8" fill="none"><circle cx="60" cy="60" r="44"/><line x1="16" y1="60" x2="104" y2="60"/></g></svg>',
        "meaning": "日，象形字。像太阳之形，中间一横表示太阳的光芒，本义为太阳。",
        "category": "象形", "strokeCount": 4,
        "examples": ["今日", "明日", "日出"]
    },
    {
        "id": 3, "char": "月", "pinyin": "yuè",
        "svg": '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="8" fill="none"><path d="M85 25 Q35 25 35 60 Q35 95 85 95 Q60 95 60 60 Q60 25 85 25 Z"/></g></svg>',
        "meaning": "月，象形字。像月牙之形，本义为月亮。",
        "category": "象形", "strokeCount": 4,
        "examples": ["今月", "明月", "月食"]
    },
    {
        "id": 4, "char": "水", "pinyin": "shuǐ",
        "svg": '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="8" stroke-linecap="round" fill="none"><line x1="20" y1="40" x2="100" y2="40"/><line x1="20" y1="60" x2="100" y2="60"/><line x1="20" y1="80" x2="100" y2="80"/><circle cx="40" cy="100" r="4" fill="#5c3d2e"/><circle cx="60" cy="100" r="4" fill="#5c3d2e"/><circle cx="80" cy="100" r="4" fill="#5c3d2e"/></g></svg>',
        "meaning": "水，象形字。像流水之形，中间线条表示水流，本义为水。",
        "category": "象形", "strokeCount": 5,
        "examples": ["流水", "河水", "雨水"]
    },
    {
        "id": 5, "char": "火", "pinyin": "huǒ",
        "svg": '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="8" stroke-linecap="round" fill="none"><path d="M60 70 L60 110"/><path d="M35 70 Q35 35 60 35 Q85 35 85 70"/></g></svg>',
        "meaning": "火，象形字。像火焰升腾之形，本义为火。",
        "category": "象形", "strokeCount": 4,
        "examples": ["大火", "小火", "火光"]
    },
    {
        "id": 6, "char": "木", "pinyin": "mù",
        "svg": '<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="8" stroke-linecap="round" fill="none"><line x1="60" y1="20" x2="60" y2="140"/><path d="M25 70 Q25 25 60 25 Q95 25 95 70"/><line x1="30" y1="140" x2="90" y2="140"/></g></svg>',
        "meaning": "木，象形字。像树木之形，上为树冠，下为树根，本义为树木。",
        "category": "象形", "strokeCount": 4,
        "examples": ["大木", "林木", "木匠"]
    },
    {
        "id": 7, "char": "山", "pinyin": "shān",
        "svg": '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="8" stroke-linecap="round" fill="none"><path d="M20 100 L20 50 L50 80 L50 30 L70 30 L70 80 L100 50 L100 100 Z" stroke-linejoin="round"/></g></svg>',
        "meaning": "山，象形字。像山峰之形，三个山峰并列，本义为山。",
        "category": "象形", "strokeCount": 3,
        "examples": ["高山", "大山", "山林"]
    },
    {
        "id": 8, "char": "雨", "pinyin": "yǔ",
        "svg": '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><g stroke="#5c3d2e" stroke-width="6" stroke-linecap="round" fill="none"><path d="M20 30 Q20 15 35 15 L85 15 Q100 15 100 30 L100 55 Q100 70 85 70 L35 70 Q20 70 20 55 Z"/><line x1="35" y1="85" x2="35" y2="105"/><line x1="55" y1="85" x2="55" y2="105"/><line x1="75" y1="85" x2="75" y2="105"/><line x1="95" y1="85" x2="95" y2="105"/></g></svg>',
        "meaning": "雨，象形字。上为天空，下为雨滴，本义为下雨。",
        "category": "象形", "strokeCount": 8,
        "examples": ["大雨", "小雨", "风雨"]
    }
]

@app.route('/api/oracle-chars', methods=['GET'])
def get_oracle_chars():
    """获取所有甲骨文字数据"""
    return jsonify({'success': True, 'data': ORACLE_CHARS_DATA})

@app.route('/api/oracle-chars/<int:char_id>', methods=['GET'])
def get_oracle_char(char_id):
    """获取单个甲骨文字数据"""
    char = next((c for c in ORACLE_CHARS_DATA if c['id'] == char_id), None)
    if char:
        return jsonify({'success': True, 'data': char})
    return jsonify({'success': False, 'message': '未找到该字符'}), 404

@app.route('/api/oracle-chars/search', methods=['GET'])
def search_oracle_chars():
    """搜索甲骨文字"""
    keyword = request.args.get('q', '')
    results = [c for c in ORACLE_CHARS_DATA if keyword in c['char'] or keyword in c['meaning']]
    return jsonify({'success': True, 'data': results})


# ===== 用户认证API =====
@app.route('/api/auth/register', methods=['POST'])
def register():
    """用户注册"""
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '')
    phone = data.get('phone', '').strip()

    if not username or not password:
        return jsonify({'success': False, 'message': '用户名和密码不能为空'}), 400
    if len(password) < 6 or len(password) > 20:
        return jsonify({'success': False, 'message': '密码长度必须为6-20位'}), 400

    users = load_data(USERS_FILE)
    if any(u['username'] == username for u in users):
        return jsonify({'success': False, 'message': '用户名已存在'}), 409

    user = {
        'id': len(users) + 1,
        'username': username,
        'password': hash_password(password),
        'phone': phone,
        'name': username,
        'createdAt': int(time.time())
    }
    users.append(user)
    save_data(USERS_FILE, users)
    return jsonify({'success': True, 'message': '注册成功'})

@app.route('/api/auth/login', methods=['POST'])
def login():
    """用户登录"""
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '')

    users = load_data(USERS_FILE)
    user = next((u for u in users if u['username'] == username), None)
    if not user or user['password'] != hash_password(password):
        return jsonify({'success': False, 'message': '用户名或密码错误'}), 401

    token = generate_token()
    SESSIONS[token] = username
    return jsonify({
        'success': True,
        'token': token,
        'user': {'username': user['username'], 'name': user['name'], 'phone': user.get('phone', '')}
    })

@app.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout():
    """退出登录"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    SESSIONS.pop(token, None)
    return jsonify({'success': True, 'message': '已退出登录'})

@app.route('/api/auth/me', methods=['GET'])
@require_auth
def get_current_user():
    """获取当前用户信息"""
    username = request.current_user
    users = load_data(USERS_FILE)
    user = next((u for u in users if u['username'] == username), None)
    if user:
        return jsonify({'success': True, 'user': {
            'username': user['username'], 'name': user['name'], 'phone': user.get('phone', '')
        }})
    return jsonify({'success': False, 'message': '用户不存在'}), 404


# ===== 购物车/订单API =====
@app.route('/api/orders', methods=['GET'])
@require_auth
def get_orders():
    """获取当前用户的订单"""
    username = request.current_user
    orders = load_data(ORDERS_FILE)
    user_orders = [o for o in orders if o['username'] == username]
    return jsonify({'success': True, 'data': user_orders})

@app.route('/api/orders', methods=['POST'])
@require_auth
def create_order():
    """创建订单"""
    data = request.get_json()
    items = data.get('items', [])
    if not items:
        return jsonify({'success': False, 'message': '订单不能为空'}), 400

    total = sum(item.get('price', 0) * item.get('quantity', 1) for item in items)
    order = {
        'id': f"ORD{int(time.time())}{uuid.uuid4().hex[:4].upper()}",
        'username': request.current_user,
        'items': items,
        'total': total,
        'status': 'pending',
        'createdAt': int(time.time())
    }
    orders = load_data(ORDERS_FILE)
    orders.append(order)
    save_data(ORDERS_FILE, orders)
    return jsonify({'success': True, 'data': order, 'message': '订单创建成功'})

@app.route('/api/orders/<order_id>', methods=['DELETE'])
@require_auth
def cancel_order(order_id):
    """取消订单"""
    orders = load_data(ORDERS_FILE)
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({'success': False, 'message': '订单不存在'}), 404
    if order['username'] != request.current_user:
        return jsonify({'success': False, 'message': '无权限'}), 403
    order['status'] = 'cancelled'
    save_data(ORDERS_FILE, orders)
    return jsonify({'success': True, 'message': '订单已取消'})


# ===== 游戏成绩排行API =====
@app.route('/api/scores', methods=['GET'])
def get_scores():
    """获取排行榜"""
    game_type = request.args.get('game', '')
    scores = load_data(SCORES_FILE)
    if game_type:
        scores = [s for s in scores if s.get('game') == game_type]
    scores.sort(key=lambda x: x.get('score', 0), reverse=True)
    return jsonify({'success': True, 'data': scores[:50]})

@app.route('/api/scores', methods=['POST'])
def submit_score():
    """提交游戏成绩"""
    data = request.get_json()
    username = data.get('username', '匿名用户')
    game = data.get('game', '')
    score = data.get('score', 0)

    if not game:
        return jsonify({'success': False, 'message': '游戏类型不能为空'}), 400

    record = {
        'id': uuid.uuid4().hex,
        'username': username,
        'game': game,
        'score': score,
        'createdAt': int(time.time())
    }
    scores = load_data(SCORES_FILE)
    scores.append(record)
    save_data(SCORES_FILE, scores)
    return jsonify({'success': True, 'data': record, 'message': '成绩已提交'})


# ===== 健康检查 =====
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'success': True, 'message': '服务正常运行', 'timestamp': int(time.time())})


# ===== 启动 =====
if __name__ == '__main__':
    print("=" * 50)
    print("  甲骨文创意学习与文创平台 - 后端服务")
    print("  API地址: http://localhost:5000")
    print("  健康检查: http://localhost:5000/api/health")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)
