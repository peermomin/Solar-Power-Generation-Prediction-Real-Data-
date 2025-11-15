import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

# -----------------------------
# Load the Trained Model
# -----------------------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("./Models/solar_rf_model.pkl")
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

model = load_model()

# -----------------------------
# App Header
# -----------------------------
st.title("☀️ Solar Power Generation Prediction App")

st.write("""
This machine learning app predicts **DC Power Output (in Watts)** for a solar panel system  
based on environmental and sensor inputs.

### Model Training Info
The prediction model was trained using **real-world data from two solar power plants**:

- **Plant 1 Dataset**  
- **Plant 2 Dataset**

The data included sensor parameters such as temperature, irradiation, and timestamps.  
After cleaning and processing, the combined dataset was used to train a  
**Random Forest Regressor with an accuracy of R² = 0.989**.

---
""")

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("Enter Input Features")

ambient_temp = st.number_input("Ambient Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0)
module_temp = st.number_input("Module Temperature (°C)", min_value=0.0, max_value=90.0, value=40.0)
irradiation = st.number_input("Irradiation (W/m²)", min_value=0.0, max_value=1500.0, value=800.0)
hour = st.number_input("Hour of Day (0–23)", min_value=0, max_value=23, value=12)
month = st.number_input("Month (1–12)", min_value=1, max_value=12, value=6)

# Prepare input as array
input_data = np.array([[ambient_temp, module_temp, irradiation, hour, month]])

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict DC Power"):
    if model is not None:
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted DC Power Output: **{prediction:.2f} W**")
    else:
        st.error("Model not loaded. Check the model file path.")

# Footer
st.write("---")
st.caption("Built using real solar plant data, Streamlit, and Machine Learning ")
