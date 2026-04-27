# Zero-Trust-Enforcer

# Zero Trust Architecture (ZTA) 
This is a Python implementation of a **Policy Enforcement Point (PEP)** based on my Seminar "Zero Trust Architecture in Modern Cybersecurity".

## Features
- **Verify Explicitly:** Validates Identity + Device ID.
- **Least Privilege:** Checks user roles before access.
- **Context-Aware:** Detects location-based risks.

## How to run
1. Install Python.
2. Run `python zero_trust_gateway.py`.
3. Try logging in with: 
   - User: `abhinandan`
   - Device: `DEV-12215656`
   - Location: `Internal Office`
   - (this is only an example login to show how it needs every criteria matched and passed to login.)
