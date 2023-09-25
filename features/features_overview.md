# Paycheck - features

Collection of thoughts on the proposed architecture. Very high-level abstraction
of features for our application:

- Loans
- Savings
- Rewards
- KYC

### Deep dive

- Rewards API:
    Manages user rewards for actions like early loan repayments and credit score improvement. 
    It interacts with the Rewards API for reward issuance and redemption

- Support Service: 
    Handles user support requests and communication. It connects with the Support API to manage and resolve support tickets.

- User Management Service: 
    Handles user registration, authentication, and authorization. It integrates with the Authentication
    & Authorization Service to enforce security measures like Two-Factor Authentication and Fingerprint Lock.

- Loans Service: 
    Manages loan applications, approvals, and disbursements. It interacts with the KYC Verification API
    to ensure user identity, and with the Machine Learning Service for fraud detection.

- KYC Verification Service:
    Integrates with the KYC Verification API to verify user identities using various documents and information.

- External Utils service:
    Interfaces with external services such as banking systems, credit bureaus, and third-party APIs.
    Provide service class interfaces and integrations for XML, SOAP (I think some banks uses it not sure), of course, REST APIs, maybe some GraphQL

- Threats/Security Machine Learning Service:
    Incorporates ML models to track fraud detection, detect patterns like late-night withdrawals, and ensure secure financial transactions.

- Disputes Module:
    Handles disputes related to failed transactions and loan repayments.
