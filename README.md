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

### Technologies Used

- Python 3.12
- Python modules:
    sklearn
    pandas

---

### Installation and Setup
1. Install the technologies used
2. Download the code file
3. 

---

### Usage


---

### Features
The key features include being able to 

---

### Architecture
The program is a machine learning model that uses a Random Forest Classifier to analyze firmware code snippets, categorizing them as either efficient or inefficient based on a Bag of Words (BoW) model.

Imports:
pandas: For data handling and reading the dataset.
CountVectorizer: To convert text data (firmware code) into numerical features using a Bag of Words approach.
train_test_split: To split the dataset into training and testing sets.
RandomForestClassifier: Machine learning model used for classification.
accuracy_score and classification_report: For evaluating the model's performance.

Data Loading:
The code reads a dataset (firmware_code_dataset.csv) containing firmware code snippets.
The dataset has two columns: code (the firmware code) and label (0 for efficient code, 1 for inefficient/redundant code).

Data Preprocessing:
The code column is converted into a numerical representation using the Bag of Words model (using CountVectorizer).
Labels (y) are extracted for classification (0 = efficient, 1 = inefficient).

Train-Test Split:
The dataset is split into training (70%) and testing (30%) sets using train_test_split.

Model Training:
A Random Forest Classifier is initialized and trained on the training data (X_train and y_train).

Prediction:
The trained model makes predictions on the test set (X_test).

Model Evaluation:
The model's accuracy is calculated using accuracy_score.
A detailed classification report (precision, recall, F1-score) is generated using classification_report.

---
