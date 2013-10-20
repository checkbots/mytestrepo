"""Sekhar: Unit tests for roman.py using py.test framework
"""


import sys
import roman
import pytest


# To demonstrate a module level fixture, use fixture to initialize test
# data for our positive test cases.
@pytest.fixture(scope="module")
def initTestData():
    """return some known test data"""
    print "Creating test data.."
    return ((1, 'I'),
           (2, 'II'),
           (3, 'III'),
           (4, 'IV'),
           (5, 'V'),
           (6, 'VI'),
           (7, 'VII'),
           (8, 'VIII'),
           (9, 'IX'),
           (10, 'X'),
           (50, 'L'),
           (100, 'C'),
           (500, 'D'),
           (1000, 'M'),
           (31, 'XXXI'),
           (148, 'CXLVIII'),
           (294, 'CCXCIV'),
           (312, 'CCCXII'),
           (421, 'CDXXI'),
           (528, 'DXXVIII'),
           (621, 'DCXXI'),
           (782, 'DCCLXXXII'),
           (870, 'DCCCLXX'),
           (941, 'CMXLI'),
           (1043, 'MXLIII'),
           (1110, 'MCX'),
           (1226, 'MCCXXVI'),
           (1301, 'MCCCI'),
           (1485, 'MCDLXXXV'),
           (1509, 'MDIX'),
           (1607, 'MDCVII'),
           (1754, 'MDCCLIV'),
           (1832, 'MDCCCXXXII'),
           (1993, 'MCMXCIII'),
           (2074, 'MMLXXIV'),
           (2152, 'MMCLII'),
           (2212, 'MMCCXII'),
           (2343, 'MMCCCXLIII'),
           (2499, 'MMCDXCIX'),
           (2574, 'MMDLXXIV'),
           (2646, 'MMDCXLVI'),
           (2723, 'MMDCCXXIII'),
           (2892, 'MMDCCCXCII'),
           (2975, 'MMCMLXXV'),
           (3051, 'MMMLI'),
           (3185, 'MMMCLXXXV'),
           (3250, 'MMMCCL'),
           (3313, 'MMMCCCXIII'),
           (3408, 'MMMCDVIII'),
           (3501, 'MMMDI'),
           (3610, 'MMMDCX'),
           (3743, 'MMMDCCXLIII'),
           (3844, 'MMMDCCCXLIV'),
           (3888, 'MMMDCCCLXXXVIII'),
           (3940, 'MMMCMXL'),
           (3999, 'MMMCMXCIX'),
           (4000, 'MMMM'),
           (4500, 'MMMMD'),
           (4888, 'MMMMDCCCLXXXVIII'),
           (4999, 'MMMMCMXCIX'))


@pytest.mark.smoke
def testToRomanKnownValues(initTestData):
    """toRoman should give known result with known input"""
    for integer, numeral in initTestData:
        result = roman.toRoman(integer)
        assert numeral == result


@pytest.mark.smoke
def testFromRomanKnownValues(initTestData):
    """fromRoman should give known result with known input"""
    for integer, numeral in initTestData:
        result = roman.fromRoman(numeral)
        assert integer == result


@pytest.mark.extended
def testToRomanTooLarge():
    """toRoman should fail with large input"""
    with pytest.raises(roman.OutOfRangeError):
        roman.toRoman(4999)


@pytest.mark.extended
def testToRomanZero():
    """toRoman should fail with 0 input"""
    with pytest.raises(roman.OutOfRangeError):
        roman.toRoman(0)


@pytest.mark.extended
@pytest.mark.skipif("sys.platform != 'win32'", reason='Run this only on Win')
def testToRomanNegative():
    """toRoman should fail with negative input"""
    with pytest.raises(roman.OutOfRangeError):
        roman.toRoman(-1)


# This test demonstrates use of xfail mark. This test is "expected to
# fail", because we have not implemented a decimal check yet in the code.
@pytest.mark.extended
@pytest.mark.xfail(reason='Have not implemented non-integer check yet')
def testToRomanDecimal():
    """toRoman should fail with non-integer input"""
    with pytest.raises(roman.NotIntegerError):
        roman.toRoman(0.5)


# This test demonstrates parametrization. Test fuction is run with
# each of the parameters from the list as a seperate test.
@pytest.mark.basic
@pytest.mark.parametrize("str",
                         ['MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'])
def testFromRomanTooManyRepeatedNumerals(str):
    """fromRoman should fail with too many repeated numerals"""
    with pytest.raises(roman.InvalidRomanNumeralError):
        roman.fromRoman(str)


@pytest.mark.basic
@pytest.mark.parametrize("str",
                         ['CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'])
def testFromRomanRepeatedPairs(str):
    """fromRoman should fail with repeated pairs of numerals"""
    with pytest.raises(roman.InvalidRomanNumeralError):
        roman.fromRoman(str)


@pytest.mark.basic
@pytest.mark.parametrize("str", ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                                 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'))
def testFromRomanMalformedAntecedent(str):
    """fromRoman should fail with malformed antecedents"""
    with pytest.raises(roman.InvalidRomanNumeralError):
        roman.fromRoman(str)


@pytest.mark.basic
def testFromRomanBlank():
    """fromRoman should fail with blank string"""
    with pytest.raises(roman.InvalidRomanNumeralError):
        roman.fromRoman("")


@pytest.mark.basic
def testSanity():
    """fromRoman(toRoman(n))==n for all n"""
    for integer in range(1, 5000):
        numeral = roman.toRoman(integer)
        result = roman.fromRoman(numeral)
        assert integer == result


@pytest.mark.extended
def testToRomanCase():
    """toRoman should always return uppercase"""
    for integer in range(1, 5000):
        numeral = roman.toRoman(integer)
        assert numeral == numeral.upper()


@pytest.mark.extended
def testFromRomanCase():
    """fromRoman should only accept uppercase input"""
    for integer in range(1, 5000):
        numeral = roman.toRoman(integer)
        roman.fromRoman(numeral.upper())
        with pytest.raises(roman.InvalidRomanNumeralError):
            roman.fromRoman(numeral.lower())
