# MarTech自習ノート

## Jupyter Notebook

### pandas

- [Titanicデータセット](etc/Titanic.ipynb)

### SQLite

SQLiteは埋め込み型のローカルデータベースなので、データの更新も検索もかなり高速。PandasとSQLiteの親和性も高く、中〜小規模なデータサイエンス活動にはうってつけ。

- [SQL](sql)

### NLTK

NLP自習の第１歩、NLP何たるかを知るためNLTKからNLP始めた。しかし、後で、今はAI使ったNLPが主流だと知った。仕事でNLTK使う機会はないが、NLPの勉強始める時はNLTKから始めた方が良い。

- [NLTK Basics](NLTK_Basics.ipynb)

### spaCy

- [spaCy](spaCy)

### Transformers

LLMの勉強しようと書籍店で"大規模言語モデル入門"を購入。NLPの知識なく、いきなりこれを理解するのは無理。O'Reillyの"実践 自然言語処理"で勉強してからこの本を読む。これまで実践してきた音声処理や画像処理系AI(DNN/CNN)の経験が役にたちそう。AIって何？学習って何？学習ってすごく面倒で大変！その辺、十分に経験してきたので。

学習済み感情分析モデルがHugging Faceのサイトに沢山あり。マーケティング部門では感情分析がかなり重要。

- [ChatGPTへネガポジコメント生成させChatGPTへネガポジ分析させる。精度がよくないので、他の手法でネガポジ分析させるため、ネガポジコメント文章を出力](./transformers/positive_negative.ipynb)
- [Tranformersでネガポジ分析など基本処理](transformers/TransformersBasics.ipynb)

## ブラウザインタフェース

自分がつくったものを、他のメンバーへ使ってもらわないと意味がない。プログラミング知識ない、Python触ったことない、それを前提に考えると、ブラウザから操作できるインタエースを提供する必要ある。

### vis.js/graphology.js

networkxだとブラウザ上での表現ができないので、networkxのデータを[vis.js](https://visjs.org/)へ取り込む必要あり。[pyvis](https://pyvis.readthedocs.io/en/latest/)もあるがvis.jsの機能をフルサポートしておらず、私にとっては都合が悪い。ここでは、pyvisとは逆で、vis.jsを埋め込んだHTML5からnetworx上のデータを取り込むアプローチを探る。JavaScriptのスクリプトを書けば実現できる。 

しかし、vis.jsは可視化はできるがグラフ理論実装されておらず、実践上では不都合が出てきた。ブラウザ上の操作でサブグラフをつくれるようなライブラリが必要。

[Cytoscape.js](https://js.cytoscape.org/)にはグラフ理論とビジュアリゼーションの両方が含まれていて良いが、少し評価してみたところビジュアリゼーションが弱い。vis.jsの方がインパクトあり。

よって、以下の組み合わせにした：
- [graphology.js](https://graphology.github.io/)でグラフ理論の処理
- vis.jsでビジュアリゼーション処理

### graphology.js や graphlogy standard library で使えそうなメソッド

#### [Subgraph](https://graphology.github.io/standard-library/operators.html#subgraph)

グラフから一部を切り出すのに使える。元ネットワークエンジニアの私としてはSubnetなりVPNなりVLANを意味する。

#### [Neigbors](https://graphology.github.io/iteration.html#neighbors-array)

あるキーワードと直接関連ある他のキーワードをリストアップするのに使える。元ネットワークエンジニアの私としては隣接ノード(Adjacent Node)を意味する。

#### [BFS](https://graphology.github.io/standard-library/traversal.html#bfs)

あるキーワードと関連ある（直接/間接）他のキーワードを、半径を指定してリストアップするのに使える。

#### [Shortest Path](https://graphology.github.io/standard-library/shortest-path.html) 

マーケティングの観点では、何と何が最短距離で関連しているか探すのに使える。元ネットワークエンジニアの私としてはOPSF(OPen Shortest path Fast)を連想する。

## 関係抽出

ナレッジグラフ生成に必要となる関係抽出、以下のモデルを試してみたが、性能がかなり良い。
- https://huggingface.co/ibm/knowgl-large

問題は、特定ドメイン固有の専門用語では関係抽出がうまく行かないこと。専用モデルの学習が必要になる。また、学習に必要十分なデータを揃えられない。

また、ここでは、ナレッジグラフ連動の検索エンジンを開発しているわけではなく、情報の整理やグルーピングをやりたいだけ。spaCyの範囲で出来る手法はないか？

最低限、ノード間依存関係とエッジのweightが必要。Weightの方、感情分析結果も反映させたい（ネットワークルーティングでいうコストに相当）。その程度ならspaCyのDependencyMatcherで実現出来ないか？探究中。。。

## Entity Linking

このプロジェクトでは、NERで抽出されたキーワードを Wikipedia (Knowledge Baseとしての) の該当ページへ hyperlink でリンクする程度の Entity Linking しか実現しない。

しかし、マーケティング部門では、製品紹介資料や客先向けプレゼン資料などから Knowledge Graph を構築出来ると良い。このプロジェクトでは、その手法については掘り下げないが、以下のツールなどを組み合わせて実現出来ること確認済み。

マーケティング部門であれば、以下のデータから固有表現抽出や関係抽出を行える。パワポ/PDF資料では関係抽出が難しいかもしれない。
- CRM/SFA/MA
- VoC/VoE
- その他資料
- 写真

多くのデータソースから固有表現を拾い上げることで、Named Entity Disambiguation (NED)も実現出来る。

## TF-IDF (Work in progress)

Betweennessを尺度にして、グラフからサブグラフを抽出したい。

Named Entityのネットワークを生成してみると、ある単語の頻度がやたら多くて目立つ場合がある。例えば自社名。自社名は重要だが、betweennessが突出して大きくなってしまうのを避けたい。TF-IDF(Term Frequency - Inverse Document Frequency)でうまく調整出来ないか？検討してみたい。

## PDF

マーケティング部門にある非構造化データといえば、エクセルの顧客コメント資料、パワポやPDFの資料、そして、画像や動画コンテンツ。これらをAIで分析すれば有用な何かが得られるはず。

- [PowerPointとPDFからデータ抽出](tools/ppt_pdf.ipynb) ... スライドがある程度構造化されていれば関係抽出しやすいが。。。

## Tools

- [言語認識](tools/LanguageIdentification.ipynb) ... 文章が短いと誤認識が起こる。
- [Image Captioning](tools/ImageCaptioning.ipynb) ... 認識性能の高さに驚いた！生成されたキャプションをNLPにかけて利用してみたい。
- [Matplotlib color map を HTML color listへ変換](tools/Colormap.ipynb) ... Networkのcommunity色分け用
- [Webスクレイピング](tools/WebScraping.ipynb) ... マーケティング部門所属エンジニアに必須なスキル。今回は Project Gutenberg の本(web版)からパラグラフ抽出を試みる。
- [YAML Database](tools/YAML_database.ipynb) ... 大量のドキュメントへNLP処理を行う際、その処理結果を保存するための簡易データベースを開発。

## 最後にライセンスの話

NLP関連では無償でも営利目的での利用を禁じるものが多い。

非営利の意味が解説されている：
- [クリエイティブ・コモンズとは？意味やクリエイティブ・コモンズ・ライセンスの利用法を解説](https://blog.hubspot.jp/marketing/copyright-creativecommons#:~:text=%E3%80%8CNC%E3%80%8D%EF%BC%88%E9%9D%9E%E5%96%B6%E5%88%A9%EF%BC%89,%E3%82%89%E3%82%8C%E3%82%8B%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82)
- [営利目的」とは？意味・具体例と「商用利用」「非営利」も解説](https://biz.trans-suite.jp/54496)

データ整理などの業務効率化に使う分には問題なさそう。利益を得るための活動をしてはならない。

## 参考

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

- MacBook Air 16GB RAMモデル
- Google Colab

※ Windows PC 8GB RAMモデルでも大半は動作する。

## Transformersのモデル保存場所

Macの場合
```
/Users/<username>/.cache/huggingface/hub
```

モデルのサイズが大きいので、用済み後は必要に応じ削除する。

## その他参考

- [Natural Language Processing With Python's NLTK Package](https://realpython.com/nltk-nlp-python/#getting-started-with-pythons-nltk)
- [Python による日本語自然言語処理](https://www.nltk.org/book-jp/ch12.html)
- [感情分析のやり方が7割わかるようになる記事（初心者向け）（ソースコードあり）（GiNZA）](https://qiita.com/Mizuiro__sakura/items/94efccb5ba12046d17b0)
- [How should I preprocess text for spaCy?](https://github.com/explosion/spaCy/discussions/10243)
- [seabornで日本語が文字化けする時の対処](https://kiseno-log.com/2021/03/13/seaborn%E3%81%A7%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%81%8C%E6%96%87%E5%AD%97%E5%8C%96%E3%81%91%E3%81%99%E3%82%8B%E6%99%82%E3%81%AE%E5%AF%BE%E5%87%A6/)
- [NER graphs](https://medium.com/@anoopjohny2000/ner-graphs-e79fb5247a95)
- [Knowledge Graph — A Powerful Data Science Technique to Mine Information from Text (with Python code)](https://prateekjoshi.medium.com/knowledge-graph-a-powerful-data-science-technique-to-mine-information-from-text-with-python-f8bfd217accc)
