#!/usr/bin/env python3

import logging
from typing import List, Optional, Dict, Any
from AppKit import NSWorkspace, NSRunningApplication
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID,
)
from .schema import WindowInfo, WindowPosition, WindowSize, ApplicationWindowInfo

logger = logging.getLogger(__name__)

# Accessibility constants
kAXWindowsAttribute = "AXWindows"
kAXTitleAttribute = "AXTitle"
kAXPositionAttribute = "AXPosition"
kAXSizeAttribute = "AXSize"
kAXSubroleAttribute = "AXSubrole"
kAXRoleAttribute = "AXRole"
kAXChildrenAttribute = "AXChildren"
kAXDescriptionAttribute = "AXDescription"
kAXValueAttribute = "AXValue"
kAXEnabledAttribute = "AXEnabled"


def get_window_info(window_dict: Dict[str, Any]) -> Optional[WindowInfo]:
    """ウィンドウの情報を取得する"""
    try:
        # タイトルの取得
        title = window_dict.get("kCGWindowName")

        # 位置の取得
        bounds = window_dict.get("kCGWindowBounds", {})
        position_info = (
            WindowPosition(x=bounds.get("X", 0), y=bounds.get("Y", 0))
            if bounds
            else None
        )

        # サイズの取得
        size_info = (
            WindowSize(width=bounds.get("Width", 0), height=bounds.get("Height", 0))
            if bounds
            else None
        )

        # 役割とサブロールの取得
        role = window_dict.get("kCGWindowLayer", "")
        subrole = window_dict.get("kCGWindowOwnerName", "")
        description = window_dict.get("kCGWindowName", "")
        enabled = True  # CoreGraphicsではこの情報は取得できない
        value = window_dict.get("kCGWindowAlpha")

        # 子要素の取得（CoreGraphicsではこの情報は取得できない）
        children: List[Dict[str, Any]] = []

        return WindowInfo(
            title=title,
            position=position_info,
            size=size_info,
            role=str(role),
            subrole=str(subrole),
            description=description,
            enabled=enabled,
            value=str(value) if value is not None else None,
            children=children,
        )
    except Exception as e:
        logger.error(f"Error getting window info: {e}", exc_info=True)
        return None


def get_app_windows(pid: int) -> List[WindowInfo]:
    """アプリケーションのすべてのウィンドウ情報を取得する"""
    windows = []
    window_list = CGWindowListCopyWindowInfo(
        kCGWindowListOptionOnScreenOnly, kCGNullWindowID
    )

    if window_list:
        for window in window_list:
            if window.get("kCGWindowOwnerPID") == pid:
                window_info = get_window_info(window)
                if window_info:
                    windows.append(window_info)

    return windows


def get_all_window_info() -> List[ApplicationWindowInfo]:
    """すべての実行中のアプリケーションのウィンドウ情報を取得する"""
    workspace = NSWorkspace.sharedWorkspace()
    running_apps = workspace.runningApplications()

    window_info_list = []
    for app in running_apps:
        if not isinstance(app, NSRunningApplication):
            continue

        try:
            pid = app.processIdentifier()
            app_name = app.localizedName()

            windows = get_app_windows(pid)
            if windows:
                window_info_list.append(
                    ApplicationWindowInfo(
                        app_name=app_name,
                        pid=pid,
                        windows=windows,
                    )
                )
        except Exception as e:
            logger.error(f"Error processing app {app}: {e}", exc_info=True)
            continue

    return window_info_list
