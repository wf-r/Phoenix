#---------------------------------------------------------------------------
# Name:        etg/propgridmanager.py
# Author:      Robin Dunn
#
# Created:     31-Aug-2016
# Copyright:   (c) 2016-2017 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"
MODULE    = "_propgrid"
NAME      = "propgridmanager"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script.
ITEMS  = [ 'wxPropertyGridPage',
           'wxPropertyGridManager',
           ]

#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)

    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.


    c = module.find('wxPropertyGridPage')
    assert isinstance(c, etgtools.ClassDef)
    tools.ignoreConstOverloads(c)


    module.addGlobalStr('wxPropertyGridManagerNameStr', c)

    c = module.find('wxPropertyGridManager')
    tools.fixWindowClass(c, hideVirtuals=False, ignoreProtected=False)
    tools.ignoreConstOverloads(c)


    # wxPGPropArg is a typedef for "const wxPGPropArgCls&" so having the
    # wrappers treat it as a normal type can be problematic. ("new cannot be
    # applied to a reference type", etc.) Let's just ignore it an replace it
    # everywhere for the real type.
    for item in module.allItems():
        if hasattr(item, 'type') and item.type == 'wxPGPropArg':
            item.type = 'const wxPGPropArgCls &'


    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)


#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()
