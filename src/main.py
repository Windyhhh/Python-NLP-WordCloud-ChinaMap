import os
from crawler import crawl_report
from nlp_wordcloud import process_text_file

def main():
    """
    主函数，整合爬虫和词云生成功能
    """
    # 项目根目录
    root_dir = os.path.dirname(os.path.dirname(__file__))
    
    # 配置参数
    url = 'http://www.hprc.org.cn/wxzl/wxysl/lczf/shisijbg/202504/t20250408_5867286.html'
    data_dir = os.path.join(root_dir, 'data')
    assets_dir = os.path.join(root_dir, 'assets')
    results_dir = os.path.join(root_dir, 'results')
    
    # 确保目录存在
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)
    
    print("1. 开始爬取政府工作报告...")
    # 爬取报告
    report_file = crawl_report(url, data_dir)
    
    print("\n2. 开始生成词云图...")
    # 检查中国地图图片是否存在
    china_mask = os.path.join(assets_dir, 'china.jpg')
    if not os.path.exists(china_mask):
        print(f"错误: 中国地图图片 {china_mask} 不存在，请将图片放入assets目录")
        return
    
    # 生成词云
    output_image = os.path.join(results_dir, 'china_wordcloud.png')
    process_text_file(report_file, china_mask, output_image)
    
    print("\n✅ 所有任务完成！")
    print(f"📄 报告文件: {report_file}")
    print(f"🗺️  词云图: {output_image}")

if __name__ == "__main__":
    main()
