import os
dir_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件的路径
model_path = os.path.join(dir_path, 'path/to/your/treebag_model.pkl')
model = pickle.load(open(model_path, 'rb'))
