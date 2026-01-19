#  Crop Recommendation System using Machine Learning

A web-based **Crop Recommendation System** that predicts the most suitable crop based on **soil nutrients and climate conditions** using a **Machine Learning model**.  
Built with **Flask**, **scikit-learn**, and a clean, user-friendly frontend.

---

##  Project Overview

Farmers often struggle to decide which crop to grow based on soil and weather conditions.  
This project uses a **Random Forest Classifier** to recommend the best crop by analyzing:

- Soil nutrients (N, P, K)
- Temperature
- Humidity
- Soil pH
- Rainfall

The application provides **instant crop recommendations** through a simple web interface.

---

##  Application Interface

Below is the user interface of the Crop Recommendation System, where users input soil and climate parameters to get an instant crop recommendation.

![Crop Recommendation System UI](assets/crop-ui.png)

---

##  Features

-  ML-based crop prediction
-  Trained RandomForest model
-  Clean and responsive UI
-  Accurate feature handling (no mismatch errors)
-  Production-ready Flask backend
-  Easy to deploy on Render / Railway / Cloud

---

##  Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Libraries:** scikit-learn, pandas, numpy
- **Target:** Crop type
- **Input Features (Exact Training Order):** ['temperature', 'N', 'P', 'K', 'humidity', 'ph', 'rainfall']


To avoid prediction errors, the app **forces the same feature order used during training**.

---

##  Tech Stack

| Layer | Technology |
|-----|-----------|
Frontend | HTML, CSS |
Backend | Flask |
ML Model | scikit-learn |
Data Handling | pandas, numpy |
Deployment | Render |
Server | gunicorn |

---



