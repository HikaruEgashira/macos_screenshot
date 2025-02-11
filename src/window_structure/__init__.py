"""
macOSのウィンドウ構造を取得するモジュール
"""

from .window_info import get_all_window_info, get_app_windows, get_window_info
from .schema import (
    WindowInfo,
    WindowPosition,
    WindowSize,
    ApplicationWindowInfo,
)
from .cli import main

__all__ = [
    "WindowInfo",
    "WindowPosition",
    "WindowSize",
    "ApplicationWindowInfo",
    "get_all_window_info",
    "get_app_windows",
    "get_window_info",
    "main",
]
