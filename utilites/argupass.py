import argparse
import unittest

parser = argparse.ArgumentParser(description='Pass Browser')

parser.add_argument('-browser', type=str, help='string1')
args = parser.parse_args()

browser=args.browser
if __name__ == '__main__':
    from Tests.FlightBookingMain import TestFlight
    testLoad = unittest.TestLoader()
    testSuite = testLoad.loadTestsFromTestCase(TestFlight)
    runner = unittest.TextTestRunner()
    runner.run(testSuite)