from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# 加载模型和标准化器，确保模型文件在项目文件夹中
model = pickle.load(open('treebag_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        data_df = pd.DataFrame([input_data])
        data_scaled = scaler.transform(data_df)
        prediction = model.predict_proba(data_scaled)[:, 1]
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
