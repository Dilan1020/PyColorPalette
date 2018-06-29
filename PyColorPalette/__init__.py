name="PycolorPalette"

try:
    from .core import ColorPalette
except ImportError:
    from core import ColorPalette
