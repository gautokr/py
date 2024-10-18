def points_comments():
    while True:
                print("Por favor, ingrese una calificación del 1 al 5.")
                point = input()

                if point.isdecimal():
                    point = int(point)
                    if point <= 0 or point > 5:
                        print('El número debe ser del 1 al 5.')
                    else:
                        print('Ingrese un comentario:')
                        comment = input()
                        post = f'puntuación: {point} comentario: {comment}'
                        with open('data.txt', 'a') as archivo_txt:
                            archivo_txt.write(f'{post} \n')
                        break
                else:
                    print('Por favor, introduzca un número.')

def resultados_hoy():
    print('Resultados hasta la fecha.')
    with open('data.txt', 'r') as archivo_txt:
        print(archivo_txt.read())
          
while True:
    print('Seleccione una opción')
    print('1. Ingresar puntuación y comentarios')
    print('2. Revisar resultados obtenidos hasta ahora')
    print('3. Salir')

    valor = input()
    
    if valor.isdecimal():
        valor = int(valor)
        if valor == 1:
            points_comments()
        elif valor == 2:
            resultados_hoy()
        elif valor == 3:
            print('Hasta luego.')
            break
        
        else:
            print('Introduzca un número del 1 al 3')
            
    else:
                    print('Introduzca un número del 1 al 3')

            
