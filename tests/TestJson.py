import unittest
import gaejdtefa as json
import datetime

ZERO = datetime.timedelta(0)

class UTC(datetime.tzinfo):
    """UTC"""
    def utcoffset(self, dt):
        return ZERO
    def tzname(self, dt):
        return "UTC"
    def dst(self, dt):
        return ZERO

utc = UTC()

class TestJson(unittest.TestCase):

    def test_dumps_with_tz(self):
        now = datetime.datetime(2011, 12, 17, 13, 10, 33, 987654, tzinfo=utc)
        self.assertEqual(json.dumps({'created': now}), '{"created": "2011-12-17T13:10:33.987Z"}')
        now = datetime.datetime(2011, 12, 17, 13, 10, 33, 123456, tzinfo=utc)
        self.assertEqual(json.dumps({'created': now}), '{"created": "2011-12-17T13:10:33.123Z"}')

    def test_dumps_without_tz(self):
        now = datetime.datetime(2011, 12, 17, 13, 10, 33, 987654) # local timezone
        res = json.dumps({'created': now})
        # we don't know the exact time, since it depends on the local timezone
        self.assertEqual(res[0 : 22], '{"created": "2011-12-1')
        self.assertEqual(res[26 : ], ':10:33.987Z"}')

    def test_loads_and_dumps(self):
        s = '{"created": "2011-12-17T13:10:33.987Z"}'
        res = json.loads(s)
        # we don't know the exact time, since it depends on the local timezone
        self.assertNotEqual(res['created'], None)
        self.assertEqual(res['created'].year, 2011)
        self.assertEqual(res['created'].month, 12)
        self.assertEqual(res['created'].minute, 10)
        self.assertEqual(res['created'].second, 33)
        self.assertEqual(res['created'].microsecond, 987000)
        # convert it to UTC timezone, so we can check the exact time
        d = json._datetime_to_UTC(res['created'])
        self.assertEqual(res['created'].year, 2011)
        self.assertEqual(res['created'].month, 12)
        self.assertEqual(res['created'].day, 17)
        self.assertEqual(res['created'].hour, 13)
        self.assertEqual(res['created'].minute, 10)
        self.assertEqual(res['created'].second, 33)
        self.assertEqual(res['created'].microsecond, 987000)
        self.assertEqual(json.dumps(res), s)

if __name__ == '__main__':
    unittest.main()
