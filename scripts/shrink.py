import sys
from opentype_feature_freezer import RemapByOTL
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont


def font_features(ttFont):
    _features = []
    for i, lookup in enumerate(ttFont["GSUB"].table.LookupList.Lookup):
        for featureRecord in ttFont["GSUB"].table.FeatureList.FeatureRecord:
            if (
                not featureRecord.FeatureTag in _features
                and i in featureRecord.Feature.LookupListIndex
            ):
                _features.append(featureRecord.FeatureTag)
                break
    for i, lookup in enumerate(ttFont["GPOS"].table.LookupList.Lookup):
        for featureRecord in ttFont["GPOS"].table.FeatureList.FeatureRecord:
            if (
                not featureRecord.FeatureTag in _features
                and i in featureRecord.Feature.LookupListIndex
            ):
                _features.append(featureRecord.FeatureTag)
                break
    return _features


def shrink(
    ttFont, freezeFeatures=[], removeFeatures=[], glyphs=[], replaceNames="", suffix=""
):

    # Freeze features

    class FreezeOptions(object):
        pass

    options = FreezeOptions()
    options.inpath = ""
    options.outpath = ""
    options.features = ",".join(
        freezeFeatures
    )  # comma-separated list of OpenType feature tags, e.g. 'smcp,c2sc,onum'
    options.script = "latn"  # OpenType script tag, e.g. 'cyrl' (default: '%(default)s')
    options.lang = None  # OpenType language tag, e.g. 'SRB ' (optional)
    options.zapnames = (
        False  # zap glyphnames from the font ('post' table version 3, .ttf only)
    )
    options.rename = (
        True if suffix else False
    )  # add a suffix to the font menu names (by default, the suffix will be constructed from the OpenType feature tags)
    options.usesuffix = suffix  # use a custom suffix when -S is provided
    options.replacenames = replaceNames  # search for strings in the font naming tables and replace them, format is 'search1/replace1,search2/replace2,...'
    options.info = True  # update font version string
    options.report = False  # report languages, scripts and features in font
    options.names = False  # output names of remapped glyphs during processing
    options.verbose = True
    remapByOTL = RemapByOTL(options)
    remapByOTL.ttx = ttFont
    remapByOTL.remapByOTL()
    remapByOTL.renameFont()

    # Subset
    features = list(set(font_features(ttFont)) - set(removeFeatures))
    options = Options(
        layout_features=features,
        name_IDs="*",
        glyph_names=True,
        name_legacy=True,
        name_languages="*",
    )
    subsetter = Subsetter(options=options)

    # populate with unicodes
    unicodes = []
    for t in ttFont["cmap"].tables:
        if t.isUnicode():
            unicodes.extend(list(t.cmap.keys()))
    subsetter.populate(unicodes=unicodes)
    subsetter.subset(ttFont)

    filename = sys.argv[-1]
    if "-" in filename:
        filename = filename.replace("-", suffix + "-")
    elif "[" in filename:
        filename = filename.replace("[", suffix + "[")
    ttFont.save(filename)


# Office
ttFont = TTFont(sys.argv[-1])
shrink(
    ttFont,
    freezeFeatures=["tnum", "lnum", "ss02"],
    removeFeatures=["aalt", "onum", "pnum", "smcp", "c2sc"],
    suffix="Office",
)

# SC
if not "Italic" in sys.argv[-1]:
    ttFont = TTFont(sys.argv[-1])
    shrink(
        ttFont,
        freezeFeatures=["smcp"],
        removeFeatures=["aalt", "c2sc"],
        suffix="SC",
    )

# Infant
ttFont = TTFont(sys.argv[-1])
shrink(
    ttFont,
    freezeFeatures=["ss01", "ss02", "lnum"],
    removeFeatures=["aalt", "pnum", "tnum", "onum"],
    suffix="Infant",
)
