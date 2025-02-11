from .window_info import get_all_window_info


def format_xml(value: str) -> str:
    """XMLエスケープを行う"""
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def print_window_xml(window, indent="  "):
    """ウィンドウ情報をXML形式で出力する"""
    print(f'{indent}<window title="{format_xml(window.title or "")}">')

    if window.position:
        print(f'{indent}  <position x="{window.position.x}" y="{window.position.y}" />')

    if window.size:
        print(
            f'{indent}  <size width="{window.size.width}" height="{window.size.height}" />'
        )

    if window.role:
        print(f"{indent}  <role>{format_xml(window.role)}</role>")

    if window.subrole:
        print(f"{indent}  <subrole>{format_xml(window.subrole)}</subrole>")

    if window.description:
        print(f"{indent}  <description>{format_xml(window.description)}</description>")

    print(f"{indent}  <enabled>{str(window.enabled).lower()}</enabled>")

    if window.value:
        print(f"{indent}  <value>{format_xml(window.value)}</value>")

    if window.children:
        print(f"{indent}  <children>")
        for child in window.children:
            print(f"{indent}    <child>")
            for key, value in child.items():
                if value is not None:
                    print(f"{indent}      <{key}>{format_xml(str(value))}</{key}>")
            print(f"{indent}    </child>")
        print(f"{indent}  </children>")

    print(f"{indent}</window>")


def main():
    """メイン関数"""
    try:
        window_info_list = get_all_window_info()

        print("<applications>")

        # 結果の出力
        for app_info in window_info_list:
            print(
                f'  <application name="{format_xml(app_info.app_name)}" pid="{app_info.pid}">'
            )
            for window in app_info.windows:
                print_window_xml(window, indent="    ")
            print("  </application>")

        print("</applications>")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
