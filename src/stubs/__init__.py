"""
Type stubs for macOS system frameworks
"""

from .AppKit import NSRunningApplication, NSWorkspace
from .Quartz import (
    CGImageRef,
    CGWindowListCopyWindowInfo,
    CGWindowListCreateImage,
    CGRectMake,
    CGImageGetWidth,
    CGImageGetHeight,
    CGImageGetBytesPerRow,
    CGImageGetDataProvider,
    CGDataProviderCopyData,
    kCGWindowListOptionOnScreenOnly,
    kCGWindowListExcludeDesktopElements,
    kCGNullWindowID,
    kCGWindowImageDefault,
    kCGWindowOwnerName,
    kCGWindowBounds,
)

__all__ = [
    "NSRunningApplication",
    "NSWorkspace",
    "CGImageRef",
    "CGWindowListCopyWindowInfo",
    "CGWindowListCreateImage",
    "CGRectMake",
    "CGImageGetWidth",
    "CGImageGetHeight",
    "CGImageGetBytesPerRow",
    "CGImageGetDataProvider",
    "CGDataProviderCopyData",
    "kCGWindowListOptionOnScreenOnly",
    "kCGWindowListExcludeDesktopElements",
    "kCGNullWindowID",
    "kCGWindowImageDefault",
    "kCGWindowOwnerName",
    "kCGWindowBounds",
]
