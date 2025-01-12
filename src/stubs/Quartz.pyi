from typing import Any, Dict, List

# Constants
kCGWindowListOptionOnScreenOnly: int
kCGWindowListExcludeDesktopElements: int
kCGNullWindowID: int
kCGWindowImageDefault: int
kCGWindowOwnerName: str
kCGWindowBounds: str

# Types
CGDirectDisplayID = int
CGWindowID = int
CGImageRef = Any  # CoreGraphicsの複雑な型を簡略化

# Window Functions
def CGWindowListCopyWindowInfo(
    option: int, relativeToWindow: CGWindowID
) -> List[Dict[str, Any]]: ...
def CGWindowListCreateImage(
    rect: Any,  # CGRect
    listOption: int,
    windowID: CGWindowID,
    imageOption: int,
) -> CGImageRef: ...

# Geometry
def CGRectMake(x: float, y: float, width: float, height: float) -> Any: ...  # CGRect

# Image Functions
def CGImageGetWidth(image: CGImageRef) -> int: ...
def CGImageGetHeight(image: CGImageRef) -> int: ...
def CGImageGetBitsPerComponent(image: CGImageRef) -> int: ...
def CGImageGetBytesPerRow(image: CGImageRef) -> int: ...
def CGImageGetDataProvider(image: CGImageRef) -> Any: ...  # CGDataProviderRef

# Data Provider Functions
def CGDataProviderCopyData(provider: Any) -> bytes: ...
