import os
from typing import List
from .stubs.AppKit import NSRunningApplication
from .app_list import get_running_apps
from .window_info import get_window_bounds
from .screenshot import capture_screenshot
from .save_image import save_screenshot
from .models import ScreenshotConfig


def process_application(app: NSRunningApplication, config: ScreenshotConfig) -> None:
    """
    アプリケーションのスクリーンショットを処理する。

    Args:
        app (NSRunningApplication): アプリケーション
        config (ScreenshotConfig): スクリーンショットの設定
    """
    try:
        # アプリケーション名を取得
        app_name = app.localizedName()
        if not app_name:
            return

        # ウィンドウ情報を取得
        windows = get_window_bounds(app, config)

        # 各ウィンドウのスクリーンショットを取得
        for i, window in enumerate(windows):
            try:
                # スクリーンショットを取得
                image = capture_screenshot(window)
                if image:
                    # スクリーンショットを保存
                    save_screenshot(image, f"{app_name}_{i}", config)
                    print(f"Captured: {app_name} (Window {i + 1})")
            except Exception as e:
                print(f"Error capturing window {i + 1} of {app_name}: {str(e)}")
    except Exception as e:
        print(f"Error processing {app.localizedName()}: {str(e)}")


def main() -> None:
    """
    メイン関数
    実行中の全アプリケーションのスクリーンショットを取得し保存する
    """
    # スクリーンショットの設定
    config = ScreenshotConfig(
        file_format="png",
        save_dir=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "screenshots"
        ),
        exclude_menu_bar_apps=True,
    )

    # 実行中のアプリケーションを取得
    apps: List[NSRunningApplication] = get_running_apps()

    # 各アプリケーションを処理
    for app in apps:
        process_application(app, config)


if __name__ == "__main__":
    main()
