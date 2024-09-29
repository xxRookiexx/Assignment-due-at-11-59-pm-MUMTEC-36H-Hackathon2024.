import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
df = pd.read_csv("firmware_code_dataset.csv")

# Step 2: Prepare the Bag of Words model
list_of_strings = df['code'].tolist()
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(list_of_strings)  # Convert code snippets to Bag of Words

# Step 3: Prepare the labels
y = df['label']  # 0 = efficient, 1 = inefficient (redundancy)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = rf_model.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Detailed classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 8: Make a prediction on new firmware code
new_code_snippet = """
// Pin definition
const int ledPin = 13;
int delayDuration = 1000;  // Redundant variable

// Setup function
void setup() {
    pinMode(ledPin, OUTPUT);
}

// Loop function
void loop() {
    digitalWrite(ledPin, HIGH);  // Turn the LED on
    delay(delayDuration);  // Wait for one second
    delay(1000);  // Extra unnecessary delay
    digitalWrite(ledPin, LOW);  // Turn the LED off
    delay(delayDuration);  // Wait for one second
}
"""

# Transform the new code snippet using the Bag of Words model
new_code_vectorized = vectorizer.transform([new_code_snippet])

# Predict whether the new snippet has redundancy
prediction = rf_model.predict(new_code_vectorized)

# Output the prediction
if prediction == 0:
    print("The code is efficient.")
else:
    print("The code has redundancy.")
