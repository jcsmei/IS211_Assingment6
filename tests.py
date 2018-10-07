#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assingment06: A simple unit test for temperature conversions."""


import conversions
import unittest


class TempValues(unittest.TestCase):
    """Class TempValues for the temperature conversion application."""
    degrees = ((88.43, 31.35, 304.5),
               (67.89, 19.94, 293.09),
               (101.12, 38.4, 311.55),
               (13.14, -10.48, 262.67),
               (209.79, 98.77, 371.92))

    def testCelsiusToKelvin(self):
        """Unit test for converting degress Celsius to degrees Kelvin."""
        for deg in self.degrees:
            cel = deg[1]
            kel = deg[2]
            expect = conversions.convertCelsiusToKelvin(cel)
            self.assertEqual(expect, kel, msg=('{} degrees Celsius '
                                               'is not equal to {}'
                                               ' degrees Kelvin.').format(cel, kel))

    def testCelsiusToFahrenheit(self):
        """Unit test for converting degress Celsius to degrees Fahrenheit."""
        for deg in self.degrees:
            cel = deg[1]
            fah = deg[0]
            expect = conversions.convertCelsiusToFahrenheit(cel)
            self.assertEqual(expect, fah, msg=('{} degrees Celsius '
                                               'is not equal to {}'
                                               ' degrees Fahrenheit.').format(cel, fah))

    def testFahrenheitToCelsius(self):
        """Unit test for converting degress Fahrenheit to degrees Celsius."""
        for deg in self.degrees:
            fah = deg[0]
            cel = deg[1]
            expect = conversions.convertFahrenheitToCelsius(fah)
            self.assertEqual(expect, cel, msg=('{} degrees Fahrenheit '
                                               'is not equal to {}'
                                               ' degrees Celsius.').format(fah, cel))

    def testFahrenheitToKelvin(self):
        """Unit test for converting degress Fahrenheit to degrees Kelvin."""
        for deg in self.degrees:
            fah = deg[0]
            kel = deg[2]
            expect = conversions.convertFahrenheitToKelvin(fah)
            self.assertEqual(expect, kel, msg=('{} degrees Fahrenheit '
                                               'is not equal to {}'
                                               ' degrees Kelvin.').format(fah, kel))

    def testKelvinToCelsius(self):
        """Unit test for converting degress Kelvin to degrees Celsius."""
        for deg in self.degrees:
            kel = deg[2]
            cel = deg[1]
            expect = conversions.convertKelvinToCelsius(kel)
            self.assertEqual(expect, cel, msg=('{} degrees Kelvin '
                                               'is not equal to {}'
                                               ' degrees Celsius.').format(kel, cel))

    def testKelvinToFahrenheit(self):
        """Unit test for converting degress Kelvin to degrees Fahrenheit."""
        for deg in self.degrees:
            kel = deg[2]
            fah = deg[0]
            expect = conversions.convertKelvinToFahrenheit(kel)
            self.assertEqual(expect, fah, msg=('{} degrees Kelvin '
                                               'is not equal to {}'
                                               ' degrees Fahrenheit.').format(kel, fah))

if __name__ == '__main__':
    unittest.main()
