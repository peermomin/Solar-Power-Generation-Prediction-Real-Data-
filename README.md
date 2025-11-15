# ☀️ Solar Power Generation Prediction

## 📘 Project Overview
This project predicts **solar power output (DC Power)** based on environmental and sensor data from two solar plants.  
The model helps in understanding how **temperature, irradiation**, and other factors influence power generation — useful for **energy forecasting and optimization** in solar farms.

---

## ⚙️ Steps Completed So Far

### 1. 🗂️ Data Collection
Loaded raw data for **Plant 1** and **Plant 2**, containing parameters like:
- DC Power (W)  
- AC Power (W)  
- Ambient Temperature (°C)  
- Module Temperature (°C)  
- Irradiation (W/m²)  
- Date-Time and Source IDs  

---

### 2. 🧹 Data Cleaning & Preparation
- Dropped redundant columns (`PLANT_ID_x`, `PLANT_ID_y`, etc.)
- Removed duplicates.
- Filtered out:
  - Rows with missing key features (`DC_POWER`, `IRRADIATION`, etc.)
  - Nighttime readings where `IRRADIATION = 0`
  - Records where `DC_POWER = 0`
- Converted timestamps to proper `datetime` format.
- Combined both plant datasets into one clean file:  
  ✅ **Cleaned_Solar_Data.csv**

---

### 3. 📊 Exploratory Data Analysis (EDA)
Generated a **correlation heatmap** to understand relationships between features:

```python
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Feature Correlation Heatmap")
plt.show()
```
## 🔍 Key Insights

- 🌞 **IRRADIATION** is highly correlated with **DC_POWER**.  
- 🌡️ **Temperatures** (ambient & module) show a moderate positive correlation with power generation.

---

## ⚙️ Model Training

Trained and compared multiple models on the cleaned dataset:

| Model              | R² Score | MAE       | RMSE      |
|--------------------|-----------|-----------|-----------|
| Linear Regression  | 0.664     | 1755.51   | 2250.71   |
| Gradient Boosting  | 0.868     | 976.05    | 1412.36   |
| 🌲 Random Forest   | **0.989** | **177.42** | **404.33** |

✅ **Best Model:** Random Forest

Saved the trained model for future use:
```python
joblib.dump(models["Random Forest"], "./Models/solar_rf_model.pkl")
```
## 🧪 Model Testing on Unseen Data

A separate notebook was used to:

- Load the saved model
- Evaluate it on the unseen test split
- Visualize Actual vs Predicted DC Power

The model maintained very high accuracy (**R² ≈ 0.989**), confirming strong generalization.

---

## 🚀 Streamlit App Deployment

A complete Streamlit web app was created to allow user interaction:

Users can input:

- Ambient Temperature
- Module Temperature
- Irradiation
- Hour of Day
- Month

And receive:

➡️ Predicted DC Power Output (in Watts)

The app loads the trained model:

```python
model = joblib.load("./Models/solar_rf_model.pkl")
```

---

## 🧠 Technologies Used
- **Python**  
- **Pandas**, **NumPy**  
- **Matplotlib**, **Seaborn**  
- **Scikit-learn**  
- **Joblib**

