from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

<<<<<<< HEAD
# 加载模型和标准化器
model_path = r'C:\Users\14701\Desktop\treebag_model.pkl'
scaler_path = r'C:\Users\14701\Desktop\scaler.pkl'

=======
# 指定模型和标准化器的路径
model_path = r'C:\Users\14701\Desktop\treebag_model.pkl'
scaler_path = r'C:\Users\14701\Desktop\scaler.pkl'

# 加载模型和标准化器
>>>>>>> 6b0ef98ec65f5f68e0fdd6ba5c636d72f429bbe1
model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 从POST请求获取JSON数据
        input_data = request.get_json()
<<<<<<< HEAD

        # 打印接收到的数据
        print("Received input data:", input_data)

        # 定义预期的特征名称
        expected_features = [
            "WBC (10^9/L)", "age", "Lym (10^9/L)", "CO2-Bp(mmol/L)", "Eos",
            "β-receptor blocker(1yes，0no)", "surgery therapy(1yes,0no)", "SBP(mmHg)"
        ]

        # 创建映射字典以匹配输入数据和预期的特征名称
        feature_mapping = {
            "WBC_109L": "WBC (10^9/L)",
            "Lym_109L": "Lym (10^9/L)",
            "CO2_Bp_mmol_L": "CO2-Bp(mmol/L)",
            "beta_receptor_blocker_1yes_0no": "β-receptor blocker(1yes，0no)",
            "surgery_therapy_1yes_0no": "surgery therapy(1yes,0no)",
            "SBP_mmHg": "SBP(mmHg)"
        }

        # 检查输入数据是否包含所有预期的特征
        if not all(feature in input_data for feature in feature_mapping):
            missing_features = [feature for feature in feature_mapping if feature not in input_data]
            return jsonify({'error': f'Input data is missing some features: {missing_features}'}), 400

        # 映射输入数据到预期的特征名称
        mapped_input_data = {feature_mapping.get(k, k): v for k, v in input_data.items()}

        # 将映射后的数据转换为DataFrame
        data_df = pd.DataFrame([mapped_input_data])

        # 应用标准化
        data_scaled = scaler.transform(data_df)

        # 进行预测
        prediction = model.predict_proba(data_scaled)[:, 1]  # 获取类别为1的预测概率

        # 返回预测结果
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
=======
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

>>>>>>> 6b0ef98ec65f5f68e0fdd6ba5c636d72f429bbe1
