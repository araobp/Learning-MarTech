# 生成AI時代マーケティング部門エンジニアとしてのNLP/LLM自習

## 自習のためのNotebook

### NLTK

PythonでNLP何たるかを知るためNLTKからNLP始めた。

- [NLTK Basics](NLTK_Basics.ipynb)

### spaCy

パシフィコ横浜で開催されたEdgeTech+2023展示会でO'Reillyの"実践 自然言語処理"を購入。展示会で買うと20%ディスカウントで良い。この本でspaCyの存在を知った。NLP実践のための良書。この本をとかっかりにNLPの勉強を本格的に開始。

- [spaCyでNLPインスタンス生成](spaCy/spacy.ipynb)
- [spaCy and networkx](spaCy/spaCy_networkx.ipynb)
- [キーフレーズ抽出](spaCy/key_phrases.ipynb)
- [感情分析](spaCy/sentiment.ipynb)

### Transformers

LLMの勉強しようと書籍店で"大規模言語モデル入門"を購入。NLPの知識なく、いきなりこれを理解するのは無理。O'Reillyの"実践 自然言語処理"で勉強してからこの本を読む。これまで実践してきた音声処理や画像処理系AI(DNN/CNN)の経験が役にたちそう。AIって何？学習って何？学習ってすごく面倒で大変！その辺、十分に経験してきたので。

- [ChatGPTへネガポジコメント生成させChatGPTへネガポジ分析させる。精度がよくないので、他の手法でネガポジ分析させるため、ネガポジコメント文章を出力](./transformers/positive_negative.ipynb)
- [Tranformersでネガポジ分析など基本処理](transformers/TransformersBasics.ipynb)

---

## なぜマーケティング部門エンジニアがNLP/LLMを勉強する必要があるのか？

生成AIバズで数ヶ月生成AIを使い続けて気がついた。生成AIバカになるまえに、マーケティング部門エンジニアとして正しくデータ分析出来るようにならなければならない。

昨年は構造化データを扱うCRM/SFA系SaaSの方で仕事したが、構造化データの限界を感じてきた。非構造化データの活用の時代が来ている。非構造化データ、多くの企業ではBox上に存在するが、Box以外のSaaSにも存在し、データはSaaS間にまたがってバラバラに管理されている。こういうとき、ローコードやハブ型のPaaSで解決する動きもあるが、プログラミングに自信あるなら、実は、すべてのデータへアクセスする権限あるローカルPC上でNLP/LLMやったほうがセキュリティー上はうまく行く。

これからのマーケティング部門エンジニアに要求されるスキルは、Python numpy/pandas/matplotlibと自然言語処理NLP/LLMによる非構造化データ処理。テキストデータ、音声データ、画像データ、動画など。NLP/LLMのスキルが必須になる。

また、データ処理結果からコンテンツを半自動生成するプロセスも必要。よって画像処理や3DCG制作のスキルも必須。
https://github.com/araobp/blender-3d でスキル強化中。 

両者を結びつけて生成AI時代のマーケティングオートメーションが成立する。不思議なことに、すべてのツールがPythonによるプログラミングに対応。Pythonはワークフロー自動化のための糊付け言語でもある。

このプロジェクトではNLP/LLMスキル獲得のための自習を行う。

## 要注意

- 生成AIバカにならないこと。生成AIが得意なのは、生成。文章や画像を生成したり要約文を生成したり。適材適所でしかるべき自然言語処理を適用すること。
- 最初は小さなモデルで始めること。段階的に精度を上げていくこと。

## 二つのフレームワーク

- 最初にspaCyを勉強する。学習済みモデルがたくさんあり軽量動作するとのこと。
- 次にTransformersを勉強する。Deep Learningで動作が重いが精度は良いとのこと。

たぶん、私の場合、大半の作業はspaCyで完結するものと予測。

## 英語と日本語

英語と日本語が混在した環境で仕事する関係上、両言語に対応した手法を勉強する。

### spaCy

NLP開発環境 & NLPライブラリ

https://spacy.io/

### Transformers

NLP開発環境 & NLPライブラリ

https://huggingface.co/docs/transformers

### GiNZA

spaCy及びTransformers上で動作する日本語NLP。日本語TokenizerであるSudachiPy採用。

https://megagonlabs.github.io/ginza/

### ChatGPT

数ヶ月使ってみて、生成や要約は得意だけど分類は苦手そう。毎度、出力される結果が異なり、期待しない結果が出力される時も多く、私にとっては使いにくい。ChatGPTはアシスタントとして使うと良い。機械的な自然言語処理には他の手法、出力される結果に一貫性あるものを適用したい。

### ソーシャルネットワーク

spaCyのNLP結果をソーシャルグラフに乗せたい。マーケティングでは、誰が他の誰と繋がっているか、誰が何と繋がっているかが重要。グラフDBといえばneo4jだが、何か軽量動作するものはないか？昔使ったPythonのnetworkxをとりあえず使ってみて感触を掴む。

参考
- [Network of The Witcher | Relationship Extraction & Network Analysis with Spacy & NetworkX](https://youtu.be/fAHkJ_Dhr50)
- [How to create an Undirected Graph using Python](https://youtu.be/rldKl1CNx-A)
  
## 購入した教科書

NLP教科書
- [実践 自然言語処理](https://www.oreilly.co.jp/books/9784873119724/)
-- [サンプルコード](https://github.com/oreilly-japan/practical-nlp-ja)

日本語LLMの参考として
- [大規模言語モデル入門](https://gihyo.jp/book/2023/978-4-297-13633-8)

## 学習/実行環境

- MacBook Air 16GBRAMモデル
- Google Colab

## Transformersのモデル保存場所

```
/Users/<username>/.cache/huggingface/hub
```

モデルのサイズが大きいので、用済み後は必要に応じ削除する。

## その他参考

- [Natural Language Processing With Python's NLTK Package](https://realpython.com/nltk-nlp-python/#getting-started-with-pythons-nltk)
- [Python による日本語自然言語処理](https://www.nltk.org/book-jp/ch12.html)
- [感情分析のやり方が7割わかるようになる記事（初心者向け）（ソースコードあり）（GiNZA）](https://qiita.com/Mizuiro__sakura/items/94efccb5ba12046d17b0)
