"""
Flet
2º ejercicio practico: Formulario de contacto
Diseñar un formulario con inputs y un botón que capture y muestre la información ingresada.
"""

import flet as ft

# Variables de color
gris_50 = ft.Colors.GREY_50
negro = ft.Colors.BLACK
secundario = ft.Colors.ON_SECONDARY_CONTAINER


def main(page: ft.Page):
    """Main App."""

    # Titulo de la pagina
    page.title = "Formulario de contacto"

    # Alineación de los elementos dentro de la pagina
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Color de fondo de la pagina
    page.bgcolor = gris_50
    # Titulo del ejercicio
    ejercicio_titulo = ft.Text(value="Formulario De Contacto", size=50)

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

    # Funciones
    def agregar_contacto():
        """agrega un contacto a la lista"""
        contacto = ft.DataRow(
            cells=[
                ft.DataCell(content=ft.Text(value=nombre.value)),
                ft.DataCell(content=ft.Text(value=apellido.value)),
                ft.DataCell(content=ft.Text(value=telefono.value)),
            ]
        )
        tabla_de_contactos.rows.append(contacto)
        page.update()

    # Lista de contactos
    titulo_lista = ft.Text(value="Lista de Contactos", size=30)
    tabla_de_contactos = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text(value="Nombre")),
            ft.DataColumn(label=ft.Text(value="Apellido")),
            ft.DataColumn(label=ft.Text(value="Telefono")),
        ],
        rows=[],
    )

    lista_de_contactos = ft.Container(
        alignment=ft.Alignment.TOP_CENTER,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                titulo_lista,
                tabla_de_contactos,
            ],
        ),
    )

    # Formulario agregar contacto
    titulo_formulario = ft.Text(value="Agregar Contacto", size=30)
    nombre = ft.TextField(
        label="Nombre",
        hint_text="Ingrese el nombre",
    )
    apellido = ft.TextField(
        label="Apellido",
        hint_text="Ingrese el apellido",
    )
    telefono = ft.TextField(
        label="Teléfono",
        hint_text="Ingrese el numero",
    )
    btn_agregar = ft.Button(content="Agregar", on_click=agregar_contacto)
    formulario_agregar = ft.Container(
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                titulo_formulario,
                nombre,
                apellido,
                telefono,
                btn_agregar,
            ],
        ),
    )

    # tabs para navegar entre acciones
    tabs = ft.Tabs(
        selected_index=0,
        length=2,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(label="Agregar contacto"),
                        ft.Tab(label="Ver contactos"),
                    ]
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        ft.Container(
                            content=formulario_agregar,
                            alignment=ft.Alignment.CENTER,
                            padding=20,
                        ),
                        ft.Container(
                            content=lista_de_contactos,
                            alignment=ft.Alignment.CENTER,
                            padding=20,
                        ),
                    ],
                ),
            ],
        ),
    )

    # Pagina principal
    page.add(
        # titulo
        ejercicio_titulo,
        # tabs
        tabs,
        # piede de pagina
        pie_de_pagina,
    )


ft.run(main)
