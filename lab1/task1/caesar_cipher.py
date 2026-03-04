from files1 import ALPHABET, INPUT_FILE, ENCRYPTED_FILE, KEY_FILE, CHECK_FILE

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


def read_text_from_file(file_path: str) -> str:
    """
    Читает текст из файла.
    
    Args:
        file_path: Путь к файлу
    
    Returns:
        Содержимое файла
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_text_to_file(file_path: str, text: str) -> None:
    """
    Записывает текст в файл.
    
    Args:
        file_path: Путь к файлу
        text: Текст для записи
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


def save_key_file(shift: int) -> None:
    """
    Сохраняет ключ шифрования в файл.
    
    Args:
        shift: Величина сдвига
    """
    with open(KEY_FILE, 'w', encoding='utf-8') as f:
        f.write(f'Ключ шифрования (сдвиг {shift})\n')
        f.write(f'Алфавит: {ALPHABET}\n\n')
        f.write('Таблица замены:\n')
        for i, letter in enumerate(ALPHABET):
            new_letter = ALPHABET[(i + shift) % len(ALPHABET)]
            f.write(f'{letter} -> {new_letter}\n')


def print_file_info(text: str, file_path: str, label: str) -> None:
    """
    Выводит информацию о файле.
    
    Args:
        text: Текст из файла
        file_path: Путь к файлу
        label: Метка для вывода
    """
    print(f'{label} прочитан из файла: {file_path}')
    print(f'Длина текста: {len(text)} символов')
    print('Первые 100 символов:')
    print(f'{text[:100]}...')
    print()


def main() -> None:
    """
    Основная функция программы.
    """
    text = read_text_from_file(INPUT_FILE)
    print_file_info(text, INPUT_FILE, 'Исходный текст')
    
    shift = 9
    print(f'Выбран сдвиг: {shift} (вправо)')
    
    encrypted = encrypt(text, shift)
    write_text_to_file(ENCRYPTED_FILE, encrypted)
    print(f'Зашифрованный текст сохранен в файл: {ENCRYPTED_FILE}')
    print(f'Первые 100 символов зашифрованного текста:')
    print(f'{encrypted[:100]}...')
    print()

    save_key_file(shift)
    print(f'Ключ шифрования сохранен в файл: {KEY_FILE}')
    print()
    
    decrypted = decrypt(encrypted, shift)
    write_text_to_file(CHECK_FILE, decrypted)
    
    if text == decrypted:
        print('Дешифровка выполнена успешно. Текст восстановлен полностью.')
    else:
        print('Ошибка дешифровки')
    
    print(f'Проверочный файл сохранен: {CHECK_FILE}')
    print()
    print('Все файлы созданы:')
    print(f'- {INPUT_FILE}')
    print(f'- {ENCRYPTED_FILE}')
    print(f'- {KEY_FILE}')
    print(f'- {CHECK_FILE}')


if __name__ == '__main__':
    main()
