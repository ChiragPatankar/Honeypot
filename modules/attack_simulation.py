def simulate_attack(attack_type, username, password):
    if attack_type == "SQL Injection":
        print(f"SQL Injection simulated with input: {username}' OR '1'='1")
    elif attack_type == "XSS":
        print(f"XSS simulated with script: <script>alert('Hacked!')</script>")
    else:
        print("No attack simulated")
