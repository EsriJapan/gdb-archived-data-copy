# gdb_archived_data_copy

履歴管理が有効なフィーチャクラスの過去の一時点の状態を、シェープファイルとして出力します。

#使用法

 コマンドラインへの入力するパラメータです。各パラメーターの間には、スペース一つをあけて入力してください。(例 python gdb_archived_data_copy.py 引数1 引数2 .... 引数n)  

* 引数1: 出力先のディレクトリ (例 C:\Users\temp)  

* 引数2:データベースのプラットフォーム ( POSTGRESQL または SQLSERVER または ORACLE*)

* 引数3:データーベースのサービス (インスタンス名)

* 引数4:データベースの認証方法 (例 DATABASE_AUTHまたはOPERATING_SYSTEM_AUTH)  

* 引数5:データベースのユーザー ( 認証方法がDATABASE_AUTH の場合のみ必要 )  

* 引数6:データベースのパスワード (DATABASE_AUTH で設定されている場合のみ必要 )

* 引数7:入力するフィーチャクラス  

* 引数8:日付 yyyy-MM-dd HH:mm:ss (例  "2015-06-8 23:45:01" )

*ORACLE  のユーザ スキーマ ジオデータベースからツールを実行することはできません。

使用例：python gdb_archived_data_copy.py C:\Users\temp SQLSERVER
 MSSQLSERVER DATABASE_AUTH user_name user_pass feature_name "2015-06-8 23:45:01"



## 使用している製品・プロジェクト

* [ArcGIS for Desktop](https://desktop.arcgis.com/ja/)
* [ArcGIS for Developers](https://developers.arcgis.com/en/)

## ライセンス
Copyright 2015 Esri Japan Corporation.

Apache License Version 2.0（「本ライセンス」）に基づいてライセンスされます。あなたがこのファイルを使用するためには、本ライセンスに従わなければなりません。本ライセンスのコピーは下記の場所から入手できます。

> http://www.apache.org/licenses/LICENSE-2.0

適用される法律または書面での同意によって命じられない限り、本ライセンスに基づいて頒布されるソフトウェアは、明示黙示を問わず、いかなる保証も条件もなしに「現状のまま」頒布されます。本ライセンスでの権利と制限を規定した文言については、本ライセンスを参照してください。

ライセンスのコピーは本リポジトリの[ライセンス ファイル](./LICENSE)で利用可能です。

[](EsriJapan Tags: <タグ（半角スペース区切り）>)
[](EsriJapan Language: <開発言語>)
