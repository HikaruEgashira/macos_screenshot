# macos-utils

## 1. window_capture

macOSで実行中の全アプリケーションのスクリーンショットを自動的に取得するユーティリティ。

```sh
uv run -m src.capture_all_apps
```

スクリーンショットは`./out/screenshots/`に`{アプリケーション名}_{ウィンドウ番号}.png`の形式で保存される。

## 2. window_structure

macOS Accessibility APIで表現されるウィンドウ構造を取得するユーティリティ。

```sh
uv run -m src.window_structure
```
