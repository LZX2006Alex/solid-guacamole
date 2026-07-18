/* ========================================
 * 甲骨文创意学习与文创平台 - API客户端
 * 负责与Flask后端通信
 * ======================================== */

const API = {
    BASE_URL: 'http://localhost:5000/api',
    token: null,

    init() {
        this.token = localStorage.getItem('oracle_api_token');
    },

    setToken(token) {
        this.token = token;
        if (token) {
            localStorage.setItem('oracle_api_token', token);
        } else {
            localStorage.removeItem('oracle_api_token');
        }
    },

    async request(path, options = {}) {
        const url = this.BASE_URL + path;
        const headers = { 'Content-Type': 'application/json' };
        if (this.token) {
            headers['Authorization'] = 'Bearer ' + this.token;
        }
        try {
            const response = await fetch(url, { ...options, headers });
            const data = await response.json();
            if (!response.ok) {
                return { success: false, message: data.message || '请求失败', status: response.status };
            }
            return data;
        } catch (err) {
            console.error('API请求失败:', err);
            return { success: false, message: '网络错误，请检查后端服务是否启动' };
        }
    },

    // 甲骨文数据
    async getOracleChars() {
        return this.request('/oracle-chars');
    },
    async getOracleChar(id) {
        return this.request('/oracle-chars/' + id);
    },
    async searchOracleChars(keyword) {
        return this.request('/oracle-chars/search?q=' + encodeURIComponent(keyword));
    },

    // 用户认证
    async register(username, password, phone) {
        const res = await this.request('/auth/register', {
            method: 'POST',
            body: JSON.stringify({ username, password, phone })
        });
        return res;
    },
    async login(username, password) {
        const res = await this.request('/auth/login', {
            method: 'POST',
            body: JSON.stringify({ username, password })
        });
        if (res.success) this.setToken(res.token);
        return res;
    },
    async logout() {
        const res = await this.request('/auth/logout', { method: 'POST' });
        this.setToken(null);
        return res;
    },
    async getCurrentUser() {
        if (!this.token) return { success: false };
        return this.request('/auth/me');
    },

    // 订单
    async getOrders() {
        return this.request('/orders');
    },
    async createOrder(items) {
        return this.request('/orders', {
            method: 'POST',
            body: JSON.stringify({ items })
        });
    },
    async cancelOrder(orderId) {
        return this.request('/orders/' + orderId, { method: 'DELETE' });
    },

    // 游戏成绩
    async getScores(game) {
        return this.request('/scores' + (game ? '?game=' + game : ''));
    },
    async submitScore(username, game, score) {
        return this.request('/scores', {
            method: 'POST',
            body: JSON.stringify({ username, game, score })
        });
    }
};

API.init();
