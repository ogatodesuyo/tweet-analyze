# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

from collections import Counter

#グラフ化用のライブラリ読み込み
import matplotlib
import matplotlib.pyplot as plt

#CSV読み込み
apr_df = pd.read_csv("201911tweet.csv")
may_df = pd.read_csv("201912tweet.csv")
jun_df = pd.read_csv("202001tweet.csv")
jul_df = pd.read_csv("202002tweet.csv")

#結合
combine = [apr_df, may_df, jun_df, jul_df]

#データフレームを作成、いいね順に並び変え
tweets_df = tweets_df = pd.concat(combine) .sort_values(by="いいね", ascending=False)

#必要データの抽出
tweets_df = tweets_df[["ツイート本文", "リツイート", "時間", "いいね"]]

#Matplotlibのグラフスタイルの設定
plt.style.use("seaborn-pastel")
font = {"family" : "IPAexGothic"}
matplotlib.rc("font", **font)

#グラフを描写
tweets_df.plot.hist( y=["いいね"], bins=50, figsize=(16,9))


#グラフを保存
plt.savefig("histogram.png")

#時間データから日付や分数を取り除く
tweets_df["時間"] = pd.to_datetime(tweets_df["時間"])
tweets_df["時刻"] = tweets_df["時間"].dt.hour

#いいね数と時刻のデータフレームを作成
time_df = tweets_df[["いいね","時刻"]]

#時刻順に並び替える
time_df = time_df.sort_values(by=["時刻"], ascending=True)

#時刻ごとにデータを集計
grouped = time_df.groupby("時刻")

#時刻ごとの平均いいね数
mean = grouped.mean()

#時刻ごとのツイート数
size = grouped.size()

#時刻ごとの平均いいね数の棒グラフを描写
mean.plot.bar(xlim=[0,24], ylim=[0,40],figsize=(16,9))

#時刻ごとのツイート数の折れ線グラフを描写
size.plot.bar(xlim=[0,24], ylim=[0,40],figsize=(16,9))

#描写したグラフを保存
plt.savefig("時刻別平均いいね数とツイート数.png")

#評価付け
tweets_df.loc[tweets_df["いいね"] >= 50, "いいね評価"] = "50~"
tweets_df.loc[(tweets_df["いいね"] < 50)  &  (tweets_df["いいね"] >= 30), "いいね評価"] = "50~30"
tweets_df.loc[(tweets_df["いいね"] < 30)  &  (tweets_df["いいね"] >= 20), "いいね評価"] = "30~20"
tweets_df.loc[(tweets_df["いいね"] < 20)  &  (tweets_df["いいね"] >= 10), "いいね評価"] = "20~10"
tweets_df.loc[tweets_df["いいね"] < 10, "いいね評価"] = "~10"

#各ツイートの文字数を取得
tweets_df["文字数"] = tweets_df.ツイート本文.str.len()

#評価用リストを作成
hyoka = ["50~", "50~30", "30~20", "20~10", "~10"]

#評価ごとの平均文字数を格納するデータフレームを作成
fav_mean_df = pd.DataFrame(index = hyoka, columns = ["平均文字数"])

#作成したデータフレームに平均文字数を格納
for i in hyoka:
    df = tweets_df[tweets_df.いいね評価 == i]
    fav_mean_df.loc[[i],["平均文字数"]] = df["文字数"].mean()

#グラフを描写
fav_mean_df.plot.bar(figsize=(16,9))

#描写したグラフを保存
plt.savefig("平均ツイート文字数.png")



#テスト用サーバー起動
app.run(debug=True,host="0.0.0.0",port="8888")

localhost:8888
