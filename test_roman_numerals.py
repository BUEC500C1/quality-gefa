#!/usr/bin/python3

import pytest
import os
from roman_numerals import convert

def test_basics():
    numbers = [(1, 'I'), (3, 'III'), (4, 'IV'), (27, 'XXVII'), (44, 'XLIV'),
            (93, 'XCIII'), (141, 'CXLI'), (402, 'CDII'), (575, 'DLXXV'),
            (1024, 'MXXIV'), (3000, 'MMM')]

    for num in numbers:
        assert (num[0] == convert(num[1]))

    for num in numbers:
        assert (num[1] == convert(num[0]))

def test_mkdir():
    os.mkdir('mydir')
    assert os.path.isdir('mydir') == True
    assert os.path.isdir('some_other_dir') == False
