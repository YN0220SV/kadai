import pandas as pd

# CSVファイルを読み込む
data = pd.read_csv('/home/yn/デスクトップ/kadai/power.csv')

# 'DATE' と 'TIME' を結合して新しい 'datetime' 列を作る
data['datetime'] = pd.to_datetime(data['DATE'] + ' ' + data['TIME'])

# 新しい 'date' 列を作る
data['date'] = data['datetime'].dt.date

# 'date' ごとの平均値と最大値を計算する
average = data.groupby('date')['需要'].mean()
maximum = data.groupby('date')['需要'].max()
sum=data.groupby("date")["需要"].sum()
# 結果を新しい DataFrame にまとめる
result = pd.DataFrame({
    'date': average.index,
    'average': average.values,
    'max': maximum.values,
    'sum':sum.values
})

# 結果を新しい CSV ファイルに出力する
result.to_csv('tempV2.csv', index=False)
