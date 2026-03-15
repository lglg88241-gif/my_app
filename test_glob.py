import glob

# 使用通配符寻找所有以 law_ 开头的 txt 文件
files = glob.glob("law_*.txt")

print(f"匹配到的法律文件列表: {files}")

# 进阶：用我们学过的列表推导式，只拿文件名不带路径
file_names = [f.split('\\')[-1] for f in files]
print(f"纯文件名清单: {file_names}")
