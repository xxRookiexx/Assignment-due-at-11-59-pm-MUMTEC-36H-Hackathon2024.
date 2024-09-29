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
  
- **Proposed Solution**: Develop a website that integrates GroqCloud AI to optimise and debug firmware using prompt engineering. The website then predicts what could have caused the error (hardware or system).  

- **Additional Problem Statemeent**: The most main problem associate with our digital industry identity system are certificate fraud, fake credentials, slow verification processes, and data breaches. To overcome this problem, there is a need of decentralized identity technology which it helps create fraud-proof credentials and empowers verifying organizations to instantly check the authenticity of those credentials. Individuals fully own and control their digital identity and credentials without relying on any third party/centralized server to prove their claims.
  
- **Proposed Solution**: Blockchain-Based Identity Management System: This is a smart contract written in Solidity for managing decentralized identity on the Ethereum blockchain. It allows user registration, token-based identity verification, and permission/role management through a smart contract.

---

### Technologies Used

#### AI-Based Firmware Code Analysis
- **Python**: The main programming language for this project.
- **Groq**:  developers to compile machine learning models to be executed on Groq hardware. 
- **Gradio**: Provides methods and tools for website creation. 

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
   pip install -q groq
   pip install gradio
   ```
   
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
   After downloading Redundify.py, run the Python script:
   ```bash
   python3 Redundify.py
   ```
2. **Output**:
   - The script will be executed in a terminal, showing a temporary URL to a website. Enter the firmware in the input box and click 'Redundi-fy' to optimise and debug your firmware. 
   
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
- **Explanation of Redundancy:**: Elaboration given on unsuitable lines of codes.
- **Recommended Code Improvements**: Provides recommendation on code optimisation. 

#### Blockchain-Based Identity Management System
- **User Registration**: Allows users to register their identity by storing their Ethereum address and public key.
- **Token-Based Identity Verification**: Users can generate time-limited tokens for identity verification.
- **Role Management**: Admins can assign or revoke roles (admin/user) to control access to certain functions.
- **Permission System**: Admins can assign or revoke permissions for specific users.
- **Event Logging**: Logs events like user registration, token generation, and permission/role changes for accountability.

---

### 6. Architecture

#### AI-Based Firmware Code Analysis

1. **Input Layer**: The firmware textbox allows the user to input code.The Gradio UI captures this input and passes it to the backend function.
2. **Processing Layer**: The redundify() function processes the user input by sending it to the Groq API. The Groq API's AI model processes the firmware code for redundancy detection, optimization, and bug detection. The result is formatted and returned as a string.
3. **Output Layer**: The Gradio UI displays the processed result in the output textbox. This allows users to see exactly what lines are redundant and receive suggestions and explanations.

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
