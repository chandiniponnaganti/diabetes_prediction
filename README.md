# 🩺 Diabetes Prediction Web App

This project is a **Machine Learning web application** built with [Streamlit](https://streamlit.io/).  
It predicts whether a person has diabetes based on medical input parameters such as glucose level, BMI, age, etc.  

---

## 📌 Features
- User-friendly web interface using **Streamlit**
- Input medical details (Glucose, Insulin, Age, BMI, etc.)
- Predict diabetes using a trained **ML model**
- Model trained with **Scikit-learn**

---

## 📂 Project Structure
diabetes_prediction/
│── Diabeted prediction web app.py # Streamlit app
│── trained_model.sav # Saved ML model
│── requirements.txt # Dependencies
│── README.md # Project documentation


---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/diabetes_prediction.git
cd diabetes_prediction

2️⃣ Install dependencies
pip install -r requirements.txt


Or install manually:

pip install streamlit scikit-learn numpy pandas

3️⃣ Run the app
streamlit run "Diabeted prediction web app.py"


🧠 Model

The ML model was trained using Support Vector Machine (SVM) on the PIMA Diabetes Dataset.
The model is saved in trained_model.sav and loaded by the Streamlit app for predictions.



🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.


---

✅ Just save this as `README.md` in your project folder and push it to GitHub.  
It will automatically show up on your repo’s homepage.

---

👉 Do you want me to also make a **`requirements.txt`** for you (so anyone can install dependencies in one command)?
