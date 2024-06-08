from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def guardar_receta():
    # Obtener los datos ingresados por el usuario
    direccion = entry_direccion.get()
    paciente = entry_paciente.get()
    diagnostico = entry_diagnostico.get()
    medicamentos = entry_medicamentos.get("1.0", "end-1c")
    edad = entry_edad.get()

    # Cargar la plantilla (imagen existente)
    template_path = "recetario_template.jpg"
    template = Image.open(template_path)

    # Crear un objeto ImageDraw para dibujar sobre la imagen
    draw = ImageDraw.Draw(template)

    # Cargar una fuente (puedes usar una fuente TrueType o una fuente de sistema)
    font_path = "arial.ttf"  # Ruta a la fuente (por ejemplo, Arial)
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)

    # Coordenadas para el texto (ajústalas según la plantilla)
    x_direccion, y_direccion = 50, 252
    x_paciente, y_paciente = 130, 222
    x_diagnostico, y_diagnostico = 50, 342
    x_medicamentos, y_medicamentos = 100, 480
    x_edad, y_edad = 394, 310
    # ... Ajusta las coordenadas para otros campos ...

    # Agregar texto a la imagen
    draw.text((x_direccion, y_direccion), f"Direccion: {direccion}", font=font, fill="black")
    draw.text((x_paciente, y_paciente), f"Paciente: {paciente}", font=font, fill="black")
    draw.text((x_diagnostico, y_diagnostico), f"diagnóstico: {diagnostico}", font=font, fill="black")
    draw.text((x_medicamentos, y_medicamentos),f"medicamentos: {medicamentos}",font=font, fill="black")
    draw.text((x_edad, y_edad),f"edad:{edad}", font=font, fill="black")
    # ... Agrega más campos de texto ...

    # Guardar la imagen superpuesta
    template.save("receta_superpuesta.jpg")

    # Crear un archivo PDF
    pdf_filename = "receta_medica.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(100, 700, f"Direccion: {direccion}")
    c.drawString(100, 680, f"Paciente: {paciente}")
    c.drawString(100, 660, f"Diagnóstico: {diagnostico}")
    c.drawString(100, 640, f"Medicamentos: {medicamentos}")
    c.drawString(100, 620, f"edad: {edad}")
    c.save()

    # Mostrar mensaje de confirmación
    messagebox.showinfo("Receta guardada", f"La receta se ha guardado en {pdf_filename}")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Recetas Médicas")

# Agregar campos de entrada
entry_direccion = tk.Entry(root, width=40)
entry_paciente = tk.Entry(root, width=40)
entry_diagnostico = tk.Entry(root, width=40)
entry_medicamentos = tk.Text(root, width=40, height=12)  # Ajusta el alto según tus necesidades
entry_edad = tk.Entry(root, width=40)

# Agregar botón para guardar la receta
boton_guardar = tk.Button(root, text="Guardar Receta", command=guardar_receta)

# Posicionar elementos en la ventana
tk.Label(root, text="Direccion:").pack()
entry_direccion.pack()
tk.Label(root, text="Paciente:").pack()
entry_paciente.pack()
tk.Label(root, text="Diagnóstico:").pack()
entry_diagnostico.pack()
tk.Label(root, text="Medicamentos (uno por línea):").pack()
entry_medicamentos.pack()
tk.Label(root, text="Edad:").pack()
entry_edad.pack()
boton_guardar.pack()

root.mainloop()
