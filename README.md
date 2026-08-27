<div align="center">

# 🗺️ Python-NLP-WordCloud-ChinaMap

### Python crawler + NLP + China-map word cloud.

Crawl text, run word-frequency NLP, and render a China-map word cloud — all in one pipeline.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jieba](https://img.shields.io/badge/Jieba-NLP-4B77BE)](https://github.com/fxsjy/jieba)

</div>

---

**Python-NLP-WordCloud-ChinaMap** builds an end-to-end pipeline: a **crawler** collects text, **NLP** computes word frequency, and a **China-map word cloud** visualizes the result.

> [!NOTE]
> 中文项目：Python 爬虫 + NLP 词频 + 中国地图词云可视化。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Python-NLP-WordCloud-ChinaMap.git
cd Python-NLP-WordCloud-ChinaMap

pip install -r requirements.txt

# crawl text
python src/crawler.py

# run the full NLP + word-cloud pipeline
python src/main.py
```

Sample input (`data/2025年政府工作报告.txt`) and output (`results/china_wordcloud.png`) are included.

---

## Features

- **Crawler** — collect source text.
- **NLP word frequency** — segmentation and counting.
- **China-map word cloud** — geographic visualization.

---

## Project Structure

```
Python-NLP-WordCloud-ChinaMap/
├── src/                  # crawler.py, main.py, nlp_wordcloud.py
├── notebooks/            # executed notebook
├── data/                 # source text
└── results/              # china_wordcloud.png
```

---

## License

MIT — free to use, modify and distribute.
