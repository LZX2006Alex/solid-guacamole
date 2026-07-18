#!/bin/bash
# 甲骨文创意学习与文创平台 - 后端启动脚本

echo "============================================"
echo "  甲骨文创意学习与文创平台 - 后端服务启动"
echo "============================================"

# 进入后端目录
cd "$(dirname "$0")/backend" || exit 1

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到 python3，请先安装 Python 3"
    exit 1
fi

# 创建虚拟环境（如果不存在）
if [ ! -d "venv" ]; then
    echo "正在创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "检查依赖..."
pip install -r requirements.txt -q

# 启动服务
echo ""
echo "启动后端服务..."
echo "API地址: http://localhost:5000"
echo "健康检查: http://localhost:5000/api/health"
echo "按 Ctrl+C 停止服务"
echo ""
python app.py
