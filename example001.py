import pandas as pd
import numpy as np

# 读入数据
data = pd.read_csv('/data/proj/exercise/yunyingshang.csv',encoding='utf-8')
print('该数据行数和列数：', data.shape)
print('前两行：', data.head(2))
##EDA
data['overdue_day_1']=np.where(data['overdue_day_1']>7, 1, 0)
data['overdue_day_1'].value_counts()
type(data['overdue_day_1'].value_counts())
# import seaborn as sns
# sns.countplot(x='overdue_day_1',data=data, plette='hls')
# plt.show()
# plt.savefig('count_plot')
count_fraud = sum(data['overdue_day_1'] == 1)
count_normal = sum(data['overdue_day_1'] == 0)
pct_fraud = count_fraud / (len(data))
print("percentage of fraud", pct_fraud * 100)
pct_normal = count_normal / (len(data))
print("percentage of normal", pct_normal * 100)
data[data.columns[1:10]].groupby('overdue_day_1').mean()
data.columns[730:len(data)]
## 一、数据清洗
###1.缺失值、异常值处理
###2.数据类型转化：回归模型解释变量转化为数值类型，或者分类模型对数值型变量进行编码
###3.根据预设想模型需要，是否对数据进行归一化
col_null = list(data.isnull().sum()[data.isnull().sum() != 0].index)
print('含空值列', col_null)
print('当前submit_time数据类型：', data['submit_time'].dtype)
data['submit_time'] = pd.to_datetime(data['submit_time'], format='%Y-%m-%d %H:%M:%S')
data.sort_values(by='submit_time', inplace=True)
data.set_index('borrower_id', drop=True, inplace=True)
tidy1 = data.drop(['Unnamed: 0', 'id_file', 'submit_time'], axis=1)
tidy2 = tidy1.drop(tidy1.columns[702: 747], axis=1)
#print('各列当前数据类型', tidy2.dtypes)
####列出当前数据非数值类型，但是运行时间太长：tidy2.dtypes[(tidy2.dtypes != 'int64') &( tidy3.dtypes !='float64')].index
tidy3 = tidy2.apply(pd.to_numeric, errors='ignore')
####异常值替换
def replace_to_median(df, missing_value):
    for column in df.columns:
        print(column)
        df[column]=np.where(np.isin(df[column].values, missing_value), np.median(df[column].values[~np.isin(df[column].values, missing_value)]), df[column].values)
    return df
miss=np.array([999999999])
tidy4=replace_to_median(tidy3, miss)
####去除常量
tidy3.columns[tidy3.var() == 0]
tidy4 = tidy3.drop(tidy3.columns[tidy3.var() == 0], axis=1)
###提取不相关变量
val_corr = tidy4.corr()
val_corr.iloc[0:10, 0:10]

def revalent_colnum(df,cor_threshold):
    i=1
    j=1
    revalent_list= []
    while(i<=df.columns.size):
        while(j<i):
            if(df.iloc[i,j]>=cor_threshold):
                revalent_list=revalent_list.append(df.columns[j])
                j= j+1
            else:
                j= j+1

        i=i+1
    return(unique([revalent_list]))






## 二、变量选择

### 1.线性关系 cor; 非线性关系:IV，卡方检验

###2.基于模型的变量重要性选择变量：gdbt,rf

## 三、模型选择

### 1.经典回归（广义线性等）、分类模型（决策树等）

#### 2.集成模型xgboost，RF，神经网络

## 四、模型评估

### 1.混淆矩阵评估指标：

#### 正确率、灵敏度、命中率、特异度、负命中率

### 2.排序类指标评估：

#### **ROC 曲线(及AUC值 )，Lift提升曲线，K-S曲线，洛伦兹曲线（及基尼系数）**

## 五、模型监控

#### 变量有效性，波动性；模型结果稳定性


###
df2 = pd.DataFrame(data={'水果': ['苹果', '梨', '草莓'],
                         '数量': [3, 2, 5],
                         '价格': [10, 9, 8],
                         '打折': [0.1, 0.8, 0.7],
                         '颜色': ['红色', '黄色', '粉色']})
df2
