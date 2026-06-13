import re
import random
import string

# ─────────────────────────────────────────────
# FUNCTION 1: Analyze the password strength
# ─────────────────────────────────────────────
def analyze_password(password):
    score = 0
    feedback = []

    # Check 1: Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short! Use at least 8 characters (12+ is best).")

    # Check 2: Uppercase letters (A-Z)
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one UPPERCASE letter (e.g., A, B, C).")

    # Check 3: Lowercase letters (a-z)
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (e.g., a, b, c).")

    # Check 4: Numbers (0-9)
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (e.g., 1, 2, 3).")

    # Check 5: Special symbols
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    else:
        feedback.append("❌ Add at least one special character (e.g., @, #, $, !).")

    # Check 6: Common weak passwords
    common_passwords = ["password", "123456", "password123", "admin", "qwerty", "letmein"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ This is a very common password! Never use this.")

    return score, feedback


# ─────────────────────────────────────────────
# FUNCTION 2: Convert score to strength label
# ─────────────────────────────────────────────
def get_strength_label(score):
    if score <= 1:
        return "🔴 WEAK"
    elif score <= 3:
        return "🟠 MODERATE"
    elif score <= 5:
        return "🟡 STRONG"
    else:
        return "🟢 VERY STRONG"


# ─────────────────────────────────────────────
# FUNCTION 3: Generate a strong password
# ─────────────────────────────────────────────
def generate_strong_password(length=14):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        score, _ = analyze_password(password)
        if score >= 6:  # Only return if it's very strong
            return password


# ─────────────────────────────────────────────
# MAIN PROGRAM — This runs when you start it
# ─────────────────────────────────────────────
def main():
    print("=" * 50)
    print("       🔐 PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Check my password")
        print("  2. Generate a strong password")
        print("  3. Exit")
        print()

        choice = input("Enter your choice (1/2/3): ").strip()

        # ── Option 1: Check a password ──
        if choice == "1":
            password = input("\nEnter your password: ")

            score, feedback = analyze_password(password)
            strength = get_strength_label(score)

            print("\n" + "-" * 40)
            print(f"  Password : {'*' * len(password)}")
            print(f"  Score    : {score} / 7")
            print(f"  Strength : {strength}")
            print("-" * 40)

            if feedback:
                print("\n📋 How to improve:")
                for tip in feedback:
                    print(f"   {tip}")
            else:
                print("\n✅ Excellent! Your password is very strong.")

            if score < 5:
                suggestion = generate_strong_password()
                print(f"\n💡 Suggested strong password: {suggestion}")

        # ── Option 2: Generate a password ──
        elif choice == "2":
            print("\nGenerating a strong password for you...")
            new_password = generate_strong_password()
            print(f"\n✅ Your new strong password: {new_password}")
            print("💾 Save this somewhere safe!")

        # ── Option 3: Exit ──
        elif choice == "3":
            print("\n👋 Goodbye! Stay secure!")
            break

        else:
            print("⚠️  Invalid choice. Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()