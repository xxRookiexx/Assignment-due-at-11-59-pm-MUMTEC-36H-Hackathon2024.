# Western Digital x MUMTEC-36H-Hackathon 2024-
# Assignment-due-at-11-59-pm-MUMTEC-36H-Hackathon2024 - MUMTEC Hackathon 2024 Submission

## Project Title: Redundifier

### Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Features](#features)
6. [Architecture](#architecture)

---

### Project Overview

- **Problem Statement**: Firmware plays a crucial role in the functioning of hardware devices, providing the low-level control required for operation. It also involves time and resources consuming processes. However, traditional firmware development often faces challenges related to performance optimization,  resource management and adaptability to new hardware. Leveraging AI can revolutionise firmware development by automating complex tasks and enhancing performance.
- **Proposed Solution**: Utilise AI to identify redundancies in the code

---
Here's the generated documentation for points 2 to 6 based on the uploaded file:

---

### Technologies Used
- **Python**: Primary programming language used for building the model and data processing.
- **pandas**: A library used for data manipulation and analysis, specifically to load and manage the firmware dataset.
- **scikit-learn**: A machine learning library that provides utilities for preprocessing (CountVectorizer), model building (RandomForestClassifier), and evaluation (train_test_split, accuracy_score, classification_report).
  - **CountVectorizer**: Used to convert text data into numerical data (Bag of Words model).
  - **RandomForestClassifier**: Used for the classification task of identifying efficient and inefficient firmware code.
- **Jupyter Notebook (Optional)**: For experimenting with and running the code.

---

### Installation and Setup

#### Prerequisites:
Ensure you have Python 3.x installed on your system. You will also need `pip` for installing the required packages.

#### Installation Steps:
1. Clone the repository or download the project files to your local machine.
2. Navigate to the project directory:
   ```bash
   cd path_to_project_directory
   ```
3. Install the required Python packages:
   ```bash
   pip install pandas scikit-learn
   ```
4. Ensure you have a dataset in CSV format (`firmware_code_dataset.csv`) containing two columns: 
   - `code`: The firmware code snippets.
   - `label`: The corresponding labels (0 for efficient, 1 for inefficient code).

---

### Usage

1. **Load Dataset**:
   Ensure your dataset is in the project directory. The dataset should contain firmware code snippets and their labels (efficient or inefficient).

2. **Run the Code**:
   Execute the script (`code.py`) to train and evaluate the Random Forest classifier:
   ```bash
   python code.py
   ```

3. **Model Output**:
   - The script will output the **accuracy score** and **classification report**, including precision, recall, and F1-score for each class (efficient and inefficient code).
   - This will help you understand how well the model performs in classifying firmware code.

---

### Features

- **Text Preprocessing with Bag of Words**: Converts raw firmware code into numerical data using the Bag of Words approach, which allows for the application of machine learning models.
  
- **Random Forest Classifier**: A robust ensemble method is used to classify firmware code as efficient or inefficient.

- **Model Evaluation**:
  - **Accuracy**: Provides the overall accuracy of the model on the test dataset.
  - **Classification Report**: A detailed report showing performance metrics like precision, recall, and F1-score for each label (efficient and inefficient).

---

### Architecture

1. **Data Loading**:
   - The firmware dataset is loaded using `pandas` from a CSV file, which contains code snippets and labels.

2. **Preprocessing**:
   - **Bag of Words**: The firmware code snippets are tokenized and converted into a matrix of word counts using `CountVectorizer`.

3. **Model Training**:
   - **Random Forest Classifier**: A machine learning model with 100 estimators (decision trees) is trained on the Bag of Words features to classify the code efficiency.

4. **Train-Test Split**:
   - The dataset is split into a 70% training set and a 30% testing set using `train_test_split`.

5. **Prediction and Evaluation**:
   - The model makes predictions on the test set.
   - Model accuracy is computed, and a detailed classification report is generated, giving performance insights for each class.

---

