# type: ignore
"""
Quartz framework bindings
"""

from Quartz.CoreGraphics import (
    kCGWindowListOptionOnScreenOnly,
    kCGWindowListExcludeDesktopElements,
    kCGNullWindowID,
    kCGWindowImageDefault,
    kCGWindowOwnerName,
    kCGWindowBounds,
    CGWindowListCopyWindowInfo,
    CGWindowListCreateImage,
    CGRectMake,
    CGImageGetWidth,
    CGImageGetHeight,
    CGImageGetBitsPerComponent,
    CGImageGetBytesPerRow,
    CGImageGetDataProvider,
    CGDataProviderCopyData,
)
from typing import Any

# Constants
__all__ = [
    "kCGWindowListOptionOnScreenOnly",
    "kCGWindowListExcludeDesktopElements",
    "kCGNullWindowID",
    "kCGWindowImageDefault",
    "kCGWindowOwnerName",
    "kCGWindowBounds",
    "CGImageRef",
    "CGWindowListCopyWindowInfo",
    "CGWindowListCreateImage",
    "CGRectMake",
    "CGImageGetWidth",
    "CGImageGetHeight",
    "CGImageGetBitsPerComponent",
    "CGImageGetBytesPerRow",
    "CGImageGetDataProvider",
    "CGDataProviderCopyData",
]

# Types
CGImageRef = Any  # CGImageRefはCの型なので、Pythonでは直接対応する型がない
