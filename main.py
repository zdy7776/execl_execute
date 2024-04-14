import os
import shutil

import flet as ft
from datetime import datetime
from file_reader import read_execl
from file_writer import write_execl

cache_file_path = ["./caches/input.xlsx"]

def get_now_time():
    now = datetime.now()
    current_time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time_string + ": "


def main(page: ft.Page):
    page.title = "征信监管辅助系统"
    page.theme_mode = "light"
    show_message = ft.Column()
    # page.horizontal_alignment = page.vertical_alignment = "center"

    page.window_width, page.window_height = 1300, 765
    page.window_center()
    page.window_visible = True
    page.on_error = lambda e: print("Error: ", e.data)

    page.appbar = ft.AppBar(
        title=ft.Text("征信监管辅助系统", color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.BLUE,
        elevation=5
    )

    def pick_files_result(e: ft.FilePickerResultEvent):
        alert_message = ""
        index = 0
        if e.files:
            for file in e.files:
                print(file.path)
                if not file.name.split(".")[-1].startswith("xls"):
                    alert_message = get_now_time() + "导入的文件只能是xlsx/xls格式!"
                    index = 1
                    break
                else:
                    os.makedirs("./caches", exist_ok=True)
                    # 复制文件到目标目录
                    shutil.copy(file.path, "./caches")
                    cache_file_path.append("./caches/{}".format(file.name))
        if index == 0:
            alert_message = get_now_time() + ", ".join(
                map(lambda f: f.name, e.files)) + " 导入成功！" if e.files else "取消导入!"

        show_message.controls.append(ft.Text(alert_message))
        show_message.controls.append(ft.Text(get_now_time() + read_file(cache_file_path)))
        page.update()

    def read_file(file_paths):
        df_str = read_execl(file_paths[-1])
        return df_str

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Column([ft.Row(
            [
                ft.ElevatedButton(
                    "选择文件",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
            ]
        ),
            ft.Row(
                [
                    ft.ElevatedButton(
                        "读取文件",
                        icon=ft.icons.READ_MORE,
                        # on_click=read_file(cache_file_path)
                    ),
                ]
            ),
            ft.Row(
                [
                    ft.ElevatedButton(
                        "清除文件",

                        icon=ft.icons.REMOVE_DONE,
                        # on_click=lambda _: pick_files_dialog.pick_files(
                        #     allow_multiple=True
                        # ),
                    ),
                ]
            ), ft.Row(
                [
                    ft.ElevatedButton(
                        "删除文件",
                        icon=ft.icons.DELETE,
                        # on_click=lambda _: pick_files_dialog.pick_files(
                        #     allow_multiple=True
                        # ),
                    ),
                ]
            ),
            ft.Divider(height=50, color="white"),
            ft.Divider(height=9, thickness=3),
            ft.Text("工作日志", color=ft.colors.BLUE, size=25),
            show_message])

    )


ft.app(main)
