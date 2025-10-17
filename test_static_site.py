#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
静态网站文件结构验证脚本
"""

import os
import sys

# 定义需要验证的文件列表
required_files = [
    'index.html',
    'success.html',
    '.gitignore',
    'README.md',
    'package.json'
]

# 检查文件是否存在
def check_files():
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("[错误] 缺少以下必要文件:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    else:
        print("[成功] 所有必要文件都已存在")
        return True

# 检查HTML文件是否包含基本结构
def check_html_structure():
    html_files = ['index.html', 'success.html']
    issues = []
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if '<!DOCTYPE html>' not in content:
                    issues.append(f"{html_file}: 缺少DOCTYPE声明")
                if '<html' not in content:
                    issues.append(f"{html_file}: 缺少html标签")
                if '<head' not in content:
                    issues.append(f"{html_file}: 缺少head标签")
                if '<body' not in content:
                    issues.append(f"{html_file}: 缺少body标签")
        except Exception as e:
            issues.append(f"读取{html_file}时出错: {str(e)}")
    
    if issues:
        print("[警告] HTML文件结构检查发现问题:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("[成功] HTML文件结构检查通过")
    
    return len(issues) == 0

# 检查JavaScript功能是否存在
def check_javascript_functions():
    functions_to_check = {
        'index.html': ['handleFileSelection', 'processBtn.addEventListener', 'showMessage'],
        'success.html': ['getURLParams', 'initPageData', 'simulateDownload']
    }
    
    missing_functions = []
    
    for html_file, functions in functions_to_check.items():
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                for func in functions:
                    if func not in content:
                        missing_functions.append(f"{html_file}: 缺少{func}功能")
        except Exception as e:
            missing_functions.append(f"读取{html_file}时出错: {str(e)}")
    
    if missing_functions:
        print("[警告] JavaScript功能检查发现问题:")
        for issue in missing_functions:
            print(f"  - {issue}")
    else:
        print("[成功] JavaScript功能检查通过")
    
    return len(missing_functions) == 0

# 显示部署指南
def show_deployment_guide():
    print("\n=== 部署指南 ===")
    print("1. 初始化Git仓库（如果尚未初始化）:")
    print("   git init")
    print("2. 添加所有文件:")
    print("   git add .")
    print("3. 提交更改:")
    print("   git commit -m 'Initial commit'")
    print("4. 推送到GitHub（需要先在GitHub创建仓库）:")
    print("   git remote add origin https://github.com/yourusername/your-repo-name.git")
    print("   git push -u origin main")
    print("5. 在GitHub仓库设置中启用GitHub Pages:")
    print("   - 进入Settings > Pages")
    print("   - 选择main分支和根目录(/)")
    print("   - 点击Save")
    print("   - 几分钟后网站将可访问")

# 主函数
def main():
    print("开始验证静态网站文件结构...")
    
    # 检查文件存在性
    files_ok = check_files()
    
    # 检查HTML结构
    html_ok = check_html_structure()
    
    # 检查JavaScript功能
    js_ok = check_javascript_functions()
    
    # 总体评估
    if files_ok and html_ok and js_ok:
        print("\n✅ 静态网站验证通过！可以部署到GitHub Pages。")
        show_deployment_guide()
        return 0
    else:
        print("\n❌ 静态网站验证未完全通过，请检查上述问题。")
        return 1

if __name__ == "__main__":
    sys.exit(main())