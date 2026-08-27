# 🗺️ Python NLP 词云地图 | Python NLP WordCloud China Map

> **Python 爬虫 + NLP 词频分析 + 中国地图词云可视化——爬取数据、分词统计、词云生成、地图展示一体化流程。**
>
> *Python crawler + NLP word frequency + China map word cloud visualization — integrated pipeline of data crawling, segmentation, word cloud generation, map display.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| 🕷️ **数据爬虫** | Web Crawler | 自动爬取网页文本数据 |
| 🧠 **NLP 分析** | NLP Analysis | Jieba 分词 + 词频统计 |
| ☁️ **词云生成** | Word Cloud | 可视化高频关键词 |
| 🗺️ **中国地图** | China Map | 区域数据地图展示 |
| 🎨 **多维可视化** | Multi-Visual | 词云 + 地图 + 图表组合展示 |

---

## 🏆 技术栈 | Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-2.26+-blue?logo=python)
![Jieba](https://img.shields.io/badge/Jieba-0.42+-red?logo=python)
![WordCloud](https://img.shields.io/badge/WordCloud-1.8+-green?logo=python)
![Pyecharts](https://img.shields.io/badge/Pyecharts-2.0+-red?logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-red?logo=matplotlib)

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/Python-NLP-WordCloud-ChinaMap.git
cd Python-NLP-WordCloud-ChinaMap

# 1. 安装依赖
pip install -r requirements.txt

# 2. 爬取数据
python src/crawler.py --urls data/urls.txt --output data/raw.txt

# 3. NLP 分词与词频统计
python src/nlp_analysis.py --input data/raw.txt --output result/keywords.csv

# 4. 生成词云
python src/wordcloud_gen.py --keywords result/keywords.csv --output result/wordcloud.png

# 5. 生成中国地图
python src/china_map.py --data data/region_data.csv --output result/china_map.html

# 6. 综合报告
python generate_report.py
```

---

## 📂 项目结构 | Project Structure

```
Python-NLP-WordCloud-ChinaMap/
├── src/                       # 核心代码
│   ├── crawler.py             # 数据爬虫
│   ├── nlp_analysis.py        # NLP 分析
│   ├── wordcloud_gen.py       # 词云生成
│   ├── china_map.py           # 中国地图
│   └── data_clean.py          # 数据清洗
├── data/                      # 数据
├── result/                    # 结果输出
└── requirements.txt
```

---

## 🔬 核心实现 | Core Implementation

### NLP 词频分析 | NLP Word Frequency

```python
# Jieba 分词 + 词频统计
import jieba
import jieba.analyse
from collections import Counter

def analyze_keywords(text, top_n=50):
    """中文分词与关键词提取"""
    # 1. 加载自定义词典
    jieba.load_userdict('data/user_dict.txt')
    
    # 2. 载入停用词
    stopwords = set()
    with open('data/stopwords.txt', encoding='utf-8') as f:
        stopwords = {line.strip() for line in f}
    
    # 3. 分词并过滤
    words = [w for w in jieba.cut(text) 
             if w not in stopwords and len(w) > 1 and not w.isdigit()]
    
    # 4. 词频统计
    word_freq = Counter(words)
    
    # 5. TF-IDF 关键词
    tfidf_keywords = jieba.analyse.extract_tags(text, topK=top_n, withWeight=True)
    
    return word_freq, tfidf_keywords
```

---

## 📊 输出示例 | Output Example

```
☁️ 词云图 (高频关键词):
  人工智能  大数据  云计算  区块链  物联网
  5G  芯片  算法  模型  应用

🗺️ 中国地图热力图:
  北京 ████████████  68%
  上海 ██████████  55%
  深圳 ████████  48%
  杭州 ██████  35%
  ...
```

---

## 🎯 应用场景 | Use Cases

- 📰 **舆情分析**：热点新闻关键词分析
- 🛒 **市场调研**：用户评论词频分析
- 🧠 **NLP 教学**：分词、词云实战项目
- 🎨 **数据展示**：词云地图可视化作品
- 📊 **报告生成**：数据可视化报告

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **爬虫 + NLP + 词云地图一体化，Star ⭐ 让数据一目了然！**
