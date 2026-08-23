import os
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def crawl_report(url, output_dir):
    """
    从指定URL爬取政府工作报告并保存到文件
    
    Args:
        url (str): 报告页面URL
        output_dir (str): 输出目录路径
        
    Returns:
        str: 保存的文件路径
    """
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取标题
    title_element = soup.find('h1')
    if title_element:
        title = title_element.text.strip()
        print(f"标题: {title}")
    else:
        print("未找到标题元素")
        title = "未知标题"
    
    # 提取正文内容
    content_element = soup.find('div', class_='TRS_Editor')
    if content_element:
        content = content_element.text.strip()
        print("正文内容已提取")
    else:
        print("未找到正文内容元素")
        content = "未知内容"
    
    # 保存到文件
    file_name = f"{title}.txt"
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(title + '\n\n' + content)
    
    print(f'爬取完成，内容已写入 {file_path} 文件')
    return file_path

if __name__ == "__main__":
    url = 'http://www.hprc.org.cn/wxzl/wxysl/lczf/shisijbg/202504/t20250408_5867286.html'
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    crawl_report(url, output_dir)
