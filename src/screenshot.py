from .stubs.Quartz import (
    CGRectMake,
    CGWindowListCreateImage,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID,
    kCGWindowImageDefault,
    CGImageRef,
)
from .models import WindowBounds


def capture_screenshot(bounds: WindowBounds) -> CGImageRef:
    """
    指定された範囲のスクリーンショットを取得する。

    Args:
        bounds (WindowBounds): ウィンドウの範囲情報

    Returns:
        CGImageRef: スクリーンショット
    """
    region = CGRectMake(bounds.x, bounds.y, bounds.width, bounds.height)

    options = kCGWindowListOptionOnScreenOnly
    screenshot = CGWindowListCreateImage(
        region, options, kCGNullWindowID, kCGWindowImageDefault
    )

    return screenshot
