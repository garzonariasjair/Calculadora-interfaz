import tkinter as tk

class MiCalculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi Calculadora")
        self.ventana.geometry("320x400")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="#eeeeee")

        self.entrada = tk.Entry(
            ventana,
            font=("Arial", 20),
            justify="right",
            bd=5
        )
        self.entrada.pack(fill="x", padx=12, pady=15, ipady=8)

        botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", ".", "+"]
        ]

        marco = tk.Frame(ventana, bg="#eeeeee")
        marco.pack()

        for fila, valores in enumerate(botones):
            for columna, texto in enumerate(valores):
                boton = tk.Button(
                    marco,
                    text=texto,
                    font=("Arial", 13),
                    width=6,
                    height=2,
                    command=lambda x=texto: self.presionar(x)
                )
                boton.grid(row=fila, column=columna, padx=3, pady=4)

        tk.Button(
            ventana,
            text="⌫",
            font=("Arial", 12),
            width=12,
            command=self.eliminar
        ).pack(pady=3)

        tk.Button(
            ventana,
            text="=",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.resolver
        ).pack(pady=5)

    def presionar(self, valor):
        if valor == "C":
            self.limpiar()
        else:
            self.entrada.insert(tk.END, valor)

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def eliminar(self):
        contenido = self.entrada.get()
        self.limpiar()
        self.entrada.insert(0, contenido[:-1])

    def resolver(self):
        try:
            operacion = self.entrada.get()

            if "+" in operacion:
                numeros = operacion.split("+")
                resultado = float(numeros[0]) + float(numeros[1])

            elif "-" in operacion:
                numeros = operacion.split("-")
                resultado = float(numeros[0]) - float(numeros[1])

            elif "*" in operacion:
                numeros = operacion.split("*")
                resultado = float(numeros[0]) * float(numeros[1])

            elif "/" in operacion:
                numeros = operacion.split("/")
                if float(numeros[1]) == 0:
                    raise ZeroDivisionError
                resultado = float(numeros[0]) / float(numeros[1])

            else:
                resultado = float(operacion)

            self.limpiar()
            self.entrada.insert(0, str(resultado))

        except ZeroDivisionError:
            self.limpiar()
            self.entrada.insert(0, "No se puede dividir por 0")

        except Exception:
            self.limpiar()
            self.entrada.insert(0, "Error")


ventana = tk.Tk()
app = MiCalculadora(ventana)
ventana.mainloop()