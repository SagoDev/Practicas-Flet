"""
Flet
3º ejercicio practico: Landing page personal
Construir una landing estática con encabezado, descripción, botones y layout básico.
"""

import flet as ft


def main(page: ft.Page):
    """Main App"""
    # Titulo de la pagina
    page.title = "Formulario de contacto"

    # Alineación de los elementos dentro de la pagina
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Color de fondo de la pagina
    page.theme_mode = ft.ThemeMode.LIGHT

    # Pie de pagina
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

    # Encabezado
    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    value="AutomatIA",
                    color=ft.Colors.BLUE_900,
                    size=25,
                    weight=ft.FontWeight.BOLD,
                )
            ]
        )
    )

    # Contenido Principal
    marca = ft.Text(
        value="AutomatIA",
        color=ft.Colors.BLUE_900,
        size=100,
    )
    texto_principal = ft.Text(
        value="Automatiza tu negocio.", color=ft.Colors.BLACK, size=40
    )
    texto_secundario_1 = ft.Text(
        value="Liberate de procesos aburridos y costosos. Recupera tu tiempo.",
        color=ft.Colors.BLACK,
        size=20,
    )
    texto_secundario_2 = ft.Text(
        value="Registrate ahora y asegura tu compra", color=ft.Colors.BLACK
    )
    registrarse = ft.TextField(hint_text="Ingresa tu email")
    divisor = ft.Divider(color=ft.Colors.BLUE_900)

    caja_de_textos = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(content=marca, align=ft.Alignment.CENTER),
                ft.Container(content=texto_principal, align=ft.Alignment.CENTER),
                ft.Container(content=texto_secundario_1, align=ft.Alignment.CENTER),
                ft.Container(content=texto_secundario_2, align=ft.Alignment.CENTER),
                ft.Container(content=registrarse, align=ft.Alignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        col=6,
        align=ft.Alignment.CENTER,
    )
    caja_de_imagen = ft.Container(
        content=ft.ShaderMask(
            content=ft.Image(
                src="https://penneo.com/wp-content/uploads/2021/02/benefits-business-process-automation.png",
                fit=ft.BoxFit.FILL,
            ),
            blend_mode=ft.BlendMode.MULTIPLY,
            shader=ft.RadialGradient(
                center=ft.Alignment.CENTER,
                radius=2.0,
                colors=[ft.Colors.WHITE, ft.Colors.BLUE_900],
                tile_mode=ft.GradientTileMode.CLAMP,
            ),
        ),
        border_radius=500,
        col=6,
        align=ft.Alignment.CENTER,
    )

    contenido_principal = ft.Container(
        expand=True,
        content=ft.ResponsiveRow(
            controls=[caja_de_textos, caja_de_imagen],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
        ),
    )

    contenedor_general = ft.Container(
        content=ft.Column(
            controls=[
                encabezado,
                divisor,
                contenido_principal,
                divisor,
                pie_de_pagina,
            ]
        ),
        expand=True,
    )

    page.add(contenedor_general)


ft.run(main)
