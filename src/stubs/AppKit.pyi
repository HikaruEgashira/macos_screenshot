from typing import List, Protocol, overload

class NSRunningApplication:
    def localizedName(self) -> str: ...

class NSWorkspaceProtocol(Protocol):
    @overload
    def runningApplications(self) -> List[NSRunningApplication]: ...
    @overload
    def runningApplications(
        self, withBundleIdentifier: str
    ) -> List[NSRunningApplication]: ...

class NSWorkspace:
    @staticmethod
    def sharedWorkspace() -> NSWorkspaceProtocol: ...
