import os
import logging
from typing import List

from .utils.app_list import get_running_apps
from .stubs.AppKit import NSRunningApplication
from .window_capture import (
    get_window_bounds,
    capture_window,
    save_window,
    WindowCaptureConfig,
)

logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(asctime)s - %(name)s - [%(levelname)s] %(message)s",
)
logger: logging.Logger = logging.getLogger(__name__)


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
                logger.debug(
                    f"Skipping {app_name} (Bundle ID: {bundle_id}) - not in whitelist"
                )
                return
        elif config.filter_mode == "blacklist":
            if bundle_id in config.blocked_apps:
                logger.debug(
                    f"Skipping {app_name} (Bundle ID: {bundle_id}) - in blacklist"
                )
                return

        # ウィンドウ情報を取得
        windows = get_window_bounds(app, config)
        logger.debug(
            f"Found {len(windows)} windows for {app_name} (Bundle ID: {bundle_id})"
        )

        # 各ウィンドウをキャプチャ
        for i, window in enumerate(windows):
            try:
                # ウィンドウをキャプチャ
                image = capture_window(window)
                if image:
                    # ウィンドウキャプチャを保存
                    save_window(image, f"{app_name}_{i}", config)
                    logger.info(f"Captured: {app_name} (Window {i + 1})")
                    logger.debug(
                        f"Detail: Bundle ID: {bundle_id}, Window bounds: {window}"
                    )
            except Exception as e:
                logger.error(
                    f"Error capturing window {i + 1} of {app_name}: {str(e)}",
                    exc_info=True,
                )
    except Exception as e:
        logger.error(f"Error processing {app.localizedName()}: {str(e)}", exc_info=True)


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

    logger.info("Starting window capture process")
    logger.debug(f"Configuration: {config}")

    # 実行中のアプリケーションを取得
    apps: List[NSRunningApplication] = get_running_apps()
    logger.debug(f"Found {len(apps)} running applications")

    # 各アプリケーションを処理
    for app in apps:
        process_application(app, config)

    logger.info("Window capture process completed")


if __name__ == "__main__":
    main()
