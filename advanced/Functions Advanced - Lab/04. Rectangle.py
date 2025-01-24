def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    return (f"Rectangle area: {area()}\n"
            f"Rectangle perimeter: {perimeter()}")
