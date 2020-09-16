#!/usr/bin/python3

# mixed-number.py
# A program that teaches about and computes mixed numbers from improper
# fractions.
# Copyright (C) 2020  Scott C. MacCallum
# Email: scott@scm.guru

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

numerator = 11
denominator = 7
quotient = numerator // denominator
product = quotient * denominator
difference = numerator - product

print(f'\nHow To Get A Mixed Number From An Improper Fraction\n')

print(f'First, the numerator of the improper faction is divided by the denominator to get the mixed numbers quotient.\n')

print(f'{numerator}')
print(f'-- =')
print(f'{denominator}\n')

print(f'{numerator} / {denominator} = {quotient}\n')

print(f'Second, the quotient is multiplied by the denominator.\n')

print(f'{quotient} x {denominator} = {product}\n')

print(f'Third, the product is subtracted from the numerator.\n')

print(f'{numerator} - {product} = {difference}\n')

print(f'The difference is the mix numbers numerator.\n')

print(f'Fourth, the mixed number is written as the quotient and the mixed numbers numerator over the denominator.\n')

print(f'  {difference}')
print(f'{quotient} --')
print(f'  {  denominator}')

# Write code below that lets the user input an improper fraction for computing.
# The code should validate that the fraction given is improper. If not, let the
# user know that it is not and give them another chance until it is.
