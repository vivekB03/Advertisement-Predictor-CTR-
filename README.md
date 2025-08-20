# AI Based Advertisement-Predictor-CTR-

# 🧠 AI-based Ad Performance Predictor  

This project predicts the performance of **upcoming ad creatives** (CTR & Conversions) based on past ad campaign data from **Google Ads** and **Meta Ads**.  

It uses **Python + Machine Learning (Random Forest)** to learn from past performance and generate predictions for new ads.  
The results can also be visualized in **Power BI** dashboards.  

---

## 📌 Features
- Train ML models (Random Forest) on past ad data  
- Predict **CTR (%)** and **Conversions** for new creatives  
- Handles text (ad headlines), creative type, and target audience  
- Saves predictions into a CSV for easy reporting & visualization  

---

## 📂 Project Structure
```

📁 Ad Performance Predictor
│── ad\_performance\_dummy.csv          # Past campaign dataset (training data)
│── upcoming\_ad\_creatives.csv         # New ads to test predictions
│── Add predictor.py                  # Main Python script
│── predicted\_ad\_performance.csv      # Output file with predictions
│── README.md                         # Project documentation


 ⚙️ Installation

Clone this repository:
```bash
git clone https://github.com/your-username/ad-performance-predictor.git
cd ad-performance-predictor
````

Install required dependencies:

```bash
pip install scikit-learn pandas joblib
```

---

## 🚀 Usage

1. Place your **past ad data** in `ad_performance_dummy.csv`.
2. Add **new upcoming creatives** in `upcoming_ad_creatives.csv`.
3. Run the script:

```bash
python "Add predictor.py"
```

4. Check the output in `predicted_ad_performance.csv`.

---

## 📊 Example Output

| Ad Headline            | Creative Type | Audience    | Predicted CTR (%) | Predicted Conversions |
| ---------------------- | ------------- | ----------- | ----------------- | --------------------- |
| Mega Clearance Sale    | Image         | Women 20–35 | 3.5               | 150                   |
| Exclusive Offer Inside | Carousel      | All 18–40   | 4.1               | 220                   |

---

## 💡 Next Steps

* Integrate model predictions into **Power BI dashboards**
* Experiment with **other ML models** (Linear Regression, XGBoost, etc.)
* Use real-world Google Ads/Meta Ads data

---

## 👨‍💻 Author

**Vivek** – Data & AI Enthusiast
📌 Skills: Python, Machine Learning, Power BI, Analytics

---

```

---

Would you like me to also **add screenshots/diagrams** (like workflow or Power BI dashboard preview) to this README so it looks more professional on GitHub?
```
