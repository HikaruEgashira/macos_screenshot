from dataclasses import dataclass
from typing import List, Optional, Any, Dict


@dataclass
class WindowPosition:
    """ウィンドウの位置情報を表すデータクラス"""

    x: float
    y: float


@dataclass
class WindowSize:
    """ウィンドウのサイズ情報を表すデータクラス"""

    width: float
    height: float


@dataclass
class WindowInfo:
    """ウィンドウの情報を表すデータクラス"""

    title: Optional[str]
    position: Optional[WindowPosition]
    size: Optional[WindowSize]
    role: Optional[str]
    subrole: Optional[str]
    description: Optional[str]
    enabled: bool
    value: Optional[str]
    children: List[Dict[str, Any]]


@dataclass
class ApplicationWindowInfo:
    """アプリケーションのウィンドウ情報を表すデータクラス"""

    app_name: str
    pid: int
    windows: List[WindowInfo]

    @classmethod
    def from_dict(cls, data: dict) -> "ApplicationWindowInfo":
        """辞書からApplicationWindowInfoを生成する"""
        windows = [
            WindowInfo(
                title=w["title"],
                position=WindowPosition(w["position"][0], w["position"][1])
                if w["position"] is not None
                else None,
                size=WindowSize(w["size"][0], w["size"][1])
                if w["size"] is not None
                else None,
                role=w.get("role"),
                subrole=w.get("subrole"),
                description=w.get("description"),
                enabled=w.get("enabled", True),
                value=w.get("value"),
                children=w.get("children", []),
            )
            for w in data["windows"]
        ]
        return cls(
            app_name=data["app_name"],
            pid=data["pid"],
            windows=windows,
        )
