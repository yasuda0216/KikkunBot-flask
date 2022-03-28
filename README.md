# KikkunBot-flask

## app.pyファイルの説明
- @app.route('/slot/<test>')ではユーザのメッセージに対してスロット抽出を行います。モデルはGPT3_finetuning_slotextraction.ipynbで学習させたものを使用しています。
- @app.route('/polarity/<test>')ではユーザの発話からpolarityの判定を行います。モデルはGPT3_finetuning_emotionality.ipynbで学習させたものを使用しています。
- @app.route('/question/<test>')ではボットの質問生成を行います。モデルはGPT3_finetuning_response.ipynbで学習したものを使用しています。
- @app.route('/aizuti/<test>')ではボットの相槌生成を行います。モデルはGPT3_finetuning_aizuti.ipynbで学習したものを使用しています。
  
## app.pyファイルの実行方法
- VSCode上の仮想環境で実行します（[VS CodeとFlaskによるWebアプリ開発「最初の一歩」](https://atmarkit.itmedia.co.jp/ait/articles/1807/24/news024.html)を参考にして実行すると分かりやすいです）
