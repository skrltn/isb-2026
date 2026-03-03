from files1 import ALPHABET, INPUT_FILE, ENCRYPTED_FILE, KEY_FILE, CHECK_FILE

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

print('Исходный текст прочитан из файла: ' + INPUT_FILE)
print('Длина текста: ' + str(len(text)) + ' символов')
print('Первые 100 символов:')
print(text[:100] + '...')
print()

shift = 9
print('Выбран сдвиг: ' + str(shift) + ' (вправо)')

def encrypt(text: str, shift: int) -> str:
    """
    Шифрует текст методом Цезаря.
    
    Args:
        text: Исходный текст для шифрования
        shift: Величина сдвига (положительное число для сдвига вправо)
    
    Returns:
        Зашифрованный текст
    """
    encrypted = ''
    for char in text:
        if char in ALPHABET:
            pos = ALPHABET.index(char)
            new_pos = (pos + shift) % len(ALPHABET)
            encrypted += ALPHABET[new_pos]
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_text: str, shift: int) -> str:
    """
    Дешифрует текст, зашифрованный методом Цезаря.
    
    Args:
        encrypted_text: Зашифрованный текст
        shift: Величина сдвига, использованная при шифровании
    
    Returns:
        Расшифрованный текст
    """
    decrypted = ''
    for char in encrypted_text:
        if char in ALPHABET:
            pos = ALPHABET.index(char)
            new_pos = (pos - shift) % len(ALPHABET)
            decrypted += ALPHABET[new_pos]
        else:
            decrypted += char
    return decrypted

encrypted = encrypt(text, shift)

with open(ENCRYPTED_FILE, 'w', encoding='utf-8') as f:
    f.write(encrypted)

print('Зашифрованный текст сохранен в файл: ' + ENCRYPTED_FILE)
print('Первые 100 символов зашифрованного текста:')
print(encrypted[:100] + '...')
print()

with open(KEY_FILE, 'w', encoding='utf-8') as f:
    f.write('Ключ шифрования (сдвиг ' + str(shift) + ')\n')
    f.write('Алфавит: ' + ALPHABET + '\n\n')
    f.write('Таблица замены:\n')
    for i, letter in enumerate(ALPHABET):
        new_letter = ALPHABET[(i + shift) % len(ALPHABET)]
        f.write(letter + ' -> ' + new_letter + '\n')

print('Ключ шифрования сохранен в файл: ' + KEY_FILE)
print()

decrypted = decrypt(encrypted, shift)

with open(CHECK_FILE, 'w', encoding='utf-8') as f:
    f.write(decrypted)

if text == decrypted:
    print(' Дешифровка выполнена успешно. Текст восстановлен полностью.')
else:
    print('Ошибка дешифровки')

print('Проверочный файл сохранен: ' + CHECK_FILE)
print()
print('Все файлы созданы:')
print('- ' + INPUT_FILE)
print('- ' + ENCRYPTED_FILE)
print('- ' + KEY_FILE)
print('- ' + CHECK_FILE)