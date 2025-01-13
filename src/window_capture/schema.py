from dataclasses import dataclass, field
from typing import List, Optional
from ..stubs.AppKit import NSRunningApplication
from ..stubs.Quartz import CGImageRef


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
    filter_mode: str = "none"  # "none", "whitelist", "blacklist"のいずれか
    allowed_apps: List[str] = field(
        default_factory=list
    )  # ホワイトリストモード時に許可するアプリのbundle identifier
    blocked_apps: List[str] = field(
        default_factory=list
    )  # ブラックリストモード時に禁止するアプリのbundle identifier

    def __post_init__(self):
        """データクラスの初期化後の処理"""
        if self.filter_mode not in ["none", "whitelist", "blacklist"]:
            raise ValueError("filter_mode must be one of: none, whitelist, blacklist")


@dataclass
class ApplicationWindow:
    """アプリケーションのウィンドウ情報を表すデータクラス"""

    app: NSRunningApplication
    bounds: List[WindowBounds]
    name: str
    screenshot: Optional[CGImageRef] = None
