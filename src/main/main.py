import random
import os

WORDS_ESP = ['noche', 'débil', 'feliz', 'amigo', 'amada', 'odiar', 'llama', 'grano', 'flaco', 'fuego', 'viejo', 'lindo', 'santo', 'oro', 'noble', 'miedo', 'flora', 'felic', 'luz', 'poco', 'raro', 'mucho', 'clara', 'pulga', 'joven', 'amor', 'ruido', 'fuera', 'ducha', 'calor', 'guapa', 'dolor', 'arena', 'blusa', 'papel', 'bello', 'trino', 'guapo', 'huevo', 'tabla', 'mesa', 'mano', 'puño', 'puro', 'muro', 'casa', 'dado', 'rato', 'arco', 'boca', 'pico', 'pila', 'palo', 'cima', 'cama', 'arte', 'azul', 'taza', 'cien', 'color', 'gota', 'buho', 'burla', 'alma', 'alta', 'ancho', 'angel', 'agua', 'abuel', 'broma', 'bello', 'breve', 'bruma', 'barco', 'canal', 'cebra', 'cable', 'cama', 'campo', 'carga', 'carro', 'clavo', 'cruel', 'chico', 'cigar', 'causa', 'ducha', 'derec', 'danza', 'doble', 'drama', 'diosa', 'dulce', 'dolor', 'disco', 'doble', 'dolor', 'funda', 'fuera', 'furia', 'forma', 'freno', 'fuego', 'flama', 'grito', 'grupo', 'gente', 'grana', 'gusto', 'guard', 'guapo', 'herir', 'heroe', 'humor', 'hongo', 'igual', 'irrac', 'jabón', 'joven', 'jugar', 'juerg', 'luz', 'luz', 'lodo', 'largo', 'lucha', 'llena', 'llama', 'lenta', 'lunes', 'limón', 'loco', 'lugar', 'llano', 'mañana', 'manta', 'mundo', 'metal', 'mesa', 'mismo', 'morir', 'mover', 'muero', 'mucho', 'miedo', 'músic', 'mujer', 'múscu', 'manos', 'nadar', 'noche', 'naran', 'nuevo', 'nariz', 'nombre', 'never', 'nerio', 'orina', 'orgía', 'orden', 'oro', 'obvio', 'óptim', 'ollas', 'olvid', 'opaco', 'oport', 'onda', 'oído', 'pérdi', 'plata', 'perro', 'pinta', 'pocos', 'pulso', 'puño', 'quedo', 'queri', 'quita', 'quema', 'quiet', 'quiet', 'ruido', 'risas', 'sabor', 'salsa', 'salir', 'salón', 'salto', 'sapos', 'sobro', 'sollo', 'sobre', 'suero', 'sierra', 'tabla', 'techo', 'trato', 'tarde', 'truen', 'trino', 'tomo', 'torpe', 'tiene', 'telón', 'tinta', 'tipo', 'talón', 'vídeo', 'voces', 'volar', 'veloz', 'veces', 'vamos', 'vista', 'villa', 'valla', 'vital', 'vasto', 'verde', 'vista', 'volvi', 'valle', 'yerba', 'yerra', 'zorro', 'zamba', 'zanja', 'zapato', 'zigza']
WORDS_ENG = ['hello', 'goodbye', 'please', 'thank', 'you', 'good', 'morning', 'afternoon', 'evening', 'night', 'yes', 'no', 'maybe', 'perhaps', 'welcome', 'until', 'later', 'soon', 'tomorrow', 'how', 'are', 'what', 'your', 'name', 'my', 'nice', 'to', 'meet', 'delighted', 'sorry', 'pardon', 'happy', 'birthday', 'christmas', 'new', 'year', 'success', 'luck', 'health', 'money', 'love', 'peace', 'joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust', 'affection', 'friend', 'boyfriend', 'girlfriend', 'husband', 'wife', 'father', 'mother', 'son', 'daughter', 'brother', 'sister', 'grandfather', 'grandmother', 'uncle', 'aunt', 'cousin', 'nephew', 'niece', 'baby', 'child', 'teenager', 'adult', 'elderly', 'young', 'old', 'handsome', 'pretty', 'ugly', 'tall', 'short', 'fat', 'thin', 'skinny', 'blonde', 'brunette', 'redhead', 'black', 'white', 'gray', 'red', 'blue', 'green', 'yellow', 'orange', 'purple']



def main():

    os.system('cls || clear')

    game_over = False
    attempts = 6
    attempt = ""
    lang = ""

    while lang != 'ESP' and lang != 'ENG':
        lang = input("In which language u wanna play ? [ESP/ENG]\n")
        lang = lang.upper()

    word = random.choice(WORDS_ESP) if lang == 'ESP' else random.choice(WORDS_ENG)


    while attempts > 0:
        while len(attempt) != len(word):
            attempt = input("Say a word ({} letters)\n".format(len(word))) if lang == 'ENG' else input("Di una palabra ({} letras)\n".format(len(word)))
        if attempt.lower() == word.lower():
            print(check_word(attempt, word))
            print("Has ganado!")
            return
        else: 
            print(check_word(attempt, word) + "                 Lifes:" + str(attempts))
            attempt = ""
            attempts -= 1
        
    print("¡Has perdido! La palabra era:") if lang == "ESP" else print("You lost! The word was:")
    print(word)
    return 


def check_word(attempt: str, word: str) -> str:
    res = ""

    for i in range(len(word)):
        if attempt[i].lower() == word[i].lower():
            res += '🟩'
        elif attempt[i].lower() in word.lower():
            res += '🟨'
        else:
            res += "🟥"

    return res

    




if __name__ == '__main__':
    main()