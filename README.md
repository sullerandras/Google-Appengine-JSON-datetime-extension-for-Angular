Google Appengine JSON datetime extension for Angular
====================================================

It is an extension for simplejson with the same interface, and it
serializes and unserializes Date objects in a way which is compatible
with [Angular](http://www.angularjs.org).

Angular is using this string format for serializing Dates, and
automatically makes a Date object from strings with this format:
2011-12-17T13:10:33.987Z

This extension is compatible with Python 2.5

How to use
----------

>from gaejdtefa import json
>import datetime
>
>json.loads('{"created":"2011-12-17T13:10:33.987Z"}')
>
>json.dumps({'created': datetime.now()})</pre>


