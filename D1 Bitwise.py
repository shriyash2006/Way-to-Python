"""
============================================================
Day 01: Python Bitwise Operators & Binary Manipulation
============================================================
Author: Shriyash Sahu
Repo:   https://github.com/shriyash2006/Way-to-Python
Date:   Day 1
Topic:  Bitwise Operators (AND, OR, XOR, NOT, Left Shift, Right Shift)
============================================================
"""

def print_separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


# ==========================================================
# 1. BITWISE AND OPERATOR (&)
# ==========================================================
# Rule: Result bit is 1 ONLY if BOTH corresponding bits are 1.
# ----------------------------------------------------------
def bitwise_and():
    print_separator("1. BITWISE AND OPERATOR (&)")

    # Example 1: 2 & 4
    # 2 in binary: 0 0 1 0
    # 4 in binary: 0 1 0 0
    # ---------------------
    # Result:      0 0 0 0  -> Decimal: 0
    print("Example 1: print(2 & 4)")
    print(f"Result: {2 & 4}")  # Output: 0
    print("Explanation: 2 (0010) & 4 (0100) have no common 1 bits -> 0\n")

    # Example 2: 5 & 7
    # 5 in binary: 0 1 0 1
    # 7 in binary: 0 1 1 1
    # ---------------------
    # Result:      0 1 0 1  -> Decimal: 5
    print("Example 2: print(5 & 7)")
    print(f"Result: {5 & 7}")  # Output: 5
    print("Explanation: 5 (0101) & 7 (0111) -> common set bits are at positions 0 and 2 -> 5")


# ==========================================================
# 2. BITWISE OR OPERATOR (|)
# ==========================================================
# Rule: Result bit is 1 if AT LEAST ONE corresponding bit is 1.
# ----------------------------------------------------------
def bitwise_or():
    print_separator("2. BITWISE OR OPERATOR (|)")

    # Example 1: 2 | 6
    # 2 in binary: 0 0 1 0
    # 6 in binary: 0 1 1 0
    # ---------------------
    # Result:      0 1 1 0  -> Decimal: 6
    print("Example 1: print(2 | 6)")
    print(f"Result: {2 | 6}")  # Output: 6
    print("Explanation: 2 (0010) | 6 (0110) -> combines set bits -> 6 (0110)\n")

    # Example 2: 3 | 4
    # 3 in binary: 0 0 1 1
    # 4 in binary: 0 1 0 0
    # ---------------------
    # Result:      0 1 1 1  -> Decimal: 7
    print("Example 2: print(3 | 4)")
    print(f"Result: {3 | 4}")  # Output: 7
    print("Explanation: 3 (0011) | 4 (0100) -> 0111 in binary -> 7\n")

    # Example 3: 5 | 7
    # 5 in binary: 0 1 0 1
    # 7 in binary: 0 1 1 1
    # ---------------------
    # Result:      0 1 1 1  -> Decimal: 7
    print("Example 3: print(5 | 7)")
    print(f"Result: {5 | 7}")  # Output: 7
    print("Explanation: 5 (0101) | 7 (0111) -> 0111 in binary -> 7")


# ==========================================================
# 3. BITWISE XOR OPERATOR (^)
# ==========================================================
# Rule: Result bit is 1 if bits are DIFFERENT (one is 1, other is 0).
# If both bits are the same (0 and 0, or 1 and 1), result is 0.
# ----------------------------------------------------------
def bitwise_xor():
    print_separator("3. BITWISE XOR OPERATOR (^)")

    # Example 1: 2 ^ 4
    # 2 in binary: 0 0 1 0
    # 4 in binary: 0 1 0 0
    # ---------------------
    # Result:      0 1 1 0  -> Decimal: 6
    print("Example 1: print(2 ^ 4)")
    print(f"Result: {2 ^ 4}")  # Output: 6
    print("Explanation: Bits are different at positions 1 and 2 -> 0110 in binary -> 6\n")

    # Example 2: 7 ^ 5
    # 7 in binary: 0 1 1 1
    # 5 in binary: 0 1 0 1
    # ---------------------
    # Result:      0 0 1 0  -> Decimal: 2
    print("Example 2: print(7 ^ 5)")
    print(f"Result: {7 ^ 5}")  # Output: 2
    print("Explanation: Only the bit at index 1 is different (1 vs 0) -> 0010 in binary -> 2")


# ==========================================================
# 4. BITWISE NOT OPERATOR / GATE (~)
# ==========================================================
# Rule: Inverts all bits (flips 0 to 1 and 1 to 0).
# 💡 TRICK: In Python, numbers use Two's Complement representation.
# Formula: ~n = -(n + 1)
# ----------------------------------------------------------
def bitwise_not():
    print_separator("4. BITWISE NOT OPERATOR (~)")

    # Example 1: ~0
    # Formula trick: -(0 + 1) = -1
    print("Example 1: print(~0)")
    print(f"Result: {~0}")  # Output: -1
    print("💡 Trick Explanation: ~0 = -(0 + 1) = -1\n")

    # Example 2: ~2
    # Formula trick: -(2 + 1) = -3
    print("Example 2: print(~2)")
    print(f"Result: {~2}")  # Output: -3
    print("💡 Trick Explanation: ~2 = -(2 + 1) = -3")


# ==========================================================
# 5. BITWISE LEFT SHIFT (<<)
# ==========================================================
# Rule: Shifts binary bits to the left by specified positions.
# Newly created bit positions on the right are filled with 0.
#
# 💡 TRICK FOR LEFT SHIFT:
# To compute (a << b):
# Take a * (2 ** b)
# Example: 5 << 4 -> 5 * (2 ** 4) = 5 * 16 = 80
# ----------------------------------------------------------
def bitwise_left_shift():
    print_separator("5. BITWISE LEFT SHIFT (<<)")

    # Example 1: 5 << 1
    # 💡 Trick: 5 * (2 ** 1) = 5 * 2 = 10
    print("Example 1: print(5 << 1)")
    print(f"Result: {5 << 1}")  # Output: 10
    print("💡 Trick: (5 << 1) -> 5 * (2^1) = 5 * 2 = 10\n")

    # Example 2: 20 << 2
    # 💡 Trick: 20 * (2 ** 2) = 20 * 4 = 80
    print("Example 2: print(20 << 2)")
    print(f"Result: {20 << 2}")  # Output: 80
    print("💡 Trick: (20 << 2) -> 20 * (2^2) = 20 * 4 = 80\n")

    # Example 3: 5 << 4
    # 💡 Trick: 5 * (2 ** 4) = 5 * 16 = 80
    print("Example 3: print(5 << 4)")
    print(f"Result: {5 << 4}")  # Output: 80
    print("💡 Trick: (5 << 4) -> 5 * (2^4) = 5 * 16 = 80")


# ==========================================================
# 6. BITWISE RIGHT SHIFT (>>)
# ==========================================================
# Rule: Shifts binary bits to the right by specified positions.
# Bits shifted off the right end are discarded.
#
# 💡 TRICK FOR RIGHT SHIFT:
# To compute (a >> b):
# Take a // (2 ** b)  [Floor Division by 2^b]
# Example: 5 >> 1 -> 5 / (2^1) = 5 / 2 = 2.5
# Output is 2 because it takes the floor value (ignores the decimal .5)!
# ----------------------------------------------------------
def bitwise_right_shift():
    print_separator("6. BITWISE RIGHT SHIFT (>>)")

    # Example 1: 5 >> 1
    # 💡 Trick: 5 / (2^1) = 2.5 -> floor division ignores decimal -> 2
    print("Example 1: print(5 >> 1)")
    print(f"Result: {5 >> 1}")  # Output: 2
    print("💡 Trick: 5 / (2^1) = 5 / 2 = 2.5. Floor division drops decimals -> 2\n")

    # Example 2: 5 >> 2
    # 💡 Trick: 5 / (2^2) = 5 / 4 = 1.25 -> floor value -> 1
    print("Example 2: print(5 >> 2)")
    print(f"Result: {5 >> 2}")  # Output: 1
    print("💡 Trick: 5 / (2^2) = 5 / 4 = 1.25. Floor division drops decimals -> 1\n")

    # Example 3: 20 >> 4
    # 💡 Trick: 20 / (2^4) = 20 / 16 = 1.25 -> floor value -> 1
    print("Example 3: print(20 >> 4)")
    print(f"Result: {20 >> 4}")  # Output: 1
    print("💡 Trick: 20 / (2^4) = 20 / 16 = 1.25. Floor division drops decimals -> 1")


# ==========================================================
# 7. PRACTICAL BONUS TRICKS (LeetCode & Interview Patterns)
# ==========================================================
def practical_tricks():
    print_separator("7. PRACTICAL BITWISE TRICKS")

    # Trick A: Check Even or Odd using (n & 1)
    num = 29
    is_even = (num & 1) == 0
    print(f"• Even/Odd Check: Is {num} even? {'Yes' if is_even else 'No'} (Formula: n & 1 == 0)")

    # Trick B: Swap two variables without temporary variable using XOR
    x, y = 15, 42
    print(f"• Swap without temp: Before: x={x}, y={y}")
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(f"  After XOR swap:    x={x}, y={y}")

    # Trick C: Check if a number is a Power of 2 using (n & (n - 1) == 0)
    val = 16
    is_pow2 = (val > 0) and (val & (val - 1) == 0)
    print(f"• Power of 2 Check: Is {val} a power of 2? {is_pow2} (Formula: n & (n - 1) == 0)")


# ==========================================================
# MAIN EXECUTION
# ==========================================================
if __name__ == "__main__":
    print("🐍 DAY 01: PYTHON BITWISE OPERATORS LEARNED TODAY")
    
    bitwise_and()
    bitwise_or()
    bitwise_xor()
    bitwise_not()
    bitwise_left_shift()
    bitwise_right_shift()
    practical_tricks()

    print("\n" + "=" * 60)
    print("✅ All Day 1 Bitwise Examples & Tricks Executed Successfully!")
    print("=" * 60 + "\n")
