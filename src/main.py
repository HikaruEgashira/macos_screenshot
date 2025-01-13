import os
from typing import List

from .app_list import get_running_apps
from .stubs.AppKit import NSRunningApplication
from .window_capture import (
    get_window_bounds,
    capture_window,
    save_window,
    WindowCaptureConfig,
)


def process_application(app: NSRunningApplication, config: WindowCaptureConfig) -> None:
    """
    アプリケーションのウィンドウをキャプチャする。

    Args:
        app (NSRunningApplication): アプリケーション
        config (WindowCaptureConfig): ウィンドウキャプチャの設定
    """
    try:
        app_name = app.localizedName()
        bundle_id = app.bundleIdentifier()
        if not app_name:
            return

        # フィルタリング状態をログ出力
        if config.filter_mode == "whitelist":
            if bundle_id not in config.allowed_apps:
                return
        elif config.filter_mode == "blacklist":
            if bundle_id in config.blocked_apps:
                return

        # ウィンドウ情報を取得
        windows = get_window_bounds(app, config)

        # 各ウィンドウをキャプチャ
        for i, window in enumerate(windows):
            try:
                # ウィンドウをキャプチャ
                image = capture_window(window)
                if image:
                    # ウィンドウキャプチャを保存
                    save_window(image, f"{app_name}_{i}", config)
                    print(f"Captured: {app_name} (Window {i + 1})")
            except Exception as e:
                print(f"Error capturing window {i + 1} of {app_name}: {str(e)}")
    except Exception as e:
        print(f"Error processing {app.localizedName()}: {str(e)}")


def main() -> None:
    """
    メイン関数
    実行中の全アプリケーションのウィンドウをキャプチャし保存する
    """
    # プロジェクトのルートディレクトリを取得
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # ウィンドウキャプチャの設定
    config = WindowCaptureConfig(
        file_format="png",
        save_dir=os.path.join(root_dir, "out", "screenshots"),
        exclude_menu_bar_apps=True,
        filter_mode="blacklist",  # ブラックリストモードを使用
        blocked_apps=[
            "com.apple.mail",  # Mail
            "com.apple.Safari",  # Safari
            "com.microsoft.VSCode",  # Visual Studio Code
            "com.google.Chrome",  # Chrome
        ],
    )

    # 実行中のアプリケーションを取得
    apps: List[NSRunningApplication] = get_running_apps()

    # 各アプリケーションを処理
    for app in apps:
        process_application(app, config)


if __name__ == "__main__":
    main()
