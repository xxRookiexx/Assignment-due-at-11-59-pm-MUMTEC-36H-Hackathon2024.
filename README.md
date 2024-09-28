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
- **Proposed Solution**: Develop an AI model that uses Bag of Words (BoW) model to analyse code and predict its redundancy. 

- **Additional Problem Statemeent**: The most main problem associate with our digital industry identity system are certificate fraud, fake credentials, slow verification processes, and data breaches. To overcome this problem, there is a need of decentralized identity technology which it helps create fraud-proof credentials and empowers verifying organizations to instantly check the authenticity of those credentials. Individuals fully own and control their digital identity and credentials without relying on any third party/centralized server to prove their claims.   
- **Proposed Solution**: Blockchain-Based Identity Management System: This is a smart contract written in Solidity for managing decentralized identity on the Ethereum blockchain. It allows user registration, token-based identity verification, and permission/role management through a smart contract.

---

### Technologies Used

#### AI-Based Firmware Code Analysis
- **Python**: The main programming language for this project.
- **pandas**: For handling and manipulating the dataset.
- **scikit-learn**: Provides machine learning models and utilities, such as Random Forest, CountVectorizer, and evaluation metrics.
  - **CountVectorizer**: Converts firmware code snippets into a numerical Bag of Words format.
  - **RandomForestClassifier**: The classification model used to predict code efficiency.

#### Blockchain-Based Identity Management System
- **Solidity**: A high-level programming language for writing smart contracts on the Ethereum blockchain.
- **Ethereum Blockchain**: The decentralized platform where the smart contract is deployed and interacts with user accounts.
- **Remix IDE** (Optional): A browser-based IDE for writing and deploying Solidity contracts.
- **MetaMask** (Optional): An Ethereum wallet for deploying and interacting with the smart contract.

---

### Installation and Setup

#### AI-Based Firmware Code Analysis
1. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages using:
   ```bash
   pip install pandas scikit-learn
   ```

2. **Prepare the Dataset**:
   Ensure you have a CSV file named `firmware_code_dataset.csv` with columns `code` (firmware code snippets) and `label` (0 for efficient, 1 for inefficient).

#### Blockchain-Based Identity Management System
1. **Set up MetaMask**:
   Install MetaMask and connect to an Ethereum test network such as Ropsten or Ganache (for local testing).

2. **Open Remix IDE**:
   Compile the Solidity contract in Remix using version `^0.8.0`.

3. **Deploy the Contract**:
   Deploy the smart contract either to a local blockchain (Ganache) or a testnet using MetaMask.

---

### Usage

#### AI-Based Firmware Code Analysis
1. **Run the Script**:
   After placing the dataset in the same directory, run the Python script:
   ```bash
   python code.py
   ```

2. **Output**:
   - The script will output the model's accuracy and a classification report, showing the performance for efficient and inefficient code snippets.

#### Blockchain-Based Identity Management System
1. **Register a New User**:
   Call the `registerUser` function with your public key as an argument to register yourself.
   ```solidity
   registerUser("your_public_key");
   ```

2. **Generate a Token**:
   Users can generate a token with an expiry time to be used for identity verification.
   ```solidity
   generateToken(duration_in_seconds);
   ```

3. **Admin Functions**:
   Admins can assign or revoke permissions, and assign roles to users.
   ```solidity
   assignPermission(userAddress, "permissionName");
   revokePermission(userAddress, "permissionName");
   assignRole(userAddress, 1); // Assign admin role
   ```

---

### Features

#### AI-Based Firmware Code Analysis
- **Text Vectorization**: Uses the Bag of Words model to convert firmware code into numerical features.
- **Random Forest Classifier**: Classifies firmware code snippets into efficient and inefficient categories.
- **Performance Evaluation**: Provides accuracy scores and a detailed classification report.

#### Blockchain-Based Identity Management System
- **User Registration**: Allows users to register their identity by storing their Ethereum address and public key.
- **Token-Based Identity Verification**: Users can generate time-limited tokens for identity verification.
- **Role Management**: Admins can assign or revoke roles (admin/user) to control access to certain functions.
- **Permission System**: Admins can assign or revoke permissions for specific users.
- **Event Logging**: Logs events like user registration, token generation, and permission/role changes for accountability.

---

### 6. Architecture

#### AI-Based Firmware Code Analysis
1. **Data Loading**: Loads the firmware dataset from a CSV file.
2. **Preprocessing**: Uses the Bag of Words model to convert text data (firmware code) into numerical vectors.
3. **Model Training**: A Random Forest Classifier is trained on the processed data to classify code as efficient or inefficient.
4. **Train-Test Split**: The dataset is split into 70% training and 30% testing sets for evaluation.
5. **Evaluation**: Accuracy and classification reports are generated to assess the model's performance.

#### Blockchain-Based Identity Management System
1. **User Struct**: Defines user data, including ID, address, public key, and role.
2. **Mappings**:
   - **User Mapping**: Stores user details using their Ethereum address as the key.
   - **Permission Mapping**: Nested mappings that link user addresses to permissions.
3. **Modifiers**:
   - **onlyAdmin**: Restricts certain functions to admin users only.
4. **Core Functions**:
   - **registerUser**: Registers a new user with a public key.
   - **generateToken**: Generates a token for identity verification with a specified expiry time.
   - **assignPermission**: Allows admins to assign permissions to users.
   - **revokePermission**: Admins can revoke permissions.
   - **assignRole**: Admins can assign roles to users (regular or admin).
   - **verifyIdentity**: Verifies a user’s identity by checking if their token has expired.

---
