import os
import unittest
from unittests import wtc

import wx.lib.agw.scrolledthumbnail as ST

pngFile = os.path.join(os.path.dirname(__file__), 'toucan.png')
#---------------------------------------------------------------------------

class lib_agw_scrolledthumbnail_Tests(wtc.WidgetTestCase):

    def test_lib_agw_scrolledthumbnailMethods(self):
        t1 = ST.Thumb(os.path.dirname(__file__), 'toucan.png')
        self.assertEqual(t1.GetOriginalSize(), None)
        self.assertEqual(
            t1.GetInfo(),
            "Name: toucan.png\nSize: 0 bytes\nModified: 0\nDimensions: (162,150)\n"
        )

#---------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
