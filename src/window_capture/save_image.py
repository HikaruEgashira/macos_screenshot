import os
from PIL import Image
import numpy as np
from ..stubs.Quartz import (
    CGImageRef,
    CGImageGetWidth,
    CGImageGetHeight,
    CGImageGetBytesPerRow,
    CGImageGetDataProvider,
    CGDataProviderCopyData,
)
from .schema import ScreenshotConfig


def save_screenshot(
    image: CGImageRef, app_name: str, config: ScreenshotConfig = ScreenshotConfig()
) -> None:
    """
    スクリーンショットを指定された形式で保存する。

    Args:
        image (CGImageRef): スクリーンショット
        app_name (str): アプリケーション名
        config (ScreenshotConfig): スクリーンショットの設定
    """
    # 保存先ディレクトリが存在しない場合は作成
    os.makedirs(config.save_dir, exist_ok=True)

    # CGImageの情報を取得
    width = CGImageGetWidth(image)
    height = CGImageGetHeight(image)
    bytes_per_row = CGImageGetBytesPerRow(image)

    # CGImageのデータプロバイダを取得
    data_provider = CGImageGetDataProvider(image)
    data = CGDataProviderCopyData(data_provider)

    # バイトデータをnumpy配列に変換
    buffer = np.frombuffer(data, dtype=np.uint8)

    # 正しいshapeに変換
    array = buffer.reshape(height, bytes_per_row // 4, 4)
    if array.shape[1] > width:
        array = array[:, :width]

    # RGBA -> RGB変換
    rgb_array = array[:, :, :3]

    # numpy配列からPIL Imageを作成
    pil_image = Image.fromarray(rgb_array)

    # ファイルパスを生成して保存
    file_path = os.path.join(
        config.save_dir, f"{app_name}.{config.file_format.lower()}"
    )
    pil_image.save(file_path)
