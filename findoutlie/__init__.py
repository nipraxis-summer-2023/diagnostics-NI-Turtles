""" Init for findoutlie module
"""
__version__ = "1.0.0"

from .outfind import find_outliers
from .metrics import dvars
from .detectors import iqr_detector, z_score_detector
