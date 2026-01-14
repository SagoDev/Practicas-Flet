"""
Flet
1º ejercicio práctico: Contador interactivo
Crear una app con texto y botones para incrementar/decrementar un valor usando estado.
"""

import flet as ft


def main(page: ft.Page):
    """Main app."""

    # Titulo de la pagina
    page.title = "Contador Interactivo"

    # Alineación de los elementos dentro de la pagina
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Color de tema de la pagina
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREY_50)

    # Titulo del ejercicio
    ejercicio_titulo = ft.Text(value="Contador interactivo", size=50)

    # Contador
    contador = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=100,
        bgcolor=ft.Colors.ON_SECONDARY_CONTAINER,
        color=ft.Colors.BLACK,
    )

    # Pie de pagina
    pie_de_pagina = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(value="Desarrollado por SagoDev."),
            ft.Text(value="Plan de Ejercicios."),
            ft.Text(value="Flet."),
            ft.Text(value="Básico."),
        ],
    )

    # Funciones sumar/restar
    def sumar():
        """Suma 1 al valor del counter."""
        contador.value = str(int(contador.value) + 1)

    def restar():
        """Resta 1 al valor del counter."""
        contador.value = str(int(contador.value) - 1)

    # Contador interactivo contador + funciones
    contador_interactivo = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
        controls=[
            ft.IconButton(
                ft.Icons.REMOVE,
                on_click=restar,
                bgcolor=ft.Colors.ON_SECONDARY_CONTAINER,
                icon_color=ft.Colors.BLACK,
            ),
            contador,
            ft.IconButton(
                ft.Icons.ADD,
                icon_color=ft.Colors.BLACK,
                on_click=sumar,
                bgcolor=ft.Colors.ON_SECONDARY_CONTAINER,
            ),
        ],
    )

    # Pagina principal
    page.add(
        # titulo
        ejercicio_titulo,
        # contador
        contador_interactivo,
        # piede de pagina
        pie_de_pagina,
    )


ft.run(main)
