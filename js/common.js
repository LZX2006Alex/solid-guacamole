/* ========================================
 * 甲骨文创意学习与文创平台 - 公共脚本
 * ======================================== */

const Toast = {
    container: null,
    init() {
        if (this.container) return;
        this.container = document.createElement('div');
        this.container.className = 'toast-container';
        document.body.appendChild(this.container);
    },
    show(message, type = 'info', duration = 3000) {
        this.init();
        const icons = { success: '✓', error: '✕', warning: '⚠', info: 'ℹ' };
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <span class="toast-icon">${icons[type] || icons.info}</span>
            <span class="toast-message">${message}</span>
        `;
        this.container.appendChild(toast);
        setTimeout(() => toast.remove(), duration);
    },
    success(m, d) { this.show(m, 'success', d); },
    error(m, d) { this.show(m, 'error', d); },
    warning(m, d) { this.show(m, 'warning', d); },
    info(m, d) { this.show(m, 'info', d); }
};

const Storage = {
    PREFIX: 'oracle_',
    set(key, value) {
        try { localStorage.setItem(this.PREFIX + key, JSON.stringify(value)); return true; }
        catch (e) { console.error('Storage.set error:', e); return false; }
    },
    get(key, defaultValue = null) {
        try {
            const data = localStorage.getItem(this.PREFIX + key);
            return data ? JSON.parse(data) : defaultValue;
        } catch (e) { console.error('Storage.get error:', e); return defaultValue; }
    },
    remove(key) { localStorage.removeItem(this.PREFIX + key); },
    clear() {
        Object.keys(localStorage)
            .filter(k => k.startsWith(this.PREFIX))
            .forEach(k => localStorage.removeItem(k));
    }
};

const PasswordUtil = {
    hash(password) {
        let hash = 0;
        const salt = 'oracle_salt_2025';
        const str = password + salt;
        for (let i = 0; i < str.length; i++) {
            const char = str.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash;
        }
        return 'h' + Math.abs(hash).toString(36);
    },
    verify(password, hashedPassword) { return this.hash(password) === hashedPassword; }
};

const Auth = {
    getCurrentUser() { return Storage.get('currentUser', null); },
    setCurrentUser(user) { user ? Storage.set('currentUser', user) : Storage.remove('currentUser'); },
    isLoggedIn() { return this.getCurrentUser() !== null; },
    logout() { this.setCurrentUser(null); },
    getRegisteredUsers() { return Storage.get('users', []); },
    register(username, password, phone) {
        const users = this.getRegisteredUsers();
        if (users.find(u => u.username === username)) return { success: false, message: '用户名已存在' };
        users.push({
            username, password: PasswordUtil.hash(password), phone,
            name: username, registeredAt: new Date().toISOString()
        });
        Storage.set('users', users);
        return { success: true, message: '注册成功' };
    },
    login(username, password) {
        const users = this.getRegisteredUsers();
        const user = users.find(u => u.username === username);
        if (user && PasswordUtil.verify(password, user.password)) {
            const { password: _, ...userInfo } = user;
            this.setCurrentUser(userInfo);
            return { success: true, user: userInfo };
        }
        return { success: false, message: '用户名或密码错误' };
    }
};

const CartManager = {
    getCart() { return Storage.get('cart', []); },
    setCart(cart) { Storage.set('cart', cart); },
    addItem(id, name, price, quantity = 1) {
        const cart = this.getCart();
        const existing = cart.find(item => item.id === id);
        if (existing) existing.quantity += quantity;
        else cart.push({ id, name, price, quantity });
        this.setCart(cart);
        return cart;
    },
    removeItem(id) {
        const cart = this.getCart().filter(item => item.id !== id);
        this.setCart(cart);
        return cart;
    },
    updateQuantity(id, quantity) {
        const cart = this.getCart();
        const item = cart.find(item => item.id === id);
        if (item) { item.quantity = Math.max(1, quantity); this.setCart(cart); }
        return cart;
    },
    clear() { Storage.remove('cart'); },
    getTotalCount() { return this.getCart().reduce((s, i) => s + i.quantity, 0); },
    getTotalPrice() { return this.getCart().reduce((s, i) => s + i.price * i.quantity, 0); }
};

const LazyLoad = {
    observer: null,
    init() {
        if (!('IntersectionObserver' in window)) { this.loadAll(); return; }
        this.observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.loadImage(entry.target);
                    this.observer.unobserve(entry.target);
                }
            });
        }, { rootMargin: '50px' });
        document.querySelectorAll('img[data-src]').forEach(img => this.observer.observe(img));
    },
    loadImage(img) {
        img.classList.add('lazy-loading');
        img.src = img.dataset.src;
        img.onload = () => {
            img.classList.remove('lazy-loading');
            img.classList.add('lazy-loaded');
        };
        img.onerror = () => img.classList.remove('lazy-loading');
    },
    loadAll() {
        document.querySelectorAll('img[data-src]').forEach(img => this.loadImage(img));
    }
};

const OracleChars = {
    data: [
        { char: '人', cssClass: 'oracle-human', demoClass: 'demo-human', meaning: '人，象形字，像侧面站立的人形' },
        { char: '日', cssClass: 'oracle-sun', demoClass: 'demo-sun', meaning: '日，象形字，像太阳的形状' },
        { char: '月', cssClass: 'oracle-moon', demoClass: 'demo-moon', meaning: '月，象形字，像月亮的形状' },
        { char: '水', cssClass: 'oracle-water', demoClass: 'demo-water', meaning: '水，象形字，像流动的水' },
        { char: '火', cssClass: 'oracle-fire', demoClass: 'demo-fire', meaning: '火，象形字，像火焰的形状' },
        { char: '木', cssClass: 'oracle-tree', demoClass: 'demo-tree', meaning: '木，象形字，像树木的形状' },
        { char: '山', cssClass: 'oracle-mountain', demoClass: 'demo-mountain', meaning: '山，象形字，像山峰的形状' },
        { char: '雨', cssClass: 'oracle-rain', demoClass: 'demo-rain', meaning: '雨，象形字，像下雨的样子' }
    ],
    getMeaning(char) {
        const m = { '日': '太阳', '月': '月亮', '山': '山脉', '水': '水流', '人': '人类', '木': '树木', '火': '火焰', '雨': '雨水' };
        return m[char] || char;
    },
    getClass(char) {
        const m = { '人': 'human', '木': 'tree', '日': 'sun', '月': 'moon', '水': 'water', '火': 'fire', '山': 'mountain', '雨': 'rain' };
        return m[char] || 'human';
    }
};

document.addEventListener('DOMContentLoaded', () => {
    Toast.init();
    LazyLoad.init();
});
