import random
import sys
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3) # Modifico el "choices" por el "sample" para que no se repitan las preguntas
puntos = 0 #Para sumar los  puntos
# El usuario deberá contestar 3 preguntas
for ques, ans, corrans in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(ques)
    for i, answer in enumerate(ans):
        print(f"{i + 1}. {answer}")
    cont = 0 #Cuento intentos
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        cont += 1
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es válida
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if (user_answer < 5) and (user_answer > 0):
                # Se verifica si la respuesta es correcta
                if (user_answer - 1) == corrans:
                    print("¡Correcto!")
                    puntos += 1
                    print ("Tu puntaje parcial es de: ", puntos)
                    break
                else:
                # Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
                    if cont == 1:
                        puntos -= 0.5
            else:
                print("Respuesta no válida.")
                sys.exit(1)
        else:
            print("Respuesta no válida.")
            sys.exit(1)
    else:   
        print("Incorrecto. La respuesta correcta es:")
        print(corrans + 1)
        puntos -= 0.5
        print ("Tu puntaje parcial es de: ", puntos)
    # Se imprime un blanco al final de la pregunta
print()
print ("Tu puntaje final es de: ", puntos)