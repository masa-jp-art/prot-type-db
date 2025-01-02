# 概要
- Public このプロジェクトでは、OpenAI o1 proが出力したプロットタイプの分類データからデータベースを作り、ランダムに取り出したプロットのリファレンスから物語のプロットのアイデアを生成します。
- このプロジェクトは、ChatGPT Proで使用できる、OpenAIのo1 pro modeの検証を兼ねています

# 手順
- ChatGPT Proのo1 pro modeに、物語のプロットを分類させます
  - [prot-type.md](https://github.com/masa-jp-art/prot-type-db/blob/main/prot-type.md)
- 出力されたプロットタイプをスプレッドシートに転記してデータベースを作ります
  - [code-for-google-colab.py](https://github.com/masa-jp-art/prot-type-db/blob/main/code-for-google-colab.py)
- Google colabでプログラムを動かし、キャラクターとあらすじを生成します
  - [20250102-prot-type-snapshot](https://docs.google.com/spreadsheets/d/1vLihxLF6ICbKBCVnP6tBbZEoWA-eDNM095_UnNLsTyg/)
 
# 関連
- [OpenAI o1 pro mode検証:マンガのプロットタイプデータベースが作れるか](https://note.com/msfmnkns/n/nec75b5ce0db0)
