# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Step 1: Load the Dataset
# Assuming we downloaded 'spam.csv' from Kaggle and placed it in the same folder as this script.
data = pd.read_csv('spam.csv', encoding='latin-1')

# View the first few rows to understand the structure (Optional)
print(data.head())

# The dataset has some unnecessary columns, so we’ll keep only 'v1' and 'v2' for label and message.
# Rename the columns to make them more intuitive: 'label' for spam/ham and 'message' for text.
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Convert labels to binary values: 1 for spam, 0 for ham.
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Step 2: Split the Data
# Split the data into training and testing sets. We use an 80/20 split.
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label'], test_size=0.2, random_state=42
)

# Step 3: Vectorize the Text Data using TF-IDF
# Convert the text messages into numerical form using TF-IDF vectorization.
# TF-IDF stands for Term Frequency-Inverse Document Frequency, a popular method to process text for machine learning.
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Fit the vectorizer on the training data and transform both training and testing data.
# Fitting on the training data means calculating the importance of each word based on the training messages.
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Step 4: Train the Model
# We'll use Multinomial Naive Bayes as it works well for text classification problems.
classifier = MultinomialNB()

# Train the classifier on the TF-IDF-transformed training data.
classifier.fit(X_train_tfidf, y_train)

# Step 5: Make Predictions
# Use the trained model to predict labels for the test set.
y_pred = classifier.predict(X_test_tfidf)

# Step 6: Evaluate the Model
# Check the model’s performance using accuracy, precision, recall, and F1-score.
# Accuracy is the percentage of correct predictions out of total predictions.
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Testing the saved model (Optional)
# Example usage after loading the model and vectorizer:
#sample_message = ["Congratulations! Won a free ticket to Bahamas!"]
#sample_message_tfidf = vectorizer.transform(sample_message)
#print(classifier.predict(sample_message_tfidf))  # Output will be 1 for spam, 0 for ham
