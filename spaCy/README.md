# spaCy

注）2024/1/5: バッハネットワークは1/5より https://github.com/araobp/bach-network で開発継続し、このリポジトリ内では1/5以降は更新しない。

パシフィコ横浜で開催されたEdgeTech+2023展示会でO'Reillyの[実践 自然言語処理](https://www.oreilly.co.jp/books/9784873119724/)を購入。展示会で買うと20%ディスカウントで良い。この本でspaCyの存在を知った。NLP実践のための良書。この本をとかっかりにNLPの勉強を本格的に開始。spaCy、マーケティングの仕事で結構使える。APIがシンプルで良い。認識精度上げたければTransformerモデル使うことも出来る。

spaCyはAPIが綺麗で使いやすい。spaCyの開発者はドイツのベルリン在住者が多い。ドイツらしいシステマティックなAPI？

25年前、私もドイツのベルリンに住んていた。ベルリンってドイツ北東部に位置するので、バッハの音楽を沢山聴いた。プロテスタント教会で聴いたオルガン音楽やクリスマスオラトリオ。Project Gutenbergより入手した[バッハの本](https://www.gutenberg.org/cache/epub/35041/pg35041-images.html)から、spaCyによるNLPでバッハの人脈図をつくってみた。[Thu Vu](https://www.youtube.com/@Thuvu5)さんのYouTube上動画を参考にした。

ある程度慣れたら、このコースで網羅的に学習する：[Advanced NLP with spaCy](https://course.spacy.io/en)。add_extension(), nlp.pipe()など、NLP実践時には必須。

spaCyを実践で使ってみると、NERがとても使えることが分かった。しかし、うまく認識してくれない固有表現も多い。役職名や会社に固有な製品名など。その辺を改善するには、spaCyを再学習させる必要あり。ただし、自然言語処理は８０％の精度と言っている人たちが多い。状況によっては、辞書とPhraseMatcherで固有表現抽出の方が精度高くて良いかも。その場合、辞書の定期的なメンテナンスが重要になる。再学習のコストと辞書メンテナンスのコストを天秤にかけて、どちらが良いか考える必要あり。

- [spaCyでNLPインスタンス生成](spacy.ipynb)
- [キーフレーズ抽出](key_phrases.ipynb)
- [感情分析](sentiment.ipynb)
- [何故regexで国名抽出するときにNERで前処理する必要があるか？](NER_with_regex.ipynb)
- [spaCy and networkx](spaCy_networkx.ipynb) ... 最後に"bach_network.html"向けJavaScript出力。（注）Bach networkはスライディングウィンドウのNERでPERSON抽出しただけで、センテンスベースやパラグラフベースでの関係抽出が出来ていない。
- [spaCy and networkx2](spaCy_networkx2.ipynb) ... こちらでは、名前のペアをセンテンスから抽出する方法を採用。スライディングウィンドウで抽出する方法と大差ない結果となったが、こちらの方では PachelbelとJohann Christophの関係等を抽出出来ていない。

以下、バッハの本にも書かれている有名なくだり：

The most renowned Clavier composers of that day were Froberger,50 Fischer,51 Johann Caspar Kerl,52 Pachelbel,53 Buxtehude,54 Bruhns,55 [pg 11]and Böhm.56 Johann Christoph possessed a book containing several pieces by these masters, and Bach begged earnestly for it, but without effect. Refusal increasing his determination, he laid his plans to get the book without his brother's knowledge. It was kept on a book-shelf which had a latticed front. Bach's hands were small. Inserting them, he got hold of the book, rolled it up, and drew it out. As he was not allowed a candle, he could only copy it on moonlight nights, and it was six months before he finished his heavy task. As soon as it was completed he looked forward to using in secret a treasure won by so much labour. But his brother found the copy and took it from him without pity, nor did Bach recover it until his brother's death soon after.

この文章を見る限り、本当は以下のようなネットワークでなければならない。上の二つの手法、両方とも完全に正確ではない。

```
Froberger ---------------+---------+--------- Johann Christoph Bach ------- Johann Sebastian Bach
                         |         |                                                 |
Fischer -----------------+         +-------------------------------------------------+
                         |
Johann Caspar Kerl ------+
                         |
Pachelbel ---------------+
                         |
Buxtehude ---------------+
                         |
Bruhns ------------------+
                         |
Böhm --------------------+
```

正確に関係抽出するにはどうしたら良いのか？私にとって、今後の課題。名前が列挙されている場合には、それをノードのグループと捉え、少し離れて記述される名前(ノード)とエッジで結ぶ方が良いのかもしれない。
- パラグラフ内でNamed Entity抽出。
- Named Entityが列挙された場合、それをグループと捉える。グループ内のNamed Enitity間のエッジweightが弱くなるように調整する。

ちなみに、上記ブクステフーデはオルガン演奏の名手で、リューベックの教会でオルガニストを務めた人物。バッハはリューベックまで聴きに行った。それを記念した石碑が教会内にある。私も、それを見に、リューベックまで何度か行った。そういえばリューベックに有名なお菓子[Marzipan](https://en.wikipedia.org/wiki/Marzipan)があって、私も大好きだったので、日本へ帰省時のお土産として買って帰った。しかし、たまたま、それを食べた日本人の口には合わなかたが。。。と頭の中で連想してしまう。これが、人間の脳内にあるナレッジグラフ。

```
       たたたま食べた日本人
              | 口に合わなかった
　　　　　　Marzipan
              |
      +- リューベック -+
      |              |
      |              |
ブクステフーデ ------ バッハ
```

以下、spaCyのDepedencyTree探索のノートブック。DependencyTreeを探索するるアルゴリズム、結構、難しい。数日がかりで関数作成成功。
- [人名列挙の探索](finding_group.ipynb) ... spaCyの Dependecy Tree で列挙される人名を探索。文の中で、列挙される人名間の関係は薄いはず。conjの関係で人名をつなぐことで人名列挙を探索する。列挙された名前の間のnode pair間weightは2/len(グループ内の人数),その他は1とする。

以下が最終的な成果
- [spaCy and networkx3](spaCy_networkx3.ipynb)

このネットワークは J.S.Bach を中心とし、Louvainアルゴリズムで３つのグループに分けられた：Bachの家族、Bach以前の有名な音楽家集団、その他。

Edgeの部分の関係も抽出したい。以下の記事で勉強中 (Work in progress)
- [Natural Language Processing — Dependency Parsing](https://towardsdatascience.com/natural-language-processing-dependency-parsing-cf094bbbe3f7)
- [Knowledge graphs from complex text](https://medium.com/inspiredbrilliance/knowledge-graphs-from-complex-text-eb009aeed48e)
