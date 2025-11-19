# belong/ml/train_lonely_death.py

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression   

from .feature_builder import build_feature_dataframe
from .config import MODEL_PATH, FINAL_FEATURES, TARGET_COL


def train_model():
    df = build_feature_dataframe()

    X = df[FINAL_FEATURES]
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()    # ← 변경됨
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    print("🎉 lonely_death_model.pkl 저장 완료! (LinearRegression 기반)")
    return model


if __name__ == "__main__":
    train_model()
