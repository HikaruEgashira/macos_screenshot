from ..stubs.Quartz import (
    CGRectMake,
    CGWindowListCreateImage,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID,
    kCGWindowImageDefault,
    CGImageRef,
)
from .schema import WindowBounds


def capture_window(bounds: WindowBounds) -> CGImageRef:
    """
    指定された範囲のウィンドウをキャプチャする。

    Args:
        bounds (WindowBounds): ウィンドウの範囲情報

    Returns:
        CGImageRef: ウィンドウキャプチャ
    """
    region = CGRectMake(bounds.x, bounds.y, bounds.width, bounds.height)

    options = kCGWindowListOptionOnScreenOnly
    window_capture = CGWindowListCreateImage(
        region, options, kCGNullWindowID, kCGWindowImageDefault
    )

    return window_capture
