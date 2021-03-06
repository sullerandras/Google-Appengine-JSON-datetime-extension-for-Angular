Google Appengine JSON datetime extension for Angular
====================================================

It is an extension of simplejson with the same interface, and it
serializes and unserializes Date objects in a way which is compatible
with [Angular](http://www.angularjs.org).

Angular is using this string format for serializing Dates, and
automatically makes a Date object from strings with this format:

    2011-12-17T13:10:33.987Z

This extension is compatible with Python 2.5

How to install
--------------

Just copy this file to anywhere in your project and import it instead of
simplejson.

If you want to use it in Google Appengine (which is not a requirement),
you don't need to add simplejson to your project, since it is already provided
by Google.

How to use
----------

It's the same as you use simplejson:

    import gaejdtefa as json
    import datetime
    
    json.loads('{"created":"2011-12-17T13:10:33.987Z"}')
    
    json.dumps({'created': datetime.datetime.now()})

How to run the tests
--------------------

Download [simplejson](http://pypi.python.org/pypi/simplejson/) and copy the
simplejson folder to this project. So the directory structure should be this:

    + Google-Appengine-JSON-datetime-extension-for-Angular/
    \-+ simplejson/
      +-- tests/
      + tests/
      + README.md
      + gaejdtefa.py

Then in the project folder, you can run the tests with a single commnand:

    python -m unittest tests.TestJson

Version history
---------------

- 1.0.0 - First public release

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
