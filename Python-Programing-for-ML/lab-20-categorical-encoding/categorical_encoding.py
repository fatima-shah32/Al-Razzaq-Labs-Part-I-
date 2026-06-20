import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

print("=== Lab 20: Encoding Categorical Variables ===")

# Create sample dataset
data = {
    "Category": [
        "Apple",
        "Banana",
        "Cherry",
        "Apple",
        "Cherry",
        "Banana"
    ]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# Task 1: Label Encoding
label_encoder = LabelEncoder()

df["Category_encoded"] = label_encoder.fit_transform(
    df["Category"]
)

print("\nLabel Encoded Dataset:")
print(df)

# Task 2: One-Hot Encoding
onehot_encoder = OneHotEncoder(
    sparse_output=False
)

onehot_encoded = onehot_encoder.fit_transform(
    df[["Category"]]
)

categories = onehot_encoder.get_feature_names_out(
    ["Category"]
)

df_onehot = pd.DataFrame(
    onehot_encoded,
    columns=categories
)

print("\nOne-Hot Encoded Dataset:")
print(df_onehot)

# Task 3: Pipeline Integration
categorical_features = ["Category"]

categorical_transformer = OneHotEncoder(
    sparse_output=False
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            categorical_transformer,
            categorical_features
        )
    ]
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression())
    ]
)

X = df[["Category"]]
y = [0, 1, 0, 1, 0, 1]

pipeline.fit(X, y)

print("\nPipeline trained successfully")

predictions = pipeline.predict(X)

print("Predictions:")
print(predictions)
