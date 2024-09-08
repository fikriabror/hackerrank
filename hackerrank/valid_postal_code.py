import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

def is_valid(P):
    return (
        bool(re.match(regex_integer_in_range, P))  # Check if P matches the integer range regex
        and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2  # Ensure fewer than 2 alternating repetitive digit pairs
    )

# Example usage
P = "123456"
print(is_valid(P)) 