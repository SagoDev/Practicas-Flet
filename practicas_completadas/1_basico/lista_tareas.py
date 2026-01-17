"""
Flet
4º ejercicio practico: Lista de tareas basica
Implementar una lista dinámica para agregar y eliminar elementos.
"""

import flet as ft


def main(page: ft.Page):
    """Main app"""

    page.title = "Lista de Tareas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def agregar_tarea():
        """Agrega una tarea a la tabla"""
        btn_eliminar_tarea = ft.FilledButton(
            content="Eliminar",
            icon=ft.Icons.DELETE,
            bgcolor=ft.Colors.RED,
            on_click=eliminar_tarea,
        )

        tarea = ft.DataRow(
            cells=[
                ft.DataCell(content=ft.Text(value=tarea_nombre.value)),
                ft.DataCell(content=ft.Text(value=descripcion.value)),
                ft.DataCell(content=ft.Text(value=fecha.value)),
                ft.DataCell(
                    content=ft.Text(value=estado.value if estado.value else "Pendiente")
                ),
                ft.DataCell(content=btn_eliminar_tarea),
            ]
        )

        btn_eliminar_tarea.data = tarea

        tabla_de_tareas.rows.append(tarea)
        page.update()

    def eliminar_tarea(e):
        """Elimina una tarea de la tabla"""
        tarea_row = e.control.data
        tabla_de_tareas.rows.remove(tarea_row)
        page.update()

    divisor_vertical = ft.VerticalDivider(color=ft.Colors.BLUE_900, col=1)
    divisor_horizontal = ft.Divider(color=ft.Colors.BLUE_900)

    encabezado = ft.Container(
        content=ft.Row(
            controls=[ft.Text(value="Lista de Tareas", size=45)],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    tarea_nombre = ft.TextField(
        label="Tarea",
        hint_text="Ingresa el nombre de la tarea",
    )
    descripcion = ft.TextField(
        label="Descripción",
        hint_text="Agrega una descripción",
    )
    fecha = ft.TextField(
        label="Fecha",
        hint_text="Ingresa fecha limite",
    )
    estado = ft.Dropdown(
        label="Estado",
        options=[
            ft.DropdownOption(key="Pendiente"),
            ft.DropdownOption(key="En progreso"),
            ft.DropdownOption(key="Completado"),
        ],
    )
    btn_agregar = ft.FilledButton(
        content="Agregar Tarea", bgcolor=ft.Colors.BLUE_900, on_click=agregar_tarea
    )

    formulario_tarea = ft.Container(
        col=3,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="Agregar Tarea", size=30),
                tarea_nombre,
                descripcion,
                fecha,
                estado,
                btn_agregar,
            ],
        ),
    )

    tabla_de_tareas = ft.DataTable(
        col=8,
        horizontal_lines=ft.BorderSide(),
        columns=[
            ft.DataColumn(label="Tarea"),
            ft.DataColumn(label="Descripción"),
            ft.DataColumn(label="Fecha Limite"),
            ft.DataColumn(label="Estado"),
            ft.DataColumn(label=""),
        ],
        rows=[],
    )

    principal = ft.Container(
        expand=True,
        content=ft.ResponsiveRow(
            controls=[
                formulario_tarea,
                divisor_vertical,
                tabla_de_tareas,
            ]
        ),
    )

    pie_de_pagina = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(value="Plan de Ejercicios.", size=15),
                ft.Text(value="Básico.", size=15),
                ft.Text(value="Flet.", size=15),
                ft.Text(value="SagoDev.", size=15),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    contenedor_principal = ft.Container(
        expand=True,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                encabezado,
                divisor_horizontal,
                principal,
                divisor_horizontal,
                pie_de_pagina,
            ],
        ),
    )

    page.add(contenedor_principal)


ft.run(main)
