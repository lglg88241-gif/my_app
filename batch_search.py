import glob
import os

# 1. 模拟准备：先创建几个不同的测试文件
files_to_create = ["case_1.txt", "case_2.txt", "law_update.log", "case_final.txt"]
for name in files_to_create:
    with open(name, "w", encoding="utf-8") as f:
        f.write(f"这是 {name} 的模拟内容")

print("--- 准备工作完成：模拟文件已生成 ---")

# 2. 实战：使用 glob 查找所有以 'case_' 开头的 .txt 文件
# * 是通配符，代表任意长度的字符
case_files = glob.glob("case_*.txt")

print(f"找到的所有案件文件: {case_files}")

# 3. 进阶：批量读取找到的文件内容
for file_path in case_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"读取文件 [{file_path}] -> 内容: {content}")