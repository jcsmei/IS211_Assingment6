#!/sur/bin/env python
#! -*- coding: utf-8 -*-
"""IS211_Assingment06: A simple mehtod for conversion refractor."""


import unittest
import decimal

class ConvertNotPossible(Exception):
    """A custom exception class for."""
    pass

kel_cel = decimal.Decimal('273.15')
kel_fah = decimal.Decimal('459.67')
div95 = decimal.Decimal('9') / 5
div59 = decimal.Decimal('5') / 9


formulas = {
    'fah': {'cel': (-32, div59, 0),
            'kel': (kel_fah, div59, 0)},
    'cel': {'kel': (kel_cel, 1, 0),
            'fah': (0, div95, 32)},
    'kel': {'cel': (-kel_cel, 1, 0),
            'fah': (0, div95, -kel_fah)},
    'mil': {'yar': (0, decimal.Decimal(1760), 0),
             'met': (0, decimal.Decimal(.9144), 0)},
    'yar': {'mil': (0, decimal.Decimal(.0005682), 0),
              'met': (0, decimal.Decimal(.9144), 0)},
    'met': {'mil': (0, decimal.Decimal(.0006214), 0),
            'yar': (0, decimal.Decimal(1.0936), 0)}
    }


def convert(fromUnit, toUnit, value):
    """A function for all conversions; temperature (fahrenheit, celsius, kelvin)
    and distance (miles, yards, meters).

    Args:
        fromUnit (str): what unit is being converted
        toUnit (str): what the value is being converted to
        value (int, float): a value that will be converted

    Returns:
        value (int, float): the converted value in the appropriate unit

    Examples:
    >>> convert('celsius', 'kelvin', 123)
    396.15
    >>> convert('miles', 'yards', 2.5)
    4400.0
    >>> convert('fahrenheit', 'celsius', 345)
    173.889
    """
    from_unit = fromUnit[:3].lower()
    to_unit = toUnit[:3].lower()
    val = decimal.Decimal(value)
    if from_unit == to_unit:
        return float(val)
    elif to_unit in formulas[from_unit]:
        conversions = (
            (val + formulas[from_unit][to_unit][0])
            * (formulas[from_unit][to_unit][1])
            + (formulas[from_unit][to_unit][2])
            )
        return round(float(conversions), 3)
    else:
        raise ConvertNotPossible('Units cannot be converted.')


class ConversionTests(unittest.TestCase):
    """A class for testing refactored conversions."""
    converse = [('Fahrenheit', 'Celsius', 572, 300),
                ('Fahrenheit', 'Kelvin', 84, 302.04),
                ('Celsius', 'Fahrenheit', 50.81, 123.45),
                ('Celsius', 'Kelvin', 50.81, 323.96),
                ('Kelvin', 'Celsius', 323.96, 50.81),
                ('Kelvin', 'Fahrenheit', 323.96, 123.45),
                ('Miles', 'Yards', 1, 1760),
                ('Miles', 'Meters', 1.25, 2011.68),
                ('Yards', 'Miles', 3520, 2),
                ('Yards', 'Meters', 123, 112.48),
                ('Meters', 'Miles', 678, .42),
                ('Meters', 'Yards', 123, 134.51)]

    def testConversions(self):
        """A function to test all conversions."""
        for i in self.converse:
            self.assertEqual(convert(i[0], i[1], i[2], i[3]))

    def testUnitType(self):
        """A function to test if unit type is the same"""
        for t in formulas:
            self.assertEqual(convert(t, t, 1.0), 1.0)

    def testUnitConvert(self):
        """A test to raise excpetion if units cannot be converted."""
        self.assertRaises(ConvertNotPossible, convert, 'Yards', 'Fahrenheit', 123)


if __name__ == '__main__':
    unittest.main()
