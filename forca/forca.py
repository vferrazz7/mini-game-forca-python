import random

palavras = ['perfume', 'jacare', 'pato', 'lasanha', 'vinicius', 'madrid', 'familia', 'astronomia', 'oceanografia', 'viagem', 'literatura', 'culinaria', 'aventura', 
            'iphone', 'saude', 'tecnologia', 'sabonete', 'musica', 'esportes', 'cultura', 
            'amizade', 'moda', 'biologia', 'moda', 'filosofia', 'natureza', 'leao', 'elefante', 'girafa', 'tigre', 'gato', 'cachorro', 'papagaio', 'peixe', 'baleia',
            'tartaruga', 'abelha', 'panda', 'pinguim', 'golfinho', 'aguia', 'coruja', 'macaco', 
            'coelho', 'crocodilo', 'borboleta']

secreto = random.choice(palavras)
digitadas = []
chances = 5

print('-=' * 20)
print('JOGO DA FORCA')
print('-=' * 20)

while True:
    letra = str(input('Digite uma letra: '))

    if len(letra) != 1 or not letra.isalpha():
        print('Não trapaceie, apenas uma letra por vez!')
        continue

    if letra in digitadas:
        print('Você já digitou essa letra. Tente novamente.')
        continue

    digitadas.append(letra)

    if letra not in secreto:
        chances -= 1

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    print(f'A palavra secreta está assim: {secreto_temporario}')

    if secreto_temporario == secreto:
        print('Você venceu e escapou da forca')
        break

    if chances <= 0:
        print('Você perdeu! FORCA!!!')
        break

    print(f'Você tem {chances} chances...')
    print()