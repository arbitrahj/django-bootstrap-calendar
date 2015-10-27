#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj_calendar
------------

Tests for `dj_calendar` modules module.
"""

import os
import shutil
import unittest
from datetime import datetime

from dj_calendar.utils import datetime_to_timestamp
from dj_calendar.utils import timestamp_to_datetime


class Testdj_calendar(unittest.TestCase):

    def setUp(self):
        print "Running some basic test"
        pass

    def test_convert_datetime_to_timestamp(self):
        value ='1376978400000'
        self.assertEquals(value, datetime_to_timestamp(
            datetime(2013, 8, 20, 8, 00)
        ), msg = "testing" )

    def test_convert_timestamp_to_datetime(self):
        value = datetime(2013, 8, 20, 8, 00)
        self.assertEquals(value, timestamp_to_datetime('1376978400000'))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
