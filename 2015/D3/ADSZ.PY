import pandas as pd
data = pd.read_table('fruit_data_with_colors.txt')

labels = np.array(data.loc[:, 'fruit_label'])
data_dropped = data.drop(['fruit_label', 'fruit_name', 'fruit_subtype'], axis=1)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data_dropped)
data_scaled[:3, :]

X = data_scaled.copy()
y = labels.copy()