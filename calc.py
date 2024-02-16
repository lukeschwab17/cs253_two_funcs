# calc.py

def calculate(current_value, num, clear):
    # replace so it looks better on user interface
    if clear:
        return ''  # Clear the current value if clear button is pressed
    elif num:
        if num == '=':
            # Calculate result if '=' is pressed
            try:
                # Safely evaluate the current expression
                return str(eval(current_value))
            except:
                return 'Error'
        else:
            # Append the pressed button value to the current value
            return current_value + num
    return current_value
