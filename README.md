# 🌾 AgriPred: Crop Yield Predictor

[![Streamlit](https://img.shields.io/badge/Streamlit-App-green?logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Responsive UI](https://img.shields.io/badge/UI-Responsive-lightgreen)](#)
[![Model: Scikit-learn](https://img.shields.io/badge/Model-Scikit--learn-orange?logo=scikit-learn)](https://scikit-learn.org/)


[![Open in Streamlit](https://img.shields.io/badge/Launch-App-green?logo=streamlit)](https://agripred-hhofqy55gddfxyvtnkshxe.streamlit.app/)


**AgriPred** is a student-led, AI-powered web app that predicts crop yield based on environmental and farming inputs. Built with Streamlit, it blends machine learning with a responsive, pastel-themed UI to deliver real-time insights for students, farmers, and educators.

---

## 🌟 Features

| Feature | Description |
|--------|-------------|
| 🌱 **Yield Prediction** | Predicts crop yield in tons per hectare using a trained ML model. |
| 🎚 **Rainfall Sensitivity** | Slider to explore how rainfall affects yield. |
| 💧 **Irrigation Impact** | Compare yield with and without irrigation. |
| 🌾 **Fertilizer Impact** | See how fertilizer usage influences crop performance. |
| 📊 **Scenario Insights** | Dynamic metrics show baseline and adjusted predictions. |
| 📱 **Responsive UI** | Mobile-friendly layout with pastel green theme and red accents. |
| 🎨 **Custom Styling** | Fully customizable via `style.css`. |
| 🧠 **Educational Tool** | Designed for student campaigns and public science outreach. |

---

## 🔧 Project Workflow

| Stage | Description |
|-------|-------------|
| 📊 **Data Collection** | Historical crop data with rainfall, temperature, fertilizer, irrigation, and harvest duration. |
| 🧪 **Model Training** | Regression model trained using `scikit-learn`. |
| 💾 **Model Serialization** | Saved as `crop_yield_model.pkl` using `joblib`. |
| 🖥️ **App Development** | Built with Streamlit using sidebar inputs and tabbed outputs. |
| 🎨 **UI Styling** | Pastel-themed `style.css` for accessibility and emotional tone. |
| 🚀 **Deployment** | Ready for Streamlit Cloud or local hosting. |

---

## 🧪 Techniques Used

### 🔍 Machine Learning
- **Model Type**: Regression (XGBoostRegressor)
- **Framework**: `scikit-learn`
- **Target**: Crop yield (t/ha)
- **Features**: Rainfall, Temperature, Days to harvest, Fertilizer, Irrigation

### 📦 Model Handling
- **Serialization**: `joblib` for saving/loading
- **Caching**: `@st.cache_resource` for performance

### 🧮 Data Processing
- **Input**: `pandas` DataFrame from sidebar
- **Prediction**: Real-time yield estimation and scenario analysis

### 🎨 UI & Styling
- **Framework**: Streamlit
- **Theme**: Pastel green with red accents
- **Responsiveness**: Media queries for mobile optimization

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/agripred.git
cd agripred

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### 🖼️ UI Overview
🧭 Sidebar Inputs
🌧️ Rainfall (mm)

🌡️ Temperature (°C)

📅 Days to harvest

💧 Irrigation used

🌾 Fertilizer used

Styled with pastel green backgrounds and red +/– buttons.

📊 Prediction Tab
Displays predicted yield using a trained ML model.

Add screenshot here: ![Prediction Tab UI](https://github.com/user-attachments/assets/00708e75-9af8-434a-bea5-d999f779fdee)

🔍 Insights Tab
Explore farming practice impacts:

💧 Irrigation scenarios

🌾 Fertilizer scenarios

🎚 Rainfall sensitivity slider

Add screenshot here: ![Insights Tab UI](https://github.com/user-attachments/assets/049a1ea7-c4ea-4db0-afba-fe8cb4650867)
