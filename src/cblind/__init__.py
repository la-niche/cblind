__all__ = [
    "Colorplots",
    "cbmap",
    "mapping",
    "reversed_cmap",
    "test_cblind",
    "test_contrast",
    "test_huescale",
    "test_solstice",
    "test_bird",
    "test_pregunta",
    "test_extreme_rainbow",
    "test_rainbow",
    "test_rbscale",
    "test_monocolor",
    "test_mapping",
]

from .cblind import Colorplots, cbmap, mapping, reversed_cmap, test_cblind, test_contrast, test_huescale, test_solstice, test_bird, test_pregunta, test_extreme_rainbow, test_rainbow, test_rbscale, test_monocolor, test_mapping

from .cblind import _register_to_mpl, PALETTES
for name in PALETTES:
    _register_to_mpl(name)

del _register_to_mpl
del PALETTES


def __getattr__(item):
    if item == "__version__":
        from importlib.metadata import version
        return version("cblind")
    raise AttributeError(f"module '{__name__}' has no attribute '{item}'")
