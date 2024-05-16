from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# 加载模型和标准化器
model = pickle.load(open(r'C:\Users\14701\Desktop\treebag_model.pkl', 'rb'))
scaler = pickle.load(open(r'C:\Users\14701\Desktop\scaler.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 从POST请求获取JSON数据
        input_data = request.get_json()
        # 将JSON数据转换为DataFrame
        data_df = pd.DataFrame([input_data])
        # 应用标准化
        data_scaled = scaler.transform(data_df)
        # 进行预测
        prediction = model.predict_proba(data_scaled)[:, 1]  # 获取类别为1的预测概率
        # 返回预测结果
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
