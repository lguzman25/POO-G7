import qrcode
from qrcode import constants
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from PIL import Image

class GeneradorQR:
    def __init__(self):
        self.version = 1
        self.error_correction = constants.ERROR_CORRECT_M
        self.box_size = 10
        self.border = 4
        self.data = ""

    def configurar_tamano(self):
        print("\nConfiguración de tamaño:")
        print("1. Pequeño (21x21)")
        print("2. Mediano (25x25)")
        print("3. Grande (29x29)")
        opcion = input("Seleccione el tamaño (1-3): ")
        if opcion == "1":
            self.version = 1
            self.box_size = 10
        elif opcion == "2":
            self.version = 3
            self.box_size = 12
        elif opcion == "3":
            self.version = 5
            self.box_size = 15

    def configurar_correccion_error(self):
        print("\nNivel de corrección de error:")
        print("1. Bajo (7% de recuperación)")
        print("2. Medio (15% de recuperación)")
        print("3. Alto (25% de recuperación)")
        print("4. Máximo (30% de recuperación)")
        opcion = input("Seleccione el nivel (1-4): ")
        if opcion == "1":
            self.error_correction = constants.ERROR_CORRECT_L
        elif opcion == "2":
            self.error_correction = constants.ERROR_CORRECT_M
        elif opcion == "3":
            self.error_correction = constants.ERROR_CORRECT_Q
        elif opcion == "4":
            self.error_correction = constants.ERROR_CORRECT_H

    def configurar_borde(self):
        self.border = int(input("\nIngrese el tamaño del borde (2-10): "))
        
    def seleccionar_estilo(self):
        print("\nEstilos disponibles:")
        print("1. Cuadrados (clásico)")
        print("2. Círculos")
        print("3. Bordes redondeados")
        opcion = input("Seleccione el estilo (1-3): ")
        if opcion == "1":
            return SquareModuleDrawer()
        elif opcion == "2":
            return CircleModuleDrawer()
        elif opcion == "3":
            return RoundedModuleDrawer()
        return SquareModuleDrawer()

    def crear_qr(self, nombre_archivo, fill_color="black", back_color="white", estilo=None):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border
        )
        
        qr.add_data(self.data)
        qr.make(fit=True)
        
        if estilo:
            imagen_qr = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=estilo,
                fill_color=fill_color,
                back_color=back_color
            )
        else:
            imagen_qr = qr.make_image(
                fill_color=fill_color,
                back_color=back_color
            )

        if not nombre_archivo.endswith('.png'):
            nombre_archivo += '.png'
        
        imagen_qr.save(nombre_archivo)
        print(f"\nCódigo QR generado como '{nombre_archivo}'")

def mostrar_menu():
    print("\n=== GENERADOR DE CÓDIGOS QR ===")
    print("1. QR básico (blanco y negro)")
    print("2. QR con colores personalizados")
    print("3. QR con estilo personalizado")
    print("4. Salir")

def main():
    generador = GeneradorQR()
    
    while True:
        mostrar_menu()
        opcion = input("\nElija una opción (1-4): ")
        
        if opcion in ["1", "2", "3"]:
            generador.data = input("\nIngrese el texto para el código QR: ")
            nombre = input("Ingrese el nombre para guardar el archivo: ")
            
            # Configuraciones generales
            generador.configurar_tamano()
            generador.configurar_correccion_error()
            generador.configurar_borde()
            
            if opcion == "1":
                generador.crear_qr(nombre)
                
            elif opcion == "2":
                color_modulos = input("Color para los módulos (ej: blue, red, #FF0000): ")
                color_fondo = input("Color para el fondo (ej: white, yellow, #FFFFFF): ")
                generador.crear_qr(nombre, fill_color=color_modulos, back_color=color_fondo)
                
            elif opcion == "3":
                color_modulos = input("Color para los módulos (ej: blue, red, #FF0000): ")
                color_fondo = input("Color para el fondo (ej: white, yellow, #FFFFFF): ")
                estilo = generador.seleccionar_estilo()
                generador.crear_qr(nombre, fill_color=color_modulos, back_color=color_fondo, estilo=estilo)
        
        elif opcion == "4":
            print("\nPrograma finalizado")
            break
            
        else:
            print("\nOpción no válida. Intente nuevamente")

if __name__ == "__main__":
    main()