from typing import List, Optional
from ..stubs.AppKit import NSWorkspace, NSRunningApplication


def get_running_apps(
    bundle_identifier: Optional[str] = None,
) -> List[NSRunningApplication]:
    """
    現在動作中のアプリケーションのリストを取得する。

    Args:
        bundle_identifier (Optional[str]): 取得するアプリケーションのバンドルID.
                                         指定しない場合は、全てのアプリケーションを取得する.

    Returns:
        List[NSRunningApplication]: 動作中のアプリケーションのリスト
    """
    workspace = NSWorkspace.sharedWorkspace()
    if bundle_identifier:
        return workspace.runningApplications(withBundleIdentifier=bundle_identifier)
    else:
        return workspace.runningApplications()
