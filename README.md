# 🔥 Algerian Forest Fire Prediction

This project focuses on predicting forest fire occurrences using meteorological and fire weather index data collected during the **summer of 2012** from two Algerian regions: **Bejaia** and **Sidi Bel-abbes**. The aim is to build machine learning models that can help in developing early warning systems for wildfire management.

---

## 📊 Dataset Overview

| Attribute              | Description                                                |
|------------------------|------------------------------------------------------------|
| 📍 **Regions**         | Bejaia (Northeast) & Sidi Bel-abbes (Northwest), Algeria   |
| 📆 **Time Period**     | June 2012 – September 2012                                 |
| 🔢 **Total Instances** | 244                                                        |
| 🌿 **Bejaia Region**   | 122 instances                                              |
| 🌾 **Sidi Bel-abbes**  | 122 instances                                              |
| 🧪 **Features**        | 11 input features (temperature, humidity, wind, rain, etc.)|
| 🎯 **Target**          | `Classes` – Fire 🔥 / Not Fire 🚫                           |

---

## 📌 Features Description

- Temperature (°C)
- RH (Relative Humidity %)
- Ws (Wind speed km/h)
- Rain (mm)
- FFMC (Fine Fuel Moisture Code)
- DMC (Duff Moisture Code)
- DC (Drought Code)
- ISI (Initial Spread Index)
- BUI (Build-Up Index)
- FWI (Fire Weather Index)
- Region

---

## 🔥 Class Distribution

| Class      | Count |
|------------|-------|
| 🔥 Fire     | 138   |
| 🚫 Not Fire | 106   |

---

## 🧠 Models Implemented

The following regression models were trained to predict **FWI (Fire Weather Index)** and classification models to predict `Classes` (Fire / Not Fire):

- 🔹 Linear Regression  
- 🔹 Ridge Regression  
- 🔹 Lasso Regression  
- 🔹 ElasticNet Regression  
- 🔹 RidgeCV  
- 🔹 LassoCV  

📌 Among these, **Ridge Regression gave the best result**, achieving an **R² score of nearly 0.99**, showing excellent predictive power.

### 🧪 Ridge Regression Code Snippet:

```python
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

model_ridge = Ridge(alpha=0.1)
model_ridge.fit(X_train_scaled, Y_train)
y_pred2 = model_ridge.predict(X_test_scaled)
print(r2_score(Y_test, y_pred2))  # Output: ~0.99
```
## ✅ Conclusion

This project successfully demonstrates how environmental features can be used to predict wildfire events with high accuracy. Using **Ridge Regression**, we achieved a near-perfect **R² score of ~0.99** for predicting the Fire Weather Index.

To enhance accessibility, I have also **created a web application using Streamlit**. This allows users to input weather conditions and receive real-time fire risk predictions through an interactive interface. 🔥🌲
