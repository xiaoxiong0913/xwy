import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle

# Read the data
data_path = r"C:\Users\14701\Desktop\model_analysis_data.xlsx"
data = pd.read_excel(data_path)

# Separate features and target variable
X = data.drop('one_year_mortality（1yes，0no）', axis=1)
y = data['one_year_mortality（1yes，0no）']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42, stratify=y)

# Instantiate the RandomForestClassifier model (Treebag model) with optimized parameters
treebag_model = RandomForestClassifier(
    n_estimators=200,  # Number of trees
    max_depth=23,       # Maximum depth of the trees
    min_samples_split=2, # Minimum number of samples required to split an internal node
    min_samples_leaf=4,  # Minimum number of samples required to be at a leaf node
    max_features='sqrt', # Number of features to consider when looking for the best split
    bootstrap=False,     # Do not bootstrap samples
    random_state=42
)

# Train the model
treebag_model.fit(X_train, y_train)

# Save the trained model and scaler to disk
pickle.dump(treebag_model, open(r'C:\Users\14701\Desktop\treebag_model.pkl', 'wb'))
pickle.dump(scaler, open(r'C:\Users\14701\Desktop\scaler.pkl', 'wb'))

print("Model and scaler have been saved successfully.")
