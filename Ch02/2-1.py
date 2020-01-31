# Create by Zwlin
import re
line = 'asdf fjdk; afed, fjek,asdf,    foo'
# 多分隔符分割
res1 = re.split(r'[;,\s]\s*',line)
# 使用捕获组时分割时会同时提取分隔符
res2 =re.split(r'(;|,|\s)\s*',line)
# 若想使用括号，但不要分隔符，使用非捕获组
res3 = re.split(r'(?:;|,|\s)\s*',line)

print(res1)
print(res2)
print(res3)