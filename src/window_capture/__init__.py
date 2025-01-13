from .schema import WindowCaptureConfig
from .window_info import get_window_bounds
from .capture import capture_window
from .save_image import save_window

__all__ = [
    "WindowCaptureConfig",
    "get_window_bounds",
    "capture_window",
    "save_window",
]
