# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib   # for saving models

past_data = pd.read_csv("ad_performance_dummy.csv")       
upcoming_data = pd.read_csv("upcoming_ad_creatives.csv") 

X = past_data[["Ad Headline", "Creative Type", "Target Audience"]]

# Targets: CTR (%) and Conversions (we will train 2 models)
y_ctr = past_data["CTR (%)"]
y_conv = past_data["Conversions"]

# -------------------------------
# STEP 3: Preprocessing
# -------------------------------
# - TF-IDF for ad headlines (turns text into numbers)
# - OneHotEncoding for Creative Type & Target Audience
preprocessor = ColumnTransformer(transformers=[
    ("headline", TfidfVectorizer(max_features=50), "Ad Headline"),
    ("categorical", OneHotEncoder(handle_unknown="ignore"), ["Creative Type", "Target Audience"])
])

# -------------------------------
# STEP 4: Define Models (Random Forest)
# -------------------------------
# One model for CTR, another for Conversions
ctr_model = Pipeline(steps=[
    ("preprocessor", preprocessor),  # first preprocess features
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))  # then apply ML model
])

conv_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# -------------------------------
# STEP 5: Train the Models
# -------------------------------
ctr_model.fit(X, y_ctr)      # learns CTR patterns
conv_model.fit(X, y_conv)    # learns Conversion patterns

# Save models for later reuse (optional)
joblib.dump(ctr_model, "ctr_predictor.pkl")
joblib.dump(conv_model, "conversion_predictor.pkl")

# -------------------------------
# STEP 6: Make Predictions on Upcoming Ads
# -------------------------------
upcoming_data["Predicted CTR (%)"] = ctr_model.predict(upcoming_data)
upcoming_data["Predicted Conversions"] = conv_model.predict(upcoming_data)

# -------------------------------
# STEP 7: Save Predictions
# -------------------------------
upcoming_data.to_csv("predicted_ad_performance.csv", index=False)

print("✅ Predictions saved to 'predicted_ad_performance.csv'")
print(upcoming_data)
