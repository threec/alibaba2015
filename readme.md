## 流程说明

1. user_action_data_split.py 首先将用户行为数据按照时间分为18号的，和非18号的。
生成user_action_train.csv和user_action_test.csv 。
2. createFeature.py [train|submit] 将第一个文件生成特征文件，如果用多个生成特征文件，最终用merge.py将特征文件融合到feature.merge.csv
gen_label_data.py 将第二个文件生成标签文件
3. gen_data.py 将特征和标签文件融合到data.csv中
4. data_sample.py 将data.csv划分为训练data.train.csv和测试文件data.test.csv，其中训练数据对付样本进行下采样。
5. model0.py 模型训练文件，不解释

## 工具
summary.py 对已训练模型进行评价


