### CONFIGS ###
"""
定义了数据集等变量和参数，用于构建和训练模型
"""
dataset = 'cora'
model = 'VGAE'

input_dim = 1433 
hidden1_dim = 32
hidden2_dim = 16
use_feature = True

num_epoch = 200
learning_rate = 0.01