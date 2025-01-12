# macos-screenshot

macOSで実行中の全アプリケーションのスクリーンショットを自動的に取得するユーティリティ。

## Features

- 実行中の全アプリケーションのスクリーンショットを自動取得
- 複数ウィンドウを持つアプリケーションに対応
- メニューバーアプリケーションの除外オプション
- PNG形式での保存

## Requirements

- macOS
- Python >= 3.11
- 以下のPythonパッケージ:
  - pyobjc-core
  - pyobjc-framework-Cocoa
  - pyobjc-framework-Quartz
  - Pillow
  - numpy

## Installation

```bash
pip install macos-screenshot
# or
uv sync
```

## Usage

```python
from macos_screenshot import main

# デフォルト設定で実行
main()
```
or
```sh
uv run -m src.main
```

設定をカスタマイズする場合：

```python
from macos_screenshot import ScreenshotConfig
from macos_screenshot import process_application, get_running_apps

config = ScreenshotConfig(
    file_format="png",
    save_dir="/path/to/save/directory",
    exclude_menu_bar_apps=True
)

# 実行中のアプリケーションを取得
apps = get_running_apps()

# 各アプリケーションを処理
for app in apps:
    process_application(app, config)
```

スクリーンショットは指定したディレクトリに`{アプリケーション名}_{ウィンドウ番号}.png`の形式で保存される。
