from dataclasses import dataclass
from typing import List, Optional
from .stubs.AppKit import NSRunningApplication
from .stubs.Quartz import CGImageRef


@dataclass
class WindowBounds:
    """ウィンドウの範囲情報を表すデータクラス"""

    x: float
    y: float
    width: float
    height: float


@dataclass
class ScreenshotConfig:
    """スクリーンショットの設定を表すデータクラス"""

    file_format: str = "png"
    save_dir: str = "./screenshots"
    exclude_menu_bar_apps: bool = False  # メニューバーのアプリを除外するかどうか
    menu_bar_height: int = 25  # macOSのメニューバーの高さ（ピクセル）


@dataclass
class ApplicationWindow:
    """アプリケーションのウィンドウ情報を表すデータクラス"""

    app: NSRunningApplication
    bounds: List[WindowBounds]
    name: str
    screenshot: Optional[CGImageRef] = None
