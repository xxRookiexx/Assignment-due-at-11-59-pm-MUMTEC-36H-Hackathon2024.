// SPDX-License-Identifier: MIT
// Declaring the version of Solidity to use
pragma solidity ^0.8.0;

// Contract definition for Identity Management System
contract IdentityManagement {
    
    // Structure to represent a User in the system
    struct User {
        uint256 id;               // Unique identifier for each user
        address userAddress;      // Ethereum address of the user
        string publicKey;         // User's public key for cryptographic purposes
        bool isRegistered;        // Flag to check if user is registered
        uint256 tokenExpiry;      // Expiry timestamp for the user's token
        uint8 role;               // User's role (0 for regular users, 1 for admins)
    }

    // Mapping from user addresses to their corresponding User struct
    mapping(address => User) public users;

    // Nested mapping to manage permissions for each user
    // Maps user address to a mapping of permission names (strings) to boolean values (granted/denied)
    mapping(address => mapping(string => bool)) public permissions;

    // Counter to track the number of registered users
    uint256 public userCount;

    // Events to log significant actions within the contract
    event UserRegistered(address userAddress, string publicKey);
    event TokenGenerated(address userAddress, uint256 expiry);
    event PermissionAssigned(address userAddress, string permission);
    event PermissionRevoked(address userAddress, string permission);
    event RoleAssigned(address userAddress, uint8 role);

    // Modifier to restrict function access to admin users only
    modifier onlyAdmin() {
        require(users[msg.sender].role == 1, "Not an admin"); // Check if the caller is an admin
        _; // Placeholder for the function body
    }

    // Function to register a new user in the system
    function registerUser(string memory publicKey) public {
        require(!users[msg.sender].isRegistered, "User already registered"); // Check if user is already registered
        userCount++; // Increment user count
        // Create a new user with their public key and mark them as registered
        users[msg.sender] = User(userCount, msg.sender, publicKey, true, 0, 0);
        emit UserRegistered(msg.sender, publicKey); // Emit the UserRegistered event
    }

    // Function to generate a token for the user with a specified duration
    function generateToken(uint256 duration) public {
        require(users[msg.sender].isRegistered, "User not registered"); // Check if the user is registered
        uint256 expiry = block.timestamp + duration; // Calculate the expiry time based on the current timestamp and duration
        users[msg.sender].tokenExpiry = expiry; // Update the user's token expiry time
        emit TokenGenerated(msg.sender, expiry); // Emit the TokenGenerated event
    }

    // Function to verify the identity of the user based on their token
    function verifyIdentity() public view returns (bool) {
        // Return true if the user is registered and their token has not expired
        return users[msg.sender].isRegistered && users[msg.sender].tokenExpiry > block.timestamp;
    }

    // Function to assign a permission to a specific user
    function assignPermission(address userAddress, string memory permission) public onlyAdmin {
        require(users[userAddress].isRegistered, "User not registered"); // Check if the user is registered
        permissions[userAddress][permission] = true; // Grant the specified permission to the user
        emit PermissionAssigned(userAddress, permission); // Emit the PermissionAssigned event
    }

    // Function to revoke a permission from a specific user
    function revokePermission(address userAddress, string memory permission) public onlyAdmin {
        require(users[userAddress].isRegistered, "User not registered"); // Check if the user is registered
        permissions[userAddress][permission] = false; // Revoke the specified permission from the user
        emit PermissionRevoked(userAddress, permission); // Emit the PermissionRevoked event
    }

    // Function to assign a role to a specific user (e.g., admin or user)
    function assignRole(address userAddress, uint8 role) public onlyAdmin {
        require(users[userAddress].isRegistered, "User not registered"); // Check if the user is registered
        users[userAddress].role = role; // Assign the specified role to the user
        emit RoleAssigned(userAddress, role); // Emit the RoleAssigned event
    }

    // Function to check if a specific user has a certain permission
    function checkPermission(address userAddress, string memory permission) public view returns (bool) {
        return permissions[userAddress][permission]; // Return the permission status (true/false)
    }
}

