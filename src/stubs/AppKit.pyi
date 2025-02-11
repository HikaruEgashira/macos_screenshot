"""
AppKit framework bindings for type checking
"""

from typing import List, Optional

class NSRunningApplication:
    def processIdentifier(self) -> int: ...
    def localizedName(self) -> str: ...
    def bundleIdentifier(self) -> str: ...

class NSWorkspace:
    @staticmethod
    def sharedWorkspace() -> "NSWorkspace": ...
    def runningApplications(
        self, withBundleIdentifier: Optional[str] = None
    ) -> List[NSRunningApplication]: ...

# Export the types for use in other modules
NSWorkspace = NSWorkspace
NSRunningApplication = NSRunningApplication
