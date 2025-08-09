import flet as ft

def main(page: ft.Page):
    tasks = []

    def delete_task(e):
        task_to_delete = e.control.data
        tasks.remove(task_to_delete)
        page.controls.remove(task_to_delete)
        page.update()

    def add_task(e):
        task_text = task_input.value
        if task_text.strip() == "":
            return

        # عنصر المهمة
        task_row = ft.Row(
            controls=[
                ft.Text(task_text),
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    tooltip="حذف",
                    on_click=delete_task,
                    data=None  # هنحط العنصر نفسه بعدين
                )
            ]
        )

        # نحفظ العنصر داخل نفسه علشان نقدر نحذفه بعدين
        task_row.controls[1].data = task_row

        tasks.append(task_row)
        page.controls.append(task_row)
        task_input.value = ""
        page.update()

    # إدخال المهمة الجديدة
    task_input = ft.TextField(label="أدخل مهمة جديدة", autofocus=True)

    # زرار إضافة المهمة
    add_button = ft.ElevatedButton(text="أضف", on_click=add_task)

    # إضافة عناصر الواجهة
    page.add(
        ft.Row([task_input, add_button])
    )

ft.app(target=main)
