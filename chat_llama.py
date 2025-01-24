import flet as ft
import llama 
import pyperclip


def main(page: ft.Page):
    page.title = "Teacher_Ollama 3.2"

    # función para copiar la respuesta de ollama
    def copiar(e, text):
        pyperclip.copy(text)


        # Función para enviar el mensaje
    def send_message(e):
        if message_input.value:
            prompt = message_input.value

            chat.controls.append(
                ft.Row(controls=[ft.TextField(label="You", value=message_input.value, bgcolor=ft.colors.GREEN, width=500, multiline=True, read_only=True, text_align="right")], expand=11)
            )
            message_input.value = ""  # Limpiar el campo de entrada
            page.update()

# traer el historial del modelo y llamarlo
            history = llama.history
            response = llama.ask_to_llama(prompt)
            
            
            ollama_textfield = ft.TextField(value=response, width=1000, read_only=True, label="Llama response", autofocus=True, multiline=True, bgcolor=ft.colors.BLUE)
            pmb = ft.PopupMenuButton(
                items=[            ft.PopupMenuItem(icon=ft.icons.COPY, text="Coppy", on_click=copiar(e, response))])
            chat.controls.append(ft.Row(controls=[ollama_textfield, pmb]))
            page.update()

    



    chat = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True, divider_thickness=5)

    # Campo de entrada de texto para el mensaje
    message_input = ft.TextField(hint_text="Ask me anything...", width=1200, autofocus=True, expand=True, cursor_color=ft.colors.RED,
            selection_color=ft.colors.YELLOW,             filled=True, focused_bgcolor=ft.colors.BLUE_400, adaptive=True, multiline=True, shift_enter=True)

    # Botón para enviar el mensaje
    send_button = ft.IconButton(icon=ft.icons.SEND, on_click=send_message, icon_color="blue", icon_size=20, tooltip="Send", adaptive=True)

    # Contenedor para el campo de entrada y el botón
    input_row = ft.Row(
        controls=[message_input, send_button],
        alignment="start",
        spacing=10,
    )

    # Contenedor principal que mantiene el área de chat y el contenedor de entrada
    main_column = ft.Column(
        controls=[chat,input_row],
        alignment="end",  # Coloca los controles al final (parte inferior)
        expand=True,  # Expande el contenedor para ocupar todo el espacio posible en la página
    )

    # Añadir el contenedor principal a la página
    page.add(main_column)

ft.app(target=main)
