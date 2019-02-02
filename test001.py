import numpy as np
import pandas as pd
df2 = pd.DataFrame(data={'水果': ['苹果', '梨', '草莓', '香蕉'],
                         '数量': [3, 2, 5, 5],
                         '价格': [10, 8, 8, 10],
                         '打折': [0.1, 0.8, 0.7, 0.6],
                         '颜色': ['红色', '黄色', '粉色','黄色']})


def replace_to_median1(df, missing_value):
    for column in df.columns:
        df[column] = np.where(np.isin(df[column].values, missing_value),
                              np.median(df[column].values[~np.isin(df[column].values, missing_value)]),
                              df[column].values)
    return df



import pandas as pd
data = pd.read_csv('/data/proj/exercise/yunyingshang.csv',encoding='utf-8')
data.head()




# #print(type(df2['价格'].median()))
# #print(type(df2['水果'][1]))
#
#
# def replace_unusual(x):
#     x[x[x == 999].index] = x[x != 999].median()
#     return x
#
#
# def replace_to_median(df, missing_value):
#     for column in df.columns:
#         df['one'] = np.where(np.isin(df.loc[:, 'one'], missing_value),
#                               np.median(df[~np.isin(df.loc[:, 'one'], missing_value)]), df.loc[:, 'one'])
#     return df
#
#
#
# import pandas as pd
# import numpy as np
# file = open('/data/proj/exercise/yunyingshang.csv', 'r', encoding='utf-8')
# data = pd.read_csv(file)
# print('该数据行数和列数：', data.shape)
# print('前两行：', data.head(2))
# col_null = list(data.isnull().sum()[data.isnull().sum() != 0].index)
# print('含空值列', col_null)
# print('当前submit_time数据类型：', data['submit_time'].dtype)
# data['submit_time'] = pd.to_datetime(data['submit_time'], format='%Y-%m-%d %H:%M:%S')
# data.sort_values(by='submit_time', inplace=True)
# data.set_index('borrower_id', drop=True, inplace=True)
# tidy1 = data.drop(['Unnamed: 0', 'id_file', 'submit_time'], axis=1)
# tidy2 = tidy1.drop(tidy1.columns[list(range(702, 747))], axis=1)
# #print('各列当前数据类型', tidy2.dtypes)
# tidy3 = tidy2.apply(pd.to_numeric, errors='ignore')
# def replace_to_median(column, missing_value):
#     return np.where(np.isin(column, missing_value), np.median(column[~np.isin(column, missing_value)]), column)
#
# # def replace_unusual(x):
# #     x[x[x == 999999999].index] = x[x != 999999999].median()
# #     return x
#
# import numpy as np
# a=np.array([1,2,3])
# b=2
# np.where(a == b,a,sum(a[a!=b]))
pd.Series