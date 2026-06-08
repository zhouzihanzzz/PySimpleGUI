import PySimpleGUI as sg

# 窗口布局
layout = [
    [sg.Text("简易记事本")],
    [sg.Multiline(size=(60, 20), key="-TEXT-")],
    [
        sg.Button("保存文件"),
        sg.Button("读取文件"),
        sg.Button("清空"),
        sg.Button("退出")
    ]
]

window = sg.Window("记事本", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "退出"):
        break
    if event == "清空":
        window["-TEXT-"].update("")
    elif event == "保存文件":
        path = sg.popup_get_file("保存文件", save_as=True, file_types=(("文本文件", "*.txt"),))
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(values["-TEXT-"])
            sg.popup("保存成功！")
    elif event == "读取文件":
        path = sg.popup_get_file("读取文件", file_types=(("文本文件", "*.txt"),))
        if path:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            window["-TEXT-"].update(content)

window.close()