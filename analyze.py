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










#テスト用サーバー起動
app.run(debug=True,host="0.0.0.0",port="8888")

localhost:8888
