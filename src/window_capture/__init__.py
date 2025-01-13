from .schema import ScreenshotConfig
from .window_info import get_window_bounds
from .capture import capture_screenshot
from .save_image import save_screenshot

__all__ = [
    "ScreenshotConfig",
    "get_window_bounds",
    "capture_screenshot",
    "save_screenshot",
]
