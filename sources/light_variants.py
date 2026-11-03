"""Dark-ink versions of the apparel designs for light fabrics (White, Athletic Heather,
Natural, Sport Grey, Sand). Recolors the live print files: cream -> charcoal #1F1F22,
grey labels -> #5A5A5E, amber -> #D0740C (for contrast on light cloth); snowman: the
light title, dashed ring and 'EST.' line outside the badge -> midnight #12284A."""
import sys, numpy as np
from PIL import Image
# usage: python3 light_variants.py fail.png mtbc.png snow.png outdir
