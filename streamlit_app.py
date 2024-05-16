import streamlit as st
import requests
import json

# 创建Web应用的标题
st.title('One-Year Mortality Prediction')

# 创建输入表单
with st.form("prediction_form"):
    wbc = st.number_input('WBC (10^9/L)', value=10.0)
    age = st.number_input('Age', value=50)
    lym = st.number_input('Lym (10^9/L)', value=1.0)
    co2_bp = st.number_input('CO2-Bp(mmol/L)', value=24.0)
    eos = st.number_input('Eos', value=0.01)
    beta_blocker = st.selectbox('β-receptor Blocker', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    surgery = st.selectbox('Surgery Therapy', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    sbp = st.number_input('SBP(mmHg)', value=120)

    # 提交按钮
    submit_button = st.form_submit_button("Predict")

# 当用户提交表单时
if submit_button:
    # 构建请求数据
    data = {
        "WBC (10^9/L)": wbc,
        "age": age,
        "Lym (10^9/L)": lym,
        "CO2-Bp(mmol/L)": co2_bp,
        "Eos": eos,
        "β-receptor blocker(1yes，0no)": beta_blocker,
        "surgery therapy(1yes,0no)": surgery,
        "SBP(mmHg)": sbp
    }

    # 发送请求到Flask API
    response = requests.post('http://127.0.0.1:5000/predict', json=data)
    prediction = response.json()

    # 显示预测结果
    st.write(f'Prediction: {prediction["prediction"]}')
