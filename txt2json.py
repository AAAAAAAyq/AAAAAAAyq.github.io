import json

with open('input.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()

# 将连续的大括号之间添加逗号，使其成为有效的 JSON 数组
content = content.replace('}\n{', '},\n{')

# 用方括号将整个内容包裹起来，形成一个 JSON 数组
content = f'[\n{content}\n]'

data = json.loads(content)

with open('data.json', 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=4)
