import jieba
from collections import Counter
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import os
import sys
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['font.family'] = 'SimHei'

def get_font_path():
    """
    获取可用的中文字体路径
    
    Returns:
        str: 字体文件路径
    """
    # 首先检查当前目录
    possible_fonts = ['simhei.ttf', 'SimHei.ttf', 'simhei.TTF']
    for font in possible_fonts:
        if os.path.exists(font):
            return font
    
    # 如果当前目录没有，检查系统字体目录
    if sys.platform == 'win32':
        # Windows 系统字体目录
        system_fonts = [
            'C:\\Windows\\Fonts\\simhei.ttf',
            'C:\\Windows\\Fonts\\SimHei.ttf',
            'C:\\Windows\\Fonts\\msyh.ttc',  # 微软雅黑
            'C:\\Windows\\Fonts\\msyh.ttf',
        ]
    elif sys.platform == 'darwin':
        # macOS 系统字体目录
        system_fonts = [
            '/Library/Fonts/SimHei.ttf',
            '/System/Library/Fonts/PingFang.ttc',
        ]
    else:
        # Linux 系统字体目录
        system_fonts = [
            '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        ]
    
    for font in system_fonts:
        if os.path.exists(font):
            return font
    
    return None

def analyze_word_frequency(text, top_n=20):
    """
    分析文本词频
    
    Args:
        text (str): 输入文本
        top_n (int): 返回前N个高频词
        
    Returns:
        list: 词频统计结果，格式为[(word, count), ...]
    """
    words = jieba.lcut(text)
    word_counts = Counter(words)
    
    # 过滤停用词和单字
    stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去',
                  '你', '会', '着', '没有', '看', '好', '自己', '这', '那', '，', '。', '、', '和', ' ', '“', '”'}
    
    filtered_words = {}
    for word, count in word_counts.items():
        if len(word) > 1 and word not in stop_words and not word.isspace():
            filtered_words[word] = count
    
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def generate_wordcloud(text, mask_image_path, output_image_path, max_words=200):
    """
    生成中国地图形状的词云图
    
    Args:
        text (str): 输入文本
        mask_image_path (str): 中国地图蒙版图片路径
        output_image_path (str): 词云图输出路径
        max_words (int): 词云图中显示的最大词数
        
    Returns:
        list: 词频统计结果
    """
    # 分析词频
    word_freq = analyze_word_frequency(text, top_n=100)
    
    print("前20个高频词:")
    for i, (word, count) in enumerate(word_freq[:20], 1):
        print(f"{i:2d}. {word}: {count}")
    
    # 生成词云
    from wordcloud import WordCloud
    
    china_mask = imageio.imread(mask_image_path)
    font_path = get_font_path()
    
    wordcloud = WordCloud(
        font_path=font_path,
        width=800,
        height=600,
        background_color='white',
        mask=china_mask,
        max_words=max_words,
        max_font_size=100,
        min_font_size=10,
        random_state=42,
        collocations=False
    )
    
    word_freq_dict = dict(word_freq)
    wordcloud.generate_from_frequencies(word_freq_dict)
    
    # 显示和保存词云图
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('中国地图形状词云图', fontsize=16, pad=20)
    
    plt.savefig(output_image_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"词云图已保存至: {output_image_path}")
    
    return word_freq

def process_text_file(txt_file_path, mask_image_path, output_image_path):
    """
    处理文本文件并生成词云
    
    Args:
        txt_file_path (str): 文本文件路径
        mask_image_path (str): 中国地图蒙版图片路径
        output_image_path (str): 词云图输出路径
        
    Returns:
        list: 词频统计结果
    """
    # 检查文件是否存在
    if not os.path.exists(txt_file_path):
        print(f"错误: 文件 {txt_file_path} 不存在")
        return None
    if not os.path.exists(mask_image_path):
        print(f"错误: 图片文件 {mask_image_path} 不存在")
        return None
    
    # 读取文本文件
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # 生成词云
    return generate_wordcloud(text, mask_image_path, output_image_path)

if __name__ == "__main__":
    # 示例用法
    current_dir = os.path.dirname(os.path.dirname(__file__))
    txt_file = os.path.join(current_dir, 'data', '2025年政府工作报告.txt')
    china_mask = os.path.join(current_dir, 'assets', 'china.jpg')
    output_image = os.path.join(current_dir, 'results', 'china_wordcloud.png')
    
    result = process_text_file(txt_file, china_mask, output_image)
