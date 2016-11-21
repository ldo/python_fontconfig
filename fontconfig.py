"""
A ctypes-based binding for the Fontconfig API, for Python
3.4 or later.
"""
#+
# Copyright 2016 by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library, in a file named COPYING; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA
#-

import ctypes as ct

fc = ct.cdll.LoadLibrary("libfontconfig.so.1")

class FC :
    "useful definitions from fontconfig/*.h. You will need to use the constants," \
    " but apart from that, see the more Pythonic wrappers defined outside this" \
    " class in preference to accessing low-level structures directly."

    Char8 = ct.c_ubyte
    Char16 = ct.c_ushort
    Char32 = ct.c_uint
    Bool = ct.c_int

    # Current Fontconfig version number
    MAJOR = 2
    MINOR = 11
    REVISION = 0
    VERSION = MAJOR * 10000 + MINOR * 100 + REVISION

    # Current font cache file format version
    CACHE_VERSION = "4"

    # pattern items
    FAMILY = "family" # String
    STYLE = "style" # String
    SLANT = "slant" # Int
    WEIGHT = "weight" # Int
    SIZE = "size" # Double
    ASPECT = "aspect" # Double
    PIXEL_SIZE = "pixelsize" # Double
    SPACING = "spacing" # Int
    FOUNDRY = "foundry" # String
    ANTIALIAS = "antialias" # Bool (depends)
    HINTING = "hinting" # Bool (true)
    HINT_STYLE = "hintstyle" # Int
    VERTICAL_LAYOUT = "verticallayout" # Bool (false)
    AUTOHINT = "autohint" # Bool (false)
    # FC_GLOBAL_ADVANCE is deprecated. this is simply ignored on freetype 2.4.5 or later
    GLOBAL_ADVANCE = "globaladvance" # Bool (true)
    WIDTH = "width" # Int
    FILE = "file" # String
    INDEX = "index" # Int
    FT_FACE = "ftface" # FT_Face
    RASTERIZER = "rasterizer" # String (deprecated)
    OUTLINE = "outline" # Bool
    SCALABLE = "scalable" # Bool
    SCALE = "scale" # double
    DPI = "dpi" # double
    RGBA = "rgba" # Int
    MINSPACE = "minspace" # Bool use minimum line spacing
    SOURCE = "source" # String (deprecated)
    CHARSET = "charset" # CharSet
    LANG = "lang" # String RFC 3066 langs
    FONTVERSION = "fontversion" # Int from 'head' table
    FULLNAME = "fullname" # String
    FAMILYLANG = "familylang" # String RFC 3066 langs
    STYLELANG = "stylelang" # String RFC 3066 langs
    FULLNAMELANG = "fullnamelang" # String RFC 3066 langs
    CAPABILITY = "capability" # String
    FONTFORMAT = "fontformat" # String
    EMBOLDEN = "embolden" # Bool - true if emboldening neede
    EMBEDDED_BITMAP = "embeddedbitmap" # Bool - true to enable embedded bitmaps
    DECORATIVE = "decorative" # Bool - true if style is a decorative variant
    LCD_FILTER = "lcdfilter" # Int
    FONT_FEATURES = "fontfeatures" # String
    NAMELANG = "namelang" # String RFC 3866 langs
    PRGNAME = "prgname" # String
    HASH = "hash" # String
    POSTSCRIPT_NAME = "postscriptname" # String

    CACHE_SUFFIX = ".cache-" + CACHE_VERSION
    DIR_CACHE_FILE = "fonts.cache-" + CACHE_VERSION
    USER_CACHE_FILE = ".fonts.cache-" + CACHE_VERSION

    # Adjust outline rasterizer
    CHAR_WIDTH = "charwidth" # Int
    CHAR_HEIGHT = "charheight" # Int
    MATRIX = "matrix" # FcMatrix

    WEIGHT_THIN = 0
    WEIGHT_EXTRALIGHT = 0
    WEIGHT_ULTRALIGHT = WEIGHT_EXTRALIGHT
    WEIGHT_LIGHT = 0
    WEIGHT_BOOK = 5
    WEIGHT_REGULAR = 0
    WEIGHT_NORMAL = WEIGHT_REGULAR
    WEIGHT_MEDIUM = 0
    WEIGHT_DEMIBOLD = 0
    WEIGHT_SEMIBOLD = WEIGHT_DEMIBOLD
    WEIGHT_BOLD = 0
    WEIGHT_EXTRABOLD = 5
    WEIGHT_ULTRABOLD = WEIGHT_EXTRABOLD
    WEIGHT_BLACK = 0
    WEIGHT_HEAVY = WEIGHT_BLACK
    WEIGHT_EXTRABLACK = 5
    WEIGHT_ULTRABLACK = WEIGHT_EXTRABLACK

    SLANT_ROMAN = 0
    SLANT_ITALIC = 0
    SLANT_OBLIQUE = 0

    WIDTH_ULTRACONDENSED = 0
    WIDTH_EXTRACONDENSED = 3
    WIDTH_CONDENSED = 5
    WIDTH_SEMICONDENSED = 7
    WIDTH_NORMAL = 0
    WIDTH_SEMIEXPANDED = 3
    WIDTH_EXPANDED = 5
    WIDTH_EXTRAEXPANDED = 0
    WIDTH_ULTRAEXPANDED = 0

    PROPORTIONAL = 0
    DUAL = 0
    MONO = 0
    CHARCELL = 0

    # sub-pixel order
    RGBA_UNKNOWN = 0
    RGBA_RGB = 1
    RGBA_BGR = 2
    RGBA_VRGB = 3
    RGBA_VBGR = 4
    RGBA_NONE = 5

    # hinting style
    HINT_NONE = 0
    HINT_SLIGHT = 1
    HINT_MEDIUM = 2
    HINT_FULL = 3

    # LCD filter
    LCD_NONE = 0
    LCD_DEFAULT = 1
    LCD_LIGHT = 2
    LCD_LEGACY = 3

    # enum FcType
    TypeUnknown = -1
    TypeVoid = 0
    TypeInteger = 1
    TypeDouble = 2
    TypeString = 3
    TypeBool = 4
    TypeMatrix = 5
    TypeCharSet = 6
    TypeFTFace = 7
    TypeLangSet = 8

    class Matrix(ct.Structure) :
        _fields_ = \
            [
                ("xx", ct.c_double),
                ("xy", ct.c_double),
                ("yx", ct.c_double),
                ("yy", ct.c_double),
            ]

        @classmethod
        def ident(celf) :
            "alternative to FcMatrixInit."
            return \
                celf(xx = 1, yy = 1, xy = 0, yx = 0)
        #end ident
    #end Matrix

    # FcObjecType, FcConstant TBD

    # enum FcResult
    ResultMatch = 0
    ResultNoMatch = 1
    ResultTypeMismatch = 2
    FcResultNoId = 3
    FcResultOutOfMemory = 4

    # FcValue, FcFontSet, FcObjectSet TBD

    # enum FcMatchKind
    FcMatchPattern = 0
    FcMatchFont = 1
    FcMatchScan = 2

    # enum FcLangResult
    FcLangEqual = 0
    FcLangDifferentCountry = 1
    FcLangDifferentTerritory = 1
    FcLangDifferentLang = 2

    # enum FcSetName
    SetSystem = 0
    SetApplication = 1

#end FC

#+
# Routine arg/result types
#-

# TODO: blanks, cache, config

fc.FcCharSetNew.restype = ct.c_void_p
fc.FcCharSetNew.argtypes = ()
fc.FcCharSetDestroy.restype = None
fc.FcCharSetDestroy.argtypes = (ct.c_void_p,)

# TODO: print, file/dir, fontset

fc.FcInit.restype = FC.Bool
fc.FcInit.argtypes = ()
fc.FcFini.restype = None
fc.FcFini.argtypes = ()
fc.FcGetVersion.restype = ct.c_int
fc.FcGetVersion.argtypes = ()
fc.FcInitReinitialize.restype = FC.Bool
fc.FcInitReinitialize.argtypes = ()
fc.FcInitBringUptoDate.restype = FC.Bool
fc.FcInitBringUptoDate.argtypes = ()

# TODO: lang, objectset/list, atomic, match, matrix, name, pattern/value, str/utf, xml

def init() :
    return \
        fc.FcInit()
#end init

def reinitialize() :
    return \
        fc.FcInitReinitialize()
#end reinitialize

def init_bring_uptodate() :
    return \
        fc.FcInitBringUptoDate()
#end init_bring_uptodate

def fini() :
    fc.FcFini()
#end fini

def get_version() :
    return \
        fc.FcGetVersion()
#end get_version

class CharSet :
    "wrapper around FcCharSet objects. For internal use only: all relevant" \
    " functions will pass and return Python sets."

    __slots__ = \
        ( # to forestall typos
            "_fcobj",
        )

    def __init__(self, _fcobj) :
        self._fcobj = _fcobj
    #end __init__

    def __del__(self) :
        if fc != None and self._fcobj != None :
            fc.FcCharSetDestroy(self._fcobj)
            self._fcobj = None
        #end if
    #end __del__

    @staticmethod
    def to_fc(pyset) :
        TBD
    #end to_fc

#end CharSet

# Pattern, LangSet TBD

# more TBD
