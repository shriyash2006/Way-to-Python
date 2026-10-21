"""
============================================================
Day 01: Python Bitwise Operators & Binary Manipulation
============================================================
Author: Shriyash Sahu
Repo:   https://github.com/shriyash2006/Way-to-Python
Date:   Day 1
Topic:  Bitwise Operations (AND, OR, XOR, NOT, Left Shift, Right Shift)
============================================================
"""

def print_separator(title: str):
    print("\n" + "=" * 55)
    print(f" {title}")
    print("=" * 55)


def bitwise_basics():
    """Demonstrates all 6 core bitwise operators in Python."""
    print_separator("1. Core Bitwise Operators")
    
    a = 12  # Binary: 0000 1100
    b = 10  # Binary: 0000 1010
    
    print(f"a = {a:2d} (Binary: {a:08b})")
    print(f"b = {b:2d} (Binary: {b:08b})")
    print("-" * 35)
    
    # 1. Bitwise AND (&): 1 only if both bits are 1
    and_res = a & b
    print(f"a & b  (AND)         = {and_res:2d} | Binary: {and_res:08b}")
    
    # 2. Bitwise OR (|): 1 if at least one bit is 1
    or_res = a | b
    print(f"a | b  (OR)          = {or_res:2d} | Binary: {or_res:08b}")
    
    # 3. Bitwise XOR (^): 1 if bits are different
    xor_res = a ^ b
    print(f"a ^ b  (XOR)         = {xor_res:2d} | Binary: {xor_res:08b}")
    
    # 4. Bitwise NOT (~): Inverts all bits (Two's complement: ~x = -(x + 1))
    not_a = ~a
    print(f"~a     (NOT/Invert)  = {not_a:2d} | (Formula: -(a + 1))")
    
    # 5. Bitwise Left Shift (<<): Shifts bits left, multiplies by 2^n
    lshift = a << 2  # 12 * 2^2 = 48
    print(f"a << 2 (Left Shift)  = {lshift:2d} | Binary: {lshift:08b} (a * 2^2)")
    
    # 6. Bitwise Right Shift (>>): Shifts bits right, floor division by 2^n
    rshift = a >> 2  # 12 // 2^2 = 3
    print(f"a >> 2 (Right Shift) = {rshift:2d} | Binary: {rshift:08b} (a // 2^2)")


def practical_applications():
    """Real-world tricks and algorithmic use cases using bit manipulation."""
    print_separator("2. Practical Tricks & LeetCode Patterns")
    
    # Trick 1: Check if an integer is Odd or Even
    num = 29
    is_even = (num & 1) == 0
    print(f"• Is {num} even? {'Yes' if is_even else 'No'} (Check: num & 1 == 0)")
    
    # Trick 2: Swap two variables without temporary variable
    x, y = 15, 42
    print(f"• Before Swap: x = {x}, y = {y}")
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(f"• After Swap:  x = {x}, y = {y}")
    
    # Trick 3: Check if a number is a Power of 2
    # Powers of 2 have only one bit set (e.g., 8 is 1000, 7 is 0111 -> 8 & 7 == 0)
    test_val = 16
    is_power_of_two = (test_val > 0) and (test_val & (test_val - 1) == 0)
    print(f"• Is {test_val} a power of 2? {is_power_of_two} (Check: n & (n - 1) == 0)")
    
    # Trick 4: Count Set Bits (Brian Kernighan's Algorithm)
    def count_set_bits(n: int) -> int:
        count = 0
        original = n
        while n > 0:
            n &= (n - 1)  # Clears the lowest set bit
            count += 1
        return count
    
    sample_n = 29  # 29 in binary is 0001 1101 (4 set bits)
    print(f"• Number of set bits in {sample_n} ({sample_n:b}): {count_set_bits(sample_n)}")
    
    # Trick 5: Bitmasking - Set, Clear, Toggle, and Check ith bit (0-indexed)
    val = 0b00001010  # 10 in decimal
    bit_pos = 2
    print(f"\n• Initial binary:       {val:08b} (decimal {val})")
    
    # Set bit
    set_bit = val | (1 << bit_pos)
    print(f"  Set bit {bit_pos}:           {set_bit:08b} (decimal {set_bit})")
    
    # Clear bit
    clear_bit = set_bit & ~(1 << bit_pos)
    print(f"  Clear bit {bit_pos}:         {clear_bit:08b} (decimal {clear_bit})")
    
    # Toggle bit
    toggled = val ^ (1 << bit_pos)
    print(f"  Toggle bit {bit_pos}:        {toggled:08b} (decimal {toggled})")
    
    # Check if bit is set
    is_set = (val & (1 << 3)) != 0
    print(f"  Is bit 3 set in {val}? {is_set}")


if __name__ == "__main__":
    print("🚀 Day 1: Starting Python Learning Journey!")
    bitwise_basics()
    practical_applications()
    print("\n✅ Day 1 Completed Successfully!\n")
