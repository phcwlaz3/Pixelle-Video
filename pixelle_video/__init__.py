"""Pixelle-Video: A video generation and processing library.

Fork of AIDC-AI/Pixelle-Video with additional features and improvements.
"""

__version__ = "0.1.0"
__author__ = "Pixelle-Video Contributors"
__license__ = "Apache-2.0"

from pixelle_video.pipeline import PixelleVideoPipeline
from pixelle_video.config import PixelleVideoConfig

__all__ = [
    "PixelleVideoPipeline",
    "PixelleVideoConfig",
    "__version__",
]
