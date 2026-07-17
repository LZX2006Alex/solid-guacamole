# 甲骨文创意学习与文创平台 - Code Wiki

## 目录
1. [项目概述](#1-项目概述)
2. [项目架构](#2-项目架构)
3. [文件结构](#3-文件结构)
4. [主要模块详解](#4-主要模块详解)
5. [关键功能与技术实现](#5-关键功能与技术实现)
6. [数据结构与模拟数据](#6-数据结构与模拟数据)
7. [样式系统](#7-样式系统)
8. [运行方式与部署指南](#8-运行方式与部署指南)
9. [依赖关系](#9-依赖关系)
10. [扩展开发指南](#10-扩展开发指南)

---

## 1. 项目概述

### 1.1 项目简介
"甲骨文创意学习与文创平台"是一个集甲骨文学习、互动游戏、文创产品展示与定制于一体的纯前端Web应用。项目旨在通过现代化的Web技术，传播和推广中国古老的甲骨文文化，让用户在游戏和购物中学习甲骨文知识。

### 1.2 项目背景
- **开发团队**：安阳师范学院
- **版权年份**：2025
- **项目类型**：静态网站 / 纯前端应用
- **技术栈**：HTML5 + CSS3 + 原生JavaScript

### 1.3 核心功能模块
| 模块 | 功能描述 | 对应页面 |
|------|----------|----------|
| 主页门户 | 平台入口，展示学习资源、文创产品、互动学习入口 | 甲骨文创意学习与文创平台3.html |
| 文创定制服务 | 文创产品展示与个性化定制 | 文创定制服务.html |
| 甲骨文书写练习 | Canvas画布书写练习，支持演示和提示 | 甲骨文书写练习.html |
| 甲骨文猜字游戏 | 看图识字游戏，10道题计分 | 甲骨文猜字游戏.html |
| 甲骨文翻译挑战 | 段落翻译挑战，5段难度递进 | 甲骨文翻译挑战.html |
| 产品详情页 | 单个文创产品详细展示与订购 | 甲骨文书签.html / 甲骨文创意U盘.html 等 |

---

## 2. 项目架构

### 2.1 架构概览
项目采用**多页面静态网站架构**，每个功能模块对应一个独立的HTML文件，页面之间通过超链接相互跳转。所有样式和脚本均内联在各自的HTML文件中，无外部构建工具依赖。

```
┌─────────────────────────────────────────────────────┐
│                   主页 (主入口)                       │
│        甲骨文创意学习与文创平台3.html                │
├────────────┬────────────┬────────────┬──────────────┤
│ 学习资源   │ 文创产品   │ 互动学习   │ 用户系统     │
└─────┬──────┴─────┬──────┴─────┬──────┴──────┬───────┘
      │            │            │             │
      ▼            ▼            ▼             ▼
 ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌─────────┐
 │字典/课程│  │定制服务 │  │猜字游戏  │  │登录注册 │
 └─────────┘  └─────────┘  └──────────┘  └─────────┘
                           │
                      ┌────┴────┐
                      ▼         ▼
                 ┌────────┐ ┌──────────┐
                 │书写练习│ │翻译挑战  │
                 └────────┘ └──────────┘
```

### 2.2 技术架构层次
```
表现层 (Presentation Layer)
  ├── HTML5 语义化结构
  ├── CSS3 样式与动画
  └── 响应式布局设计

交互层 (Interaction Layer)
  ├── DOM 事件处理
  ├── Canvas 绘图 API
  └── 状态管理 (变量存储)

数据层 (Data Layer)
  ├── 内存模拟数据 (mock data)
  ├── LocalStorage (预留)
  └── 静态资源文件

外部依赖 (External Dependencies)
  └── Font Awesome 6.4.0 (CDN)
```

---

## 3. 文件结构

### 3.1 完整文件清单

| 文件名 | 类型 | 大小 | 功能描述 |
|--------|------|------|----------|
| [甲骨文创意学习与文创平台3.html](file:///workspace/甲骨文创意学习与文创平台3.html) | HTML | ~1500行 | 主页面，平台入口 |
| [文创定制服务.html](file:///workspace/文创定制服务.html) | HTML | 900行 | 文创产品展示与定制 |
| [甲骨文书写练习.html](file:///workspace/甲骨文书写练习.html) | HTML | 976行 | Canvas书写练习 |
| [甲骨文猜字游戏.html](file:///workspace/甲骨文猜字游戏.html) | HTML | 889行 | 猜字游戏 |
| [甲骨文翻译挑战.html](file:///workspace/甲骨文翻译挑战.html) | HTML | 672行 | 翻译挑战游戏 |
| [甲骨文书签.html](file:///workspace/甲骨文书签.html) | HTML | 352行 | 书签产品详情页 |
| [甲骨文创意U盘.html](file:///workspace/甲骨文创意U盘.html) | HTML | ~350行 | U盘产品详情页 |
| [甲骨文笔记本.html](file:///workspace/甲骨文笔记本.html) | HTML | ~350行 | 笔记本产品详情页 |
| [甲骨文玩偶.html](file:///workspace/甲骨文玩偶.html) | HTML | ~350行 | 玩偶产品详情页 |
| 甲骨文背景.gif | GIF | - | 主页背景动图 |
| U盘.jpg / 书签.jpg / 笔记本.jpg / 玩偶.jpg | JPG | - | 产品展示图片 |
| 日.jpg / 月.jpg / 山.jpg / 水.jpg / 人.jpg / 木.jpg | JPG | - | 甲骨文字展示图片 |

### 3.2 文件分类说明

#### 核心页面 (Core Pages)
- 主页面：提供导航、学习资源、文创产品、用户系统等综合功能
- 互动学习页面：3个独立游戏/练习页面
- 文创定制页面：产品展示与定制功能

#### 产品详情页 (Product Detail Pages)
- 4个独立的产品详情页，结构相似但内容不同
- 每个页面包含产品展示、特色说明、订购表单

#### 静态资源 (Static Assets)
- 图片资源：产品图、文字图、背景动图
- 无独立CSS/JS文件，全部内联

---

## 4. 主要模块详解

### 4.1 主页模块 (甲骨文创意学习与文创平台3.html)

#### 4.1.1 页面结构
```
Header (导航栏)
  ├── Logo: 甲骨文苑
  ├── 导航链接: 首页/学习资源/文创产品/甲骨文字典/互动学习/关于我们
  ├── 搜索框
  ├── 购物车图标
  └── 登录按钮

Hero (主横幅)
  └── 背景动图 + 标题 + 副标题 + CTA按钮

学习资源区 (Learning Resources)
  ├── 甲骨文基础入门课程 (外链B站)
  ├── 甲骨文字典查询 (外链字典网站)
  └── 甲骨文研究文献 (外链文献网站)

文创产品区 (Products)
  ├── 甲骨文创意U盘
  ├── 甲骨文笔记本
  ├── 甲骨文书签
  └── 甲骨文玩偶

甲骨文字展示区 (Oracle Bones)
  ├── 日 / 月 / 山 / 水 / 人 / 木
  └── 点击跳转B站视频讲解

互动学习区 (Interactive Learning)
  ├── 甲骨文猜字游戏
  ├── 甲骨文书写练习
  └── 甲骨文翻译挑战

Footer (页脚)
  ├── 关于我们 / 学习资源 / 文创产品 / 关注我们
  └── 版权信息

模态框 (Modals)
  ├── 登录/注册模态框
  ├── 购物车侧边栏
  └── 页脚详情弹窗
```

#### 4.1.2 核心JavaScript功能

**用户认证系统**
```javascript
// 模拟用户数据
const mockUsers = [
    { username: 'user1', password: 'pass1', name: '用户一', phone: '13800138000' },
    { username: 'user2', password: 'pass2', name: '用户二', phone: '13900139000' }
];

// 应用状态
let currentUser = null;      // 当前登录用户
let cart = [];               // 购物车数据
let verifyCodeTimer = null;  // 验证码计时器
let storedVerifyCode = '';   // 存储生成的验证码
```

**主要函数说明**
| 函数名 | 功能 | 参数 | 返回值 |
|--------|------|------|--------|
| `openAuthModal()` | 打开登录/注册模态框 | 无 | void |
| `closeAuthModal()` | 关闭登录/注册模态框 | 无 | void |
| `switchToLogin()` | 切换到登录面板 | 无 | void |
| `switchToRegister()` | 切换到注册面板 | 无 | void |
| `sendVerifyCode()` | 发送验证码（模拟） | 无 | void |
| `handleLogin()` | 处理登录逻辑 | event | void |
| `handleRegister()` | 处理注册逻辑 | event | void |
| `addToCart()` | 添加商品到购物车 | productId, name, price | void |
| `updateCart()` | 更新购物车显示 | 无 | void |
| `toggleCart()` | 切换购物车侧边栏 | 无 | void |
| `showFooterModal()` | 显示页脚详情弹窗 | contentId | void |

**表单验证规则**
- 用户名：必填，长度限制
- 密码：必填，6-20位
- 手机号：格式验证（11位数字）
- 验证码：6位数字，模拟发送
- 确认密码：与密码一致

---

### 4.2 文创定制服务模块 (文创定制服务.html)

#### 4.2.1 页面结构
```
Header (头部导航)
  ├── Logo: 甲骨文文创
  ├── 导航: 产品展示 / 个性定制
  └── 购物车图标

Banner (横幅)
  └── 标题 + 描述 + 立即定制按钮

产品展示区 (Products)
  ├── 甲骨文T恤 (¥129)
  ├── 甲骨文马克杯 (¥89)
  ├── 甲骨文笔记本 (¥59)
  └── 甲骨文帆布包 (¥79)

个性定制区 (Customization)
  ├── 预览区: 实时预览定制效果
  └── 控制面板:
      ├── 产品类型选择
      ├── 甲骨文字符选择 (12个字符)
      ├── 自定义文字输入
      ├── 颜色选择 (5种颜色)
      └── 定制备注

购物车侧边栏 (Cart Modal)
  └── 商品列表 + 总价 + 结算按钮

Footer (页脚)
  └── 版权信息
```

#### 4.2.2 核心JavaScript功能

**定制功能数据**
```javascript
// 产品类型与价格映射
switch(productType.value) {
    case 't-shirt':  price = 129; break;
    case 'mug':      price = 89;  break;
    case 'notebook': price = 59;  break;
    case 'bag':      price = 79;  break;
}
// 自定义文字附加费用: +¥20
```

**主要函数说明**
| 函数名 | 功能 | 参数 | 返回值 |
|--------|------|------|--------|
| `updateCart()` | 更新购物车UI和计数 | 无 | void |
| 匿名事件处理函数 | 选择甲骨文字符并更新预览 | click event | void |
| 匿名事件处理函数 | 选择颜色并更新预览 | click event | void |
| 匿名事件处理函数 | 添加预设产品到购物车 | click event | void |
| 匿名事件处理函数 | 添加定制产品到购物车 | click event | void |

**购物车数据结构**
```javascript
cartItems = [
    {
        name: "定制T恤",       // 商品名称
        price: 149,            // 价格（含定制费）
        oracleChar: "𓃒",       // 甲骨文字符
        customText: "自定义文字" // 自定义文字（可选）
    }
]
```

---

### 4.3 甲骨文书写练习模块 (甲骨文书写练习.html)

#### 4.3.1 页面结构
```
Header (标题区)
  └── 标题 + 副标题

使用说明 (Instructions)
  └── 5步操作指南

主内容区 (Main Content)
  ├── 书写区域 (Writing Area)
  │   ├── 工具栏: 清除 / 演示 / 提示
  │   ├── Canvas画布 (400px高度)
  │   └── 反馈文字
  └── 模板区域 (Template Area)
      ├── 字符网格 (8个字符)
      │   ├── 人 / 日 / 月 / 水
      │   └── 火 / 木 / 山 / 雨
      └── 字符信息面板

Footer (页脚)
  └── 版权信息
```

#### 4.3.2 核心JavaScript功能

**Canvas绘图系统**
```javascript
// 画布配置
ctx.lineWidth = 3;           // 线条宽度
ctx.lineCap = 'round';       // 线帽样式
ctx.lineJoin = 'round';      // 连接点样式
ctx.strokeStyle = '#8B4513'; // 线条颜色（棕色）

// 书写状态
let isDrawing = false;       // 是否正在绘制
let lastX = 0, lastY = 0;    // 上一个坐标点
let currentCharacter = '';   // 当前选中的字符
```

**主要函数说明**
| 函数名 | 功能 | 参数 | 返回值 |
|--------|------|------|--------|
| `resizeCanvas()` | 调整Canvas尺寸以适应容器 | 无 | void |
| `startDrawing(e)` | 开始绘制（mousedown/touchstart） | event | void |
| `draw(e)` | 绘制过程中（mousemove/touchmove） | event | void |
| `stopDrawing()` | 结束绘制（mouseup/touchend） | 无 | void |
| `getCoordinates(e)` | 获取鼠标/触摸坐标（兼容处理） | event | [x, y] |
| `clearCanvas()` | 清空画布 | 无 | void |
| `demoCharacter()` | 演示当前字符的标准写法 | 无 | void |
| `getCharacterClass(char)` | 获取字符对应的CSS类名 | char (string) | string |
| `showHint()` | 显示当前字符的含义提示 | 无 | void |
| `evaluateWriting()` | 简单评估书写效果（随机反馈） | 无 | void |

**支持的甲骨文字符**
| 汉字 | CSS类名 | 字形说明 |
|------|---------|----------|
| 人 | `oracle-human` | 侧面站立的人形 |
| 日 | `oracle-sun` | 太阳的形状，中间一横 |
| 月 | `oracle-moon` | 月牙形状 |
| 水 | `oracle-water` | 流动的水（两道横线） |
| 火 | `oracle-fire` | 火焰升腾的形状 |
| 木 | `oracle-tree` | 树木形状（树干+树冠） |
| 山 | `oracle-mountain` | 两座山峰 |
| 雨 | `oracle-rain` | 天空下雨（上框下三滴） |

**CSS甲骨文绘制原理**
使用CSS `::before` 和 `::after` 伪元素结合 `border`、`border-radius` 等属性绘制甲骨文字形，无需图片资源。每个字符对应一个CSS类，分为小尺寸（网格展示）和大尺寸（演示用）两套。

---

### 4.4 甲骨文猜字游戏模块 (甲骨文猜字游戏.html)

#### 4.4.1 页面结构
```
Header (标题区)
  └── 标题 + 描述

游戏信息栏 (Game Info)
  ├── 得分
  └── 进度 (1/10)

游戏区域 (Game Area)
  ├── 甲骨文展示区 (左)
  │   └── CSS绘制的甲骨文字形
  └── 选项区 (右)
      └── 4个汉字选项按钮

反馈区 (Feedback)
  └── 答题结果提示

控制按钮 (Controls)
  ├── 下一题按钮
  └── 重新开始按钮

游戏说明 (Instructions)
  └── 4条游戏规则
```

#### 4.4.2 核心JavaScript功能

**游戏数据结构**
```javascript
const oracleData = [
    { 
        oracle: "人",           // 正确答案汉字
        options: ["人","大","天","木"], // 四个选项
        answer: "人",           // 正确答案
        element: '<div class="oracle-human"></div>' // 图形HTML
    },
    // ... 共10道题（8种字符，有重复）
];
```

**游戏状态变量**
```javascript
let currentQuestion = 0;   // 当前题目索引
let score = 0;             // 当前得分
let gameCompleted = false; // 游戏是否完成
```

**主要函数说明**
| 函数名 | 功能 | 参数 | 返回值 |
|--------|------|------|--------|
| `initGame()` | 初始化游戏，重置分数和进度 | 无 | void |
| `loadQuestion()` | 加载当前题目，显示图形和选项 | 无 | void |
| `checkAnswer(selectedOption, optionEl)` | 检查答案是否正确，更新分数 | selectedOption, optionEl | void |
| `nextQuestion()` | 进入下一题或结束游戏 | 无 | void |

**游戏规则**
- 共10道题目
- 每题4个选项
- 答对得10分，答错不扣分
- 选项随机排序
- 答题后显示正确/错误标记
- 完成后显示最终得分

---

### 4.5 甲骨文翻译挑战模块 (甲骨文翻译挑战.html)

#### 4.5.1 页面结构
```
Header (标题区)
  └── 标题 + 副标题

统计信息栏 (Stats Area)
  ├── 得分
  ├── 进度 (1/5)
  └── 准确率

挑战区域 (Challenge Area)
  ├── 甲骨文段落区 (左)
  │   ├── 甲骨文文本
  │   └── 段落背景说明
  └── 翻译输入区 (右)
      ├── 文本输入框
      └── 提示/提交按钮

反馈区 (Feedback Area - 默认隐藏)
  ├── 得分显示
  ├── 用户翻译 vs 参考翻译对比
  ├── 详细解释
  └── 下一段落按钮

结果弹窗 (Result Overlay)
  ├── 最终得分
  ├── 评价消息
  └── 重新开始按钮

Footer (页脚)
  └── 版权信息
```

#### 4.5.2 核心JavaScript功能

**段落数据结构**
```javascript
const oraclePassages = [
    {
        text: "今日雨其自西来",           // 甲骨文文本
        reference: "今天下雨，雨水从西方而来。", // 参考翻译
        explanation: "这是一段关于天气的甲骨文记载...", // 简短背景
        detailed: "这段甲骨文记载了商代某日的天气情况...", // 详细解释
        keywords: ["今天", "下雨", "西方", "来"], // 关键词
        difficulty: 1 // 难度等级 1-5
    },
    // ... 共5段，难度递增
];
```

**游戏状态变量**
```javascript
let score = 0;             // 总得分
let currentPassage = 0;    // 当前段落索引
let totalAccuracy = 0;     // 累计准确率
let isGameActive = true;   // 游戏是否进行中
```

**主要函数说明**
| 函数名 | 功能 | 参数 | 返回值 |
|--------|------|------|--------|
| `initGame()` | 初始化游戏，重置所有状态 | 无 | void |
| `updateStats()` | 更新得分、进度、准确率显示 | 无 | void |
| `loadPassage()` | 加载当前段落内容 | 无 | void |
| `submitTranslation()` | 提交翻译，计算得分 | 无 | void |
| `calculateScore(userTranslation, passage)` | 计算翻译得分和准确率 | userTranslation, passage | {score, accuracy} |
| `nextPassage()` | 进入下一段落或结束 | 无 | void |
| `showResults()` | 显示最终结果弹窗 | 无 | void |
| `showHint()` | 显示关键词提示 | 无 | void |

**评分算法**
```
关键词匹配数 ÷ 总关键词数 × 100% = 准确率
基础分 = 难度等级 × 10
实际得分 = 基础分 × (准确率 / 100)

例：难度1（10分基础分），匹配2/4关键词 = 50%准确率 = 5分
```

**难度等级分布**
| 段落 | 难度 | 基础分 | 主题 |
|------|------|--------|------|
| 第1段 | 1 | 10分 | 天气 |
| 第2段 | 2 | 20分 | 占卜 |
| 第3段 | 3 | 30分 | 祭祀 |
| 第4段 | 4 | 40分 | 抓捕 |
| 第5段 | 5 | 50分 | 天气预测 |

**最终评价标准**
- ≥120分：甲骨文大师
- ≥80分：不错的水平
- ≥50分：有一定了解
- <50分：继续努力

---

### 4.6 产品详情页模块

#### 4.6.1 通用结构（适用于所有产品详情页）
```
Header (头部横幅)
  └── 品牌名 + 标语

产品展示区 (Product Showcase)
  ├── 产品图片区 (左)
  │   └── 主图 + 更多图片占位
  └── 产品详情区 (右)
      ├── 产品标题
      ├── 产品描述
      ├── 价格
      └── 产品特色列表

订购表单 (Order Form)
  ├── 收货人姓名
  ├── 联系电话
  ├── 收货地址
  ├── 购买数量（加减按钮）
  ├── 包装选项（标准/精美礼盒/豪华收藏）
  ├── 留言备注
  └── 提交订单按钮

Footer (页脚)
  └── 版权 + 联系方式
```

#### 4.6.2 产品列表
| 产品名称 | 价格 | 对应文件 |
|----------|------|----------|
| 甲骨文创意书签 | ¥36 | 甲骨文书签.html |
| 甲骨文创意U盘 | ¥98 | 甲骨文创意U盘.html |
| 甲骨文笔记本 | ¥48 | 甲骨文笔记本.html |
| 甲骨文玩偶 | ¥78 | 甲骨文玩偶.html |

#### 4.6.3 核心JavaScript功能
- 数量加减控制（1-10件）
- 表单提交验证
- 订单确认弹窗
- 表单重置

---

## 5. 关键功能与技术实现

### 5.1 Canvas绘图系统
**所在文件**：甲骨文书写练习.html

**技术要点**：
1. **双端支持**：同时支持鼠标事件和触摸事件，适配PC和移动端
2. **坐标转换**：触摸事件需通过 `getBoundingClientRect()` 计算相对坐标
3. **响应式画布**：画布尺寸随容器大小动态调整
4. **连续绘制**：通过记录上一坐标点，使用 `moveTo()` + `lineTo()` 实现连续线条

**事件绑定**：
```javascript
// 鼠标事件
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

// 触摸事件
canvas.addEventListener('touchstart', startDrawing);
canvas.addEventListener('touchmove', draw);
canvas.addEventListener('touchend', stopDrawing);
```

### 5.2 CSS纯图形甲骨文绘制
**应用页面**：书写练习、猜字游戏、文创定制

**实现原理**：
使用CSS伪元素（`::before`、`::after`）配合 `border`、`border-radius`、`position` 等属性，以纯CSS方式绘制甲骨文字形，无需图片资源。

**优点**：
- 无需加载图片，性能更好
- 可通过CSS变量轻松调整颜色和大小
- 缩放不失真

**字符分类**：
- 小尺寸版（`.oracle-xxx`）：60-80px，用于列表展示
- 大尺寸版（`.demo-xxx`）：120-160px，用于演示预览

### 5.3 模态框与侧边栏系统
**实现方式**：纯CSS + JavaScript类切换

**模态框类型**：
| 类型 | 样式类 | 出现方式 | 用途 |
|------|--------|----------|------|
| 居中模态框 | `.modal` | 居中淡入 | 登录/注册、页脚详情 |
| 侧边栏 | `.cart-modal` | 右侧滑入 | 购物车 |
| 全屏覆盖层 | `.result-overlay` | 淡入 | 游戏结果 |
| 炫酷弹窗 | `.footer-modal` | 缩放+模糊 | 页脚详情（主页） |

**动画效果**：
- 淡入淡出（opacity）
- 滑入滑出（transform: translateX/Y）
- 缩放动画（transform: scale）
- 毛玻璃背景（backdrop-filter: blur）

### 5.4 用户认证系统（模拟）
**所在文件**：甲骨文创意学习与文创平台3.html

**功能特性**：
1. **登录/注册切换**：单模态框内切换面板
2. **表单验证**：前端验证用户名、密码、手机号格式
3. **验证码模拟**：6位数字验证码，60秒倒计时
4. **密码强度**：长度验证（6-20位）
5. **错误提示**：实时显示错误信息，带抖动动画
6. **注册成功**：成功后显示成功界面，可跳转登录

**数据持久化**：当前仅内存存储，刷新页面数据丢失（可扩展为LocalStorage）

### 5.5 购物车系统
**实现方式**：数组存储 + DOM动态渲染

**购物车操作**：
- 添加商品
- 数量增减（部分页面）
- 总价计算
- 商品列表渲染

**数据结构**：
```javascript
// 主页购物车
cart = [{id, name, price, quantity, image}]

// 定制服务购物车
cartItems = [{name, price, oracleChar, customText}]
```

### 5.6 响应式设计
**断点设置**：
- 桌面端：> 768px
- 平板/移动端：≤ 768px
- 小屏移动端：≤ 480px（翻译挑战页）

**响应式策略**：
1. Flex布局换行：`flex-wrap: wrap`
2. Grid自适应列数：`grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`
3. 导航栏隐藏：移动端隐藏导航链接
4. 购物车全宽：移动端购物车占满屏幕
5. 字体大小调整：根据屏幕宽度调整字号

---

## 6. 数据结构与模拟数据

### 6.1 用户数据
```javascript
mockUsers = [
    {
        username: 'user1',      // 用户名
        password: 'pass1',      // 密码（明文存储，仅演示）
        name: '用户一',          // 显示名称
        phone: '13800138000'    // 手机号
    }
]
```

### 6.2 产品数据（主页）
```javascript
mockProducts = [
    { id: 1, name: '甲骨文创意T恤', price: 168, image: 'product1.jpg' },
    { id: 2, name: '甲骨文笔记本', price: 48, image: 'product2.jpg' },
    { id: 3, name: '甲骨文书签套装', price: 36, image: 'product3.jpg' },
    { id: 4, name: '甲骨文手机壳', price: 78, image: 'product4.jpg' }
]
```

### 6.3 甲骨文字符映射表
| 汉字 | CSS类 | 类型 | 象形含义 |
|------|-------|------|----------|
| 人 | human | 象形 | 侧面站立的人 |
| 木 | tree | 象形 | 树木 |
| 日 | sun | 象形 | 太阳 |
| 月 | moon | 象形 | 月亮 |
| 水 | water | 象形 | 流水 |
| 火 | fire | 象形 | 火焰 |
| 山 | mountain | 象形 | 山峰 |
| 雨 | rain | 象形 | 下雨 |

### 6.4 翻译挑战段落数据
见 4.5.2 节。

---

## 7. 样式系统

### 7.1 设计主题
**品牌色系**（古典中国风）：
| 变量名 | 色值 | 用途 |
|--------|------|------|
| `--primary-color` | #8c5e3c | 主色调（棕色） |
| `--secondary-color` | #d4af37 | 强调色（金色） |
| `--light-color` | #f5f1e6 | 背景色（米白） |
| `--dark-color` | #5a3921 | 深色（深棕） |
| `--text-color` | #333 | 正文文字 |
| `--success-color` | #28a745 | 成功状态 |
| `--error-color` | #dc3545 | 错误状态 |

**字体**：
- 主要字体："Microsoft YaHei", "SimSun", sans-serif
- 古风字体："SimSun", "STKaiti", serif（部分页面）

### 7.2 各页面风格对比
| 页面 | 主色调 | 字体风格 | 整体风格 |
|------|--------|----------|----------|
| 主页 | #8c5e3c + 金色 | 微软雅黑+宋体 | 现代古风 |
| 文创定制 | #8a7355 (卡其色) | 宋体+楷体 | 古典雅致 |
| 书写练习 | #8B4513 (赭色) | 微软雅黑 | 简洁教育风 |
| 猜字游戏 | #5c3d2e (深棕) | 微软雅黑 | 游戏化风格 |
| 翻译挑战 | #7a5c3c (棕色) | 宋体+楷体 | 古朴学术风 |
| 产品详情页 | #8B4513 (赭色) | 微软雅黑+宋体 | 电商风格 |

### 7.3 动画效果汇总
| 动画名称 | CSS属性 | 应用场景 |
|----------|---------|----------|
| `fadeIn` | opacity | 表单切换 |
| `shake` | transform: translateX | 错误提示 |
| `modalSlideUp` | transform + filter | 页脚弹窗 |
| `shine` | transform: translate | 弹窗头部光泽 |
| `titleSlideIn` | transform + filter | 弹窗标题 |
| `pulse` | transform: scale | 列表项图标 |
| Hover过渡 | transform: translateY | 卡片、按钮 |

---

## 8. 运行方式与部署指南

### 8.1 本地运行

**方式一：直接打开（最简单）**
1. 找到项目文件夹中的 `甲骨文创意学习与文创平台3.html`
2. 双击文件，用浏览器打开即可
3. 推荐浏览器：Chrome / Edge / Firefox 最新版本

**方式二：本地服务器（推荐）**
```bash
# 使用 Python 3 启动
cd /workspace
python3 -m http.server 8000

# 或使用 Node.js (需先安装 http-server)
npx http-server -p 8000

# 访问地址
# http://localhost:8000/甲骨文创意学习与文创平台3.html
```

### 8.2 部署到服务器

**静态文件部署**：
项目为纯静态网站，可部署到任何静态文件服务器：

1. **Nginx**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/project;
    index 甲骨文创意学习与文创平台3.html;
}
```

2. **GitHub Pages**
   - 将代码推送到GitHub仓库
   - 在Settings中启用Pages
   - 选择main分支作为源

3. **Vercel / Netlify**
   - 直接拖拽文件夹到平台
   - 或连接Git仓库自动部署

### 8.3 入口文件
**主入口**：`甲骨文创意学习与文创平台3.html`

建议配置服务器将此文件设为默认首页，或重命名为 `index.html`。

### 8.4 浏览器兼容性
| 浏览器 | 最低版本 | 备注 |
|--------|----------|------|
| Chrome | 80+ | 完全支持 |
| Edge | 80+ | 完全支持 |
| Firefox | 75+ | 完全支持 |
| Safari | 13+ | 基本支持，部分CSS效果可能有差异 |
| IE | - | 不支持 |

---

## 9. 依赖关系

### 9.1 外部依赖

| 依赖名称 | 版本 | 引入方式 | 用途 |
|----------|------|----------|------|
| Font Awesome | 6.4.0 | CDN链接 | 图标库（购物车、心形、用户等图标） |
| Google Fonts | - | 无 | 未使用，全部系统字体 |

**Font Awesome CDN地址**：
```
https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css
```

**使用的图标**：
- `fa-shopping-cart` - 购物车
- `fa-heart` / `far fa-heart` - 收藏/喜欢
- `fa-spinner fa-spin` - 加载动画
- `fa-check-circle` - 成功图标

### 9.2 内部页面链接关系

```
主页 (甲骨文创意学习与文创平台3.html)
  ├── 学习资源外链 (B站、字典网站、文献网站)
  ├── 文创产品链接
  │   ├── 甲骨文创意U盘.html
  │   ├── 甲骨文笔记本.html
  │   ├── 甲骨文书签.html
  │   └── 甲骨文玩偶.html
  ├── 甲骨文字展示外链 (B站视频)
  └── 互动学习链接
      ├── 甲骨文猜字游戏.html
      ├── 甲骨文书写练习.html
      └── 甲骨文翻译挑战.html

文创定制服务.html (独立入口)
  └── 购物车功能 (本地)

各产品详情页
  └── 返回主页 (通过浏览器返回)
```

---

## 10. 扩展开发指南

### 10.1 添加新的甲骨文字符

**步骤**：
1. 在CSS中添加新字符的绘制样式（小尺寸和大尺寸两套）
2. 在相关页面的数据数组中添加字符数据
3. 在HTML中添加字符元素（如需要）

**参考样式模板**：
```css
.oracle-xxx {
    width: 60px;
    height: 60px;
    position: relative;
}
.oracle-xxx::before {
    content: "";
    position: absolute;
    /* 绘制主体部分 */
}
.oracle-xxx::after {
    content: "";
    position: absolute;
    /* 绘制辅助部分 */
}
```

### 10.2 添加新产品

**产品详情页模板**：
复制现有产品详情页，修改以下内容：
- 页面标题
- 产品图片路径
- 产品名称、描述、价格
- 产品特色列表

**主页添加产品卡片**：
在 `products` 区域添加新的 `product-card` div，修改图片、名称、价格、链接。

### 10.3 添加新游戏/学习模块

**建议结构**：
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>模块标题</title>
    <style>
        /* 样式 */
    </style>
</head>
<body>
    <!-- 页面内容 -->
    <script>
        // 交互逻辑
    </script>
</body>
</html>
```

**在主页添加入口**：
在 `interactive-learning` 区域添加新的 `learning-option` 卡片。

### 10.4 后端集成建议

当前项目为纯前端，如需后端支持，建议：

1. **用户系统**：
   - 接入后端API替代 mockUsers
   - 使用 Token 认证（JWT）
   - 数据持久化到数据库

2. **购物车**：
   - 购物车数据同步到后端
   - 接入支付系统（微信/支付宝）

3. **游戏数据**：
   - 用户成绩排行榜
   - 学习进度记录
   - 更多题目动态加载

### 10.5 代码优化建议

1. **样式抽离**：将公共样式提取为独立CSS文件
2. **脚本抽离**：将公共功能（如购物车、模态框）提取为JS模块
3. **组件化**：使用Vue/React等框架重构，提高复用性
4. **构建工具**：引入Vite/Webpack，支持模块化开发
5. **性能优化**：图片懒加载、CDN加速

---

## 附录：快速参考

### A. 页面路由速查
| 功能 | 文件名 | 入口位置 |
|------|--------|----------|
| 首页 | 甲骨文创意学习与文创平台3.html | 主入口 |
| 文创定制 | 文创定制服务.html | 页脚-定制服务 |
| 书写练习 | 甲骨文书写练习.html | 互动学习区 |
| 猜字游戏 | 甲骨文猜字游戏.html | 互动学习区 |
| 翻译挑战 | 甲骨文翻译挑战.html | 互动学习区 |
| 书签详情 | 甲骨文书签.html | 文创产品区 |
| U盘详情 | 甲骨文创意U盘.html | 文创产品区 |
| 笔记本详情 | 甲骨文笔记本.html | 文创产品区 |
| 玩偶详情 | 甲骨文玩偶.html | 文创产品区 |

### B. 颜色速查表
| 颜色名 | HEX | 用途 |
|--------|-----|------|
| 主棕色 | #8c5e3c / #8B4513 | 导航、按钮主色 |
| 金色 | #d4af37 | 强调色、价格 |
| 米白色 | #f5f1e6 / #f9f3e9 | 背景色 |
| 深棕色 | #5a3921 / #5d4c35 | 深色文字、页脚 |
| 卡其色 | #d4c6b0 / #e8dfd1 | 次级背景 |

---

**文档版本**：v1.0  
**生成日期**：2025年  
**适用项目**：甲骨文创意学习与文创平台
