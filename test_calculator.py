import pytest
import math
from calculator_project import calculate, preprocess_expression, tk, clear_entry, create_entry

TOLERANCE = 1e-10

def test_calculate():
    # Test basic arithmetic
    assert calculate("2 + 3 * 4 - 1") == 13

    # Test division
    assert calculate("10 / 2") == 5

    # Test trigonometric functions with tolerance
    expected_value = math.sin(math.radians(90)) + math.cos(math.radians(45))
    assert calculate("(sin(90)) + (cos(45))") == pytest.approx(expected_value, rel=TOLERANCE)

    # Test error handling for division by zero
    with pytest.raises(ValueError, match="Error: Division by zero"):
        calculate("1 / 0")

    # Test error handling for invalid expressions
    with pytest.raises(ValueError, match="Error: "):
        calculate("1 + abc")

def test_clear_entry():
    # Create a Tkinter Entry widget for testing
    root = tk.Tk()
    entry = create_entry(root)
    
    # Set some initial value in the Entry widget
    entry.insert(tk.END, "12345")

    # Call the clear_entry function
    clear_entry(entry)

    # Check if the Entry widget is cleared
    assert entry.get() == ""  # Assert that the entry is cleared
    assert entry.index(tk.END) == 0  # Assert that the cursor is at the beginning of the entry



if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
