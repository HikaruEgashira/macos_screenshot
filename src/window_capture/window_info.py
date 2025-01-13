from typing import List, Dict, Any
from ..stubs.Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGWindowListExcludeDesktopElements,
    kCGNullWindowID,
    kCGWindowOwnerName,
    kCGWindowBounds,
)
from ..stubs.AppKit import NSRunningApplication
from .schema import WindowBounds, ScreenshotConfig


def get_window_bounds(
    app: NSRunningApplication, config: ScreenshotConfig
) -> List[WindowBounds]:
    """
    アプリケーションのウィンドウ情報を取得し、ウィンドウの範囲情報を返す。

    Args:
        app (NSRunningApplication): アプリケーション
        config (ScreenshotConfig): スクリーンショット設定

    Returns:
        List[WindowBounds]: ウィンドウの範囲情報のリスト
    """
    # アプリケーションのフィルタリングチェック
    bundle_id = app.bundleIdentifier
    if config.filter_mode == "whitelist" and bundle_id not in config.allowed_apps:
        return []
    if config.filter_mode == "blacklist" and bundle_id in config.blocked_apps:
        return []

    options = kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements
    windows: List[Dict[str, Any]] = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    app_windows: List[WindowBounds] = []

    for window in windows:
        window_owner_name = window.get(kCGWindowOwnerName, "")
        if window_owner_name == app.localizedName():
            bounds = window.get(kCGWindowBounds)
            if bounds:
                # メニューバー領域のウィンドウをチェック
                if (
                    config.exclude_menu_bar_apps
                    and bounds["Y"] < config.menu_bar_height
                ):
                    continue

                app_windows.append(
                    WindowBounds(
                        x=bounds["X"],
                        y=bounds["Y"],
                        width=bounds["Width"],
                        height=bounds["Height"],
                    )
                )

    return app_windows
