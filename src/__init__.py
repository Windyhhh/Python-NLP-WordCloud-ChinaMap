# 政府工作报告爬虫与词云生成包
__version__ = "1.0.0"

from .crawler import crawl_report
from .nlp_wordcloud import process_text_file, analyze_word_frequency, generate_wordcloud

__all__ = [
    "crawl_report",
    "process_text_file",
    "analyze_word_frequency",
    "generate_wordcloud"
]
