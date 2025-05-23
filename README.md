# MarTech(Marketing Technolgies)自習ノート

普通のPCで動作するもの、かつ、無償で利用できるものに限定する。

## pandas

毎日、pandasを使って仕事中。。。

- [Titanicデータセット](etc/Titanic.ipynb)

## NLTK

NLP自習の第１歩、NLP何たるかを知るためNLTKからNLP始めた。しかし、後で、今はAI使ったNLP(例えばspaCy)が主流だと知った。仕事でNLTK使う機会はないが、NLPの勉強始める時はNLTKから始めた方が良い。

- [NLTK Basics](NLTK_Basics.ipynb)

## spaCy

もはや、これ抜きで、私の仕事は成立せず。定量化できない非構造化データに眠っているお宝を拾い上げるための手段。ChatGPTやGeminiをAPI経由で利用する際のデータ前処理向け（チャンク化や匿名化など）にも重宝。

- [spaCy](spaCy)

私の趣味の世界でつくったアプリ
- [Bach Network](https://github.com/araobp/bach-network)

## Transformers

学習済み感情分析モデルがHugging Faceのサイトに沢山あり。

- [ChatGPTへネガポジコメント生成させChatGPTへネガポジ分析させる。精度がよくないので、他の手法でネガポジ分析させるため、ネガポジコメント文章を出力](./transformers/positive_negative.ipynb)
- [Tranformersでネガポジ分析など基本処理](transformers/TransformersBasics.ipynb)

## Clustering VoC

VoCを埋め込みで数値化し, K-meansでクラスタリングし, t-SNEで埋め込みの次元を削減してクラスタリングの結果を可視化する。

- [Clustering VoC](clustering/ClusteringVoC.ipynb)

## SQLite

2024年の3月から仕事で盛んに使うようになった。SQLiteは埋め込み型のローカルデータベースなので、データの更新も検索もかなり高速。PandasとSQLiteの親和性も高く、中〜小規模なデータサイエンス活動にはうってつけ。

- [SQL](sql)

## PDF

マーケティング部門にある非構造化データといえば、エクセルの顧客コメント資料、パワポやPDFの資料、そして、画像や動画コンテンツ。これらをAIで分析すれば有用な何かが得られるはず。

- [PowerPointとPDFからデータ抽出](tools/ppt_pdf.ipynb) ... スライドがある程度構造化されていれば関係抽出しやすいが。。。

## PDFテキストハイライト

注意：この自習活動は[pdf-searchレポジトリ](https://github.com/araobp/pdf-search)へスピンアウト。これ以上、こちらは更新しない。

2024年GW自習活動はPDF全文検索とテキストハイライトに決めた。

- [PDFテキストハイライト実験](pdf_highlight/PDF_text_highlight.ipynb)

処理したデータを職場の同僚へウエブブラウザを介して見せたいとする。[Streamlit](https://streamlit.io/)も気になるが、JavaScript系のライブラリを使いたいのでFlaskでAPIサーバ作ることにした。その方が、後々、Salesforce等へソースコードの一部を再利用することが出来て良い(Salesforce, OutSystems, Mendixなど、ローコード開発基盤は、全て、HTML5(=JavaScript)でアプリをつくる)。

- [経済産業省の通商白書を全文検索するAPIサーバの計画](pdf_highlight/ApiServerDesign.ipynb)
- [アーキテクチャー図](https://docs.google.com/presentation/d/e/2PACX-1vT43IcCwEF3m27u_PwFEFjDMfFkqCZukqz485mm3Nsb-B7YTappdcZ-5lBnXVimDdqls0LkbXSlgtmp/pub?start=false&loop=false&delayms=3000)
- [MVCアプリ](pdf_highlight/App)

FlaskでMVCつくるときの参考：https://qiita.com/hiro_hiro_0425/items/e0a7a777f2772c3ac0ec

## Salesforce

Salesforce独自フレームワークや独自言語を覚えなければならない。SaaSの特性上、一度に処理できるデータ量の制約あり。。。

一時期Salesforce SEだったので、Salesforceを技術的に勉強するためにつくったアプリ。今でも使っている。
- [My Photos](https://github.com/araobp/myphotos)

メタバースってCRMで儲かるのだが、誰も理解してくれない。。。メタバース語るなら、フルスタックで勉強してね！最近はChatGPT流行ってきたし。。。
- [Unity Chat](https://github.com/araobp/unity-chat)

## UI

Jupyter Notebookでデータ分析して、レポート書いてお終い。。。だと、仕事は半分も出来ていない。
データをインタラクティブに可視化して見せるため、UI/UXは重要な要素。

2D UI向けフレームワークとして、私は、SvelteKitとBootstrapを使っている。これら、仕事では、大変重宝している。
- [SvelteKit AI](https://github.com/araobp/sveltekit-ai)

3D UI向けフレームワークとして、仕事ではUnityをずっと使ってきたが、最近はライセンスフリーなGodotを勉強中。
- [Godot Showroom](https://github.com/araobp/godot-showroom)

## その他ツール

- [言語認識](tools/LanguageIdentification.ipynb) ... 文章が短いと誤認識が起こる。
- [Image Captioning](tools/ImageCaptioning.ipynb) ... 認識性能の高さに驚いた！生成されたキャプションをNLPにかけて利用してみたい。
- [Matplotlib color map を HTML color listへ変換](tools/Colormap.ipynb) ... Networkのcommunity色分け用
- [Webスクレイピング](tools/WebScraping.ipynb) ... マーケティング部門所属エンジニアに必須なスキル。今回は Project Gutenberg の本(web版)からパラグラフ抽出を試みる。
- [YAML Database](tools/YAML_database.ipynb) ... 大量のドキュメントへNLP処理を行う際、その処理結果を保存するための簡易データベースを開発。

## ブラウザインタフェース

仕事では、自分がつくったものを他のメンバーへ使ってもらう手段として、ブラウザから操作できるインタフェースを提供。

### vis.js/graphology.js

Pythonで処理したnetworkxデータを[vis.js](https://visjs.org/)へ取り込みたい。しかし、vis.jsは可視化はできるがグラフ理論実装されておらず、実践上では不都合が出てきた。ブラウザ上の操作でサブグラフをつくれるようなライブラリが必要。

[Cytoscape.js](https://js.cytoscape.org/)にはグラフ理論とビジュアリゼーションの両方が含まれていて良いが、少し評価してみたところビジュアリゼーションが弱い。vis.jsの方がインパクトあり。

よって、以下の組み合わせにした：
- [graphology.js](https://graphology.github.io/)でグラフ理論の処理
- vis.jsでビジュアリゼーション処理

## 関係抽出

ナレッジグラフ生成に必要となる関係抽出、以下のモデルを試してみたが、性能がかなり良い。
- https://huggingface.co/ibm/knowgl-large

問題は、特定ドメイン固有の専門用語では関係抽出がうまく行かないこと。専用モデルの学習が必要になる。また、学習に必要十分なデータを揃えられない。

また、ここでは、ナレッジグラフ連動の検索エンジンを開発しているわけではなく、情報の整理やグルーピングをやりたいだけ。spaCyの範囲で出来る手法はないか？

最低限、ノード間依存関係とエッジのweightが必要。Weightの方、感情分析結果も反映させたい（ネットワークルーティングでいうコストに相当）。その程度ならspaCyのDependencyMatcherで実現出来ないか？探究中。。。

## TF-IDF (Work in progress)

Betweennessを尺度にして、グラフからサブグラフを抽出したい。

Named Entityのネットワークを生成してみると、ある単語の頻度がやたら多くて目立つ場合がある。例えば自社名。自社名は重要だが、betweennessが突出して大きくなってしまうのを避けたい。TF-IDF(Term Frequency - Inverse Document Frequency)でうまく調整出来ないか？検討してみたい。

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

Transformersのモデル保存場所

Macの場合
```
/Users/<username>/.cache/huggingface/hub
```

モデルのサイズが大きいので、用済み後は必要に応じ削除する。

### GiNZA

spaCy及びTransformers上で動作する日本語NLP。日本語TokenizerであるSudachiPy採用。
https://megagonlabs.github.io/ginza/

私は仕事でGiNZAを使っていない。英語と日本語両方扱う必要あるので。

## 購入した教科書（購入順）

日本語LLMの参考として
- [大規模言語モデル入門](https://gihyo.jp/book/2023/978-4-297-13633-8)

NLP教科書
- [実践 自然言語処理](https://www.oreilly.co.jp/books/9784873119724/)
-- [サンプルコード](https://github.com/oreilly-japan/practical-nlp-ja)

マーケティングの教科書
- [コトラーのマーケティング5.0](https://publications.asahi.com/product/23523.html)


## その他参考

- [Natural Language Processing With Python's NLTK Package](https://realpython.com/nltk-nlp-python/#getting-started-with-pythons-nltk)
- [Python による日本語自然言語処理](https://www.nltk.org/book-jp/ch12.html)
- [感情分析のやり方が7割わかるようになる記事（初心者向け）（ソースコードあり）（GiNZA）](https://qiita.com/Mizuiro__sakura/items/94efccb5ba12046d17b0)
- [How should I preprocess text for spaCy?](https://github.com/explosion/spaCy/discussions/10243)
- [seabornで日本語が文字化けする時の対処](https://kiseno-log.com/2021/03/13/seaborn%E3%81%A7%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%81%8C%E6%96%87%E5%AD%97%E5%8C%96%E3%81%91%E3%81%99%E3%82%8B%E6%99%82%E3%81%AE%E5%AF%BE%E5%87%A6/)
- [NER graphs](https://medium.com/@anoopjohny2000/ner-graphs-e79fb5247a95)
- [Knowledge Graph — A Powerful Data Science Technique to Mine Information from Text (with Python code)](https://prateekjoshi.medium.com/knowledge-graph-a-powerful-data-science-technique-to-mine-information-from-text-with-python-f8bfd217accc)
