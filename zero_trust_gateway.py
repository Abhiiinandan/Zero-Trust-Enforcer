import datetime

# --- MOCK DATABASE (Your Policy Decision Point) ---
USERS = {
    "abhinandan": {"role": "admin", "device_id": "DEV-12215656"},
    "guest": {"role": "viewer", "device_id": "DEV-9999"}
}

# --- ZERO TRUST ENGINE ---
def verify_access(username, provided_device_id, location):
    print(f"\n[SYSTEM] Verifying access for: {username}")
    
    # Principle 1: Verify Explicitly (Check identity and Device)
    if username not in USERS:
        return False, "Access Denied: Unknown Identity"
    
    user_data = USERS[username]
    
    # Principle 2: Device Posture Check
    if provided_device_id != user_data["device_id"]:
        return False, "Access Denied: Untrusted Device (Assume Breach logic triggered)"

    # Principle 3: Contextual Check (e.g., Location/Time)
    if location != "Internal Office":
        return False, "Access Denied: Unsecure Location. MFA required."

    return True, f"Access Granted! Welcome {username} [{user_data['role']} role]."

# --- REAL-TIME SIMULATION ---
def main():
    print("--- Zero Trust Architecture Mini-Project ---")
    print("Scenario: User attempting to access Secure Database")
    
    # Input simulation
    user = input("Enter Username: ")
    device = input("Enter Device ID: ")
    loc = input("Enter Location (e.g. Internal Office / Starbucks): ")

    # The Decision
    allowed, message = verify_access(user, device, loc)
    
    if allowed:
        print(f"✅ SUCCESS: {message}")
    else:
        print(f"❌ SECURITY ALERT: {message}")

if __name__ == "__main__":
    main()