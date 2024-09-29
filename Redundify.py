#First AI - classifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers
from sentence_transformers import SentenceTransformer


# Step 1: Load your dataset
# Assuming your dataset has two columns: 'error' and 'solution'
data = pd.read_csv('/Users/a27/Desktop/firmware_code_errors.csv')

# Step 2: Preprocess the data using Sentence-Transformers
# Initialize the sentence transformer model (pre-trained)
model_name = 'all-MiniLM-L6-v2'  # You can choose different models from the Hugging Face library
embedding_model = SentenceTransformer(model_name)

# Function to get embeddings from Sentence-Transformers
def get_embedding(text):
    return embedding_model.encode(text, convert_to_numpy=True)

# Apply the embedding function to the 'error' column
data['errors'] = data['code_snippet'].apply(get_embedding)

# Convert the embeddings into numpy array format
X = np.array(data['errors'].to_list())

# Encode solutions into class labels
le = LabelEncoder()
data['solution'] = le.fit_transform(data['error_label'])
y = np.array(data['solution'])

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Build the Neural Network model using TensorFlow
model = tf.keras.Sequential([
layers.InputLayer(input_shape=(len(X[0]),)),  # Input shape matches embedding length
layers.Dense(128, activation='relu'),
layers.Dropout(0.2),
layers.Dense(64, activation='relu'),
layers.Dropout(0.2),
layers.Dense(len(np.unique(y)), activation='softmax')  # Output layer for multi-class classification
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Step 5: Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Step 6: Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy}")

def classify(firmware):
    new_error_embedding = np.array(get_embedding(firmware)).reshape(1, -1)
    predicted_solution_label = np.argmax(model.predict(new_error_embedding), axis=1)[0] 
    predicted_solution = le.inverse_transform([predicted_solution_label])[0]
    return predicted_solution

#---------------------------------------------------------------------------------#

import os 
from groq import Groq 

def redundify(firmware):
    client = Groq(api_key = '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')
    stream = client.chat.completions.create(
        messages = [
            {
        'role': 'user',
        'content': f'Look at this code: \n {firmware} \n point out the specific line of codes that are redundant and can be optimised, give recommended code for the selected lines and reason they are redundant. If there are bugs, debug it and show the line of code where the bug is. Give the answer in readable bullet points.'
    }], 
        model = 'mixtral-8x7b-32768',
        #stream = True, 
    )
    #for chunk in stream: 
        #a = chunk.choices[0].delta.content, end= ""
    stream = stream.choices[0].message.content
    return(stream)

def classifier(firmware):
    return {'key': 'value'}

import gradio as gr
html = """<html><body><h1>Redundify: What, where and why.</h1></body></html>"""
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    input_mic = gr.HTML(html)
    firmware = gr.Textbox(label="Initial firmware", elem_id = "input")
    output1 = gr.Textbox(label="New Solution by AI", elem_id = 'new')
    output2 = gr.Textbox(label= "Solution from Dataset", elem_id = 'old')
    red_btn = gr.Button("Redundi-fy")
    red_btn.click(fn = redundify, inputs= firmware, outputs = output1, api_name="redundify")
    red_btn.click(fn = classify, inputs= firmware, outputs = output2, api_name="redundify2")
    @gr.render(inputs= firmware)
    def show_split(text):
        if len(text) == 0:
            gr.Markdown("## No Input Provided")

    



demo.launch()





