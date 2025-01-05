# AI-markdown-translator
Markdownをさまざまな言語に翻訳し、それぞれの新しいMarkdownファイルを作成します。

## 機能
- 翻訳中にすべてのMarkdownフォーマットと構造を保持
- 単一の実行で複数のターゲット言語をサポート
- 高品質な翻訳のためにOpenAIのGPT-3.5-turboモデルを使用
- コードブロック、URL、特殊文字を変更せずに保持
- 各ターゲット言語に対して別々の出力ファイルを作成

## 前提条件
- Python 3.6以上
- OpenAI APIキー

## インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/imhuiye/AI-markdown-translator.git
cd AI-markdown-translator
```

2. 必要な依存関係をインストール:
```bash
pip install -r requirements.txt
```

3. プロジェクトのルートディレクトリに`.env`ファイルを作成し、OpenAI APIの認証情報を記述:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
```

## 使用方法

基本的なコマンド構文は次のとおりです:
```bash
python translator.py <input_file> --source <source_lang> --target <target_langs>
```

パラメータ:
- `input_file`: 翻訳したいMarkdownファイルのパス
- `--source`: ソース言語コード（例: CNは中国語、ENは英語）
- `--target`: ターゲット言語コードのカンマ区切りリスト（例: EN,JP,KR）

例:
```bash
python translator.py README.md --source CN --target EN,JP
```

これにより、次のファイルが作成されます:
- `README_EN.md` (英語翻訳)
- `README_JP.md` (日本語翻訳)

## 言語コード
一般的な言語コード:
- EN: 英語
- CN: 中国語
- JP: 日本語
- KR: 韓国語
- FR: フランス語
- DE: ドイツ語
- ES: スペイン語

## 注意点
- 翻訳は、ヘッダー、リスト、コードブロック、リンク、フォーマットを含むすべてのMarkdown構文を保持します
- コードブロック内のコンテンツ（```または`で囲まれた部分）は翻訳されません
- OpenAI APIキーに十分なクレジットがあることを確認してください

## エラーハンドリング
スクリプトには以下のエラーハンドリングが含まれています:
- 無効なファイルパス
- APIエラー
- ファイルの読み取り/書き込みの問題
- 無効な言語コード

問題が発生した場合は、コンソール出力のエラーメッセージを確認して詳細を確認してください。