#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assingment06: A simple application for temperature conversions."""

import decimal


def convertCelsiusToKelvin(degrees):
    """A function to convert degrees Celsius to degrees kelvin.

    Args:
        degrees (int, float): A number to be converted.

    Returns:
        integer (int, float): A number that was converted from the argument.

    Examples:
    >>> convertCelsiusToKelvin(53)
    326.15
    >>> convertCelsiusToKelvin(33)
    306.15
    >>> convertCelsiusToKelvin(23.45)
    296.6
    """
    degress = str(degrees)
    convert = (decimal.Decimal(degrees) + decimal.Decimal('273.15'))
    return float(convert)


def convertCelsiusToFahrenheit(degrees):
    """A function to convert degrees Celsius to degrees Fahrenheit.

    Args:
        degrees (int, float): A number to be converted.

    Returns:
        integer (int, float): A number that was converted from the argument.

    Examples:
    >>> convertCelsiusToFahrenheit(22.15)
    99.15
    >>> convertCelsiusToFahrenheit(111.11)
    188.11
    >>> convertCelsiusToFahrenheit(5.65)
    82.65
    """
    degress = str(degrees)
    convert = (decimal.Decimal(degrees) * 9 / 5) + 32
    return round(float(convert), 2)


def convertFahrenheitToCelsius(degrees):
    """A function to convert degrees Fahrenheit to degrees Celsius.

    Args:
        degrees (int, float): A number to be converted.

    Returns:
        integer (int, float): A number that was converted from the argument.

    Examples:
    >>> convertFahrenheitToCelsius(102.64)
    39.24
    >>> convertFahrenheitToCelsius(75)
    23.89
    >>> convertFahrenheitToCelsius(66.5)
    19.17
    """
    degress = str(degrees)
    convert = (decimal.Decimal(degrees) - 32) * 5 / 9
    return round((float(convert)), 2)


def convertFahrenheitToKelvin(degrees):
    """A function to convert degrees Fahrenheit to degrees Kelvin.

    Args:
        degrees (int, float): A number to be converted.

    Returns:
        integer (int, float): A number that was converted from the argument.

    Examples:
    >>> convertFahrenheitToKelvin(77.89)
    298.64
    >>> convertFahrenheitToKelvin(120)
    322.04
    >>> convertFahrenheitToKelvin(99.95)
    310.9
    """
    degress = str(degrees)
    convert = ((decimal.Decimal(degrees) - 32 ) * 5 / 9 +
               decimal.Decimal('273.15'))
    return round((float(convert)), 2)


def convertKelvinToCelsius(degrees):
    """A function to convert degrees Kelvin to degrees Celsius.

    Args:
        degrees (int, float): A number to be converted.

    Returns:
        integer (int, float): A number that was converted from the argument.

    Examples:
    >>> convertKelvinToCelsius(300.56)
    27.41
    >>> convertKelvinToCelsius(56)
    -217.15
    >>> convertKelvinToCelsius(-56)
    -329.15
    """
    degress = str(degrees)
    convert = (decimal.Decimal(degrees) - decimal.Decimal('273.15'))
    return round((float(convert)), 2)


def convertKelvinToFahrenheit(degrees):
    """A function to convert degrees Kelvin to degrees Fahrenheit.

    Args:
        degrees (int, float): A number to be converted.

    Returns:
        integer (int, float): A number that was converted from the argument.

    Examples:
    >>> convertKelvinToFahrenheit(-2345)
    -4680.67
    >>> convertKelvinToFahrenheit(105)
    -270.67
    >>> convertKelvinToFahrenheit(33.689)
    -399.03
    """
    degress = str(degrees)
    convert = ((decimal.Decimal(degrees) - decimal.Decimal('273.15')) * 9 / 5
               + 32)
    return round((float(convert)), 2)
