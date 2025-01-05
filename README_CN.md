# AI-markdown-translator
将 Markdown 文件翻译成多种语言，并为每种语言创建新的 Markdown 文件。

## 功能
- 在翻译过程中保留所有 Markdown 格式和结构
- 支持单次运行中翻译成多种目标语言
- 使用 OpenAI 的 GPT-3.5-turbo 模型进行高质量翻译
- 保持代码块、URL 和特殊字符不变
- 为每种目标语言创建单独的输出文件

## 前提条件
- Python 3.6 或更高版本
- OpenAI API 密钥 或使用支持 OpenAI 接口的大语言模型

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/imhuiye/AI-markdown-translator.git
cd AI-markdown-translator
```

2. 安装所需的依赖项：
```bash
pip install -r requirements.txt
```

3. 在项目根目录下创建一个 `.env` 文件，并填入你的 OpenAI API 凭证：
```
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
```

## 使用

基本命令语法如下：
```bash
python translator.py <input_file> --source <source_lang> --target <target_langs>
```

参数：
- `input_file`: 要翻译的 Markdown 文件的路径
- `--source`: 源语言代码（例如，CN 表示中文，EN 表示英文）
- `--target`: 目标语言代码的逗号分隔列表（例如，EN,JP,KR）

示例：
```bash
python translator.py README.md --source CN --target EN,JP
```

这将创建：
- `README_EN.md`（英文翻译）
- `README_JP.md`（日文翻译）

## 语言代码
常用语言代码：
- EN: 英文
- CN: 中文
- JP: 日文
- KR: 韩文
- FR: 法文
- DE: 德文
- ES: 西班牙文

## 注意事项
- 翻译会保留所有 Markdown 语法，包括标题、列表、代码块、链接和格式
- 代码块中的内容（由 ``` 或 ` 包围）不会被翻译
- 确保你的 OpenAI API 密钥有足够的额度用于翻译

## 错误处理
脚本包含以下错误处理：
- 无效的文件路径
- API 错误
- 文件读写问题
- 无效的语言代码

如果遇到任何问题，请查看控制台输出中的错误信息以获取更多详细信息。