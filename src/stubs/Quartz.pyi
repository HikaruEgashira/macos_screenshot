"""
Quartz framework bindings for type checking
"""

from typing import Any, Dict, List, Tuple, Protocol
from typing_extensions import Buffer

class CGImage:
    """CGImage representation"""

    pass

class CGDataProvider:
    """CGDataProvider representation"""

    pass

class CFData(Buffer):
    """CFData representation with buffer protocol support"""
    def __bytes__(self) -> bytes: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: int) -> int: ...

CGImageRef = CGImage
CGDataProviderRef = CGDataProvider
CFDataRef = CFData
CGRect = Tuple[float, float, float, float]

# Constants
kCGWindowListOptionOnScreenOnly: int
kCGWindowListExcludeDesktopElements: int
kCGNullWindowID: int
kCGWindowImageDefault: int
kCGWindowOwnerName: str
kCGWindowBounds: str

# Functions
def CGWindowListCopyWindowInfo(
    option: int, relativeToWindow: int
) -> List[Dict[str, Any]]: ...
def CGWindowListCreateImage(
    rect: CGRect, listOption: int, windowID: int, imageOption: int
) -> CGImageRef: ...
def CGRectMake(x: float, y: float, width: float, height: float) -> CGRect: ...
def CGImageGetWidth(image: CGImageRef) -> int: ...
def CGImageGetHeight(image: CGImageRef) -> int: ...
def CGImageGetBytesPerRow(image: CGImageRef) -> int: ...
def CGImageGetDataProvider(image: CGImageRef) -> CGDataProviderRef: ...
def CGDataProviderCopyData(provider: CGDataProviderRef) -> CFDataRef: ...
