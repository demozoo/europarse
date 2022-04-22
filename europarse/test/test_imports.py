import sys

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class ImportEasterTest(unittest.TestCase):
    """ Test that europarse.easter-related imports work properly """

    def testEasterDirect(self):
        import europarse.easter

    def testEasterFrom(self):
        from europarse import easter

    def testEasterStar(self):
        from europarse.easter import easter


class ImportParserTest(unittest.TestCase):
    """ Test that europarse.parser-related imports work properly """
    def testParserDirect(self):
        import europarse.parser

    def testParserFrom(self):
        from europarse import parser

    def testParserAll(self):
        # All interface
        from europarse.parser import parse
        from europarse.parser import parserinfo

        # Other public classes
        from europarse.parser import parser

        for var in (parse, parserinfo, parser):
            self.assertIsNot(var, None)


class ImportRelativeDeltaTest(unittest.TestCase):
    """ Test that europarse.relativedelta-related imports work properly """
    def testRelativeDeltaDirect(self):
        import europarse.relativedelta

    def testRelativeDeltaFrom(self):
        from europarse import relativedelta

    def testRelativeDeltaAll(self):
        from europarse.relativedelta import relativedelta
        from europarse.relativedelta import MO, TU, WE, TH, FR, SA, SU

        for var in (relativedelta, MO, TU, WE, TH, FR, SA, SU):
            self.assertIsNot(var, None)

        # In the public interface but not in all
        from europarse.relativedelta import weekday
        self.assertIsNot(weekday, None)


class ImportRRuleTest(unittest.TestCase):
    """ Test that europarse.rrule related imports work properly """
    def testRRuleDirect(self):
        import europarse.rrule

    def testRRuleFrom(self):
        from europarse import rrule

    def testRRuleAll(self):
        from europarse.rrule import rrule
        from europarse.rrule import rruleset
        from europarse.rrule import rrulestr
        from europarse.rrule import YEARLY, MONTHLY, WEEKLY, DAILY
        from europarse.rrule import HOURLY, MINUTELY, SECONDLY
        from europarse.rrule import MO, TU, WE, TH, FR, SA, SU

        rr_all = (rrule, rruleset, rrulestr,
                  YEARLY, MONTHLY, WEEKLY, DAILY,
                  HOURLY, MINUTELY, SECONDLY,
                  MO, TU, WE, TH, FR, SA, SU)

        for var in rr_all:
            self.assertIsNot(var, None)

        # In the public interface but not in all
        from europarse.rrule import weekday
        self.assertIsNot(weekday, None)


class ImportTZTest(unittest.TestCase):
    """ Test that europarse.tz related imports work properly """
    def testTzDirect(self):
        import europarse.tz

    def testTzFrom(self):
        from europarse import tz

    def testTzAll(self):
        from europarse.tz import tzutc
        from europarse.tz import tzoffset
        from europarse.tz import tzlocal
        from europarse.tz import tzfile
        from europarse.tz import tzrange
        from europarse.tz import tzstr
        from europarse.tz import tzical
        from europarse.tz import gettz
        from europarse.tz import tzwin
        from europarse.tz import tzwinlocal

        tz_all = ["tzutc", "tzoffset", "tzlocal", "tzfile", "tzrange",
                  "tzstr", "tzical", "gettz"]

        tz_all += ["tzwin", "tzwinlocal"] if sys.platform.startswith("win") else []
        lvars = locals()

        for var in tz_all:
            self.assertIsNot(lvars[var], None)


@unittest.skipUnless(sys.platform.startswith('win'), "Requires Windows")
class ImportTZWinTest(unittest.TestCase):
    """ Test that europarse.tzwin related imports work properly """
    def testTzwinDirect(self):
        import europarse.tzwin

    def testTzwinFrom(self):
        from europarse import tzwin

    def testTzwinStar(self):
        tzwin_all = ["tzwin", "tzwinlocal"]


class ImportZoneInfoTest(unittest.TestCase):
    def testZoneinfoDirect(self):
        import europarse.zoneinfo

    def testZoneinfoFrom(self):
        from europarse import zoneinfo

    def testZoneinfoStar(self):
        from europarse.zoneinfo import gettz
        from europarse.zoneinfo import gettz_db_metadata
        from europarse.zoneinfo import rebuild

        zi_all = (gettz, gettz_db_metadata, rebuild)

        for var in zi_all:
            self.assertIsNot(var, None)
