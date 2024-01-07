import os
import pyAesCrypt


# Расшифровываем базу данных
def decrypt() -> object:
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        encrypted_file = os.path.join(base_dir, 'users.cw')
        decrypted_file = os.path.join(base_dir, 'users.sqlite')

        pyAesCrypt.decryptFile(encrypted_file, decrypted_file, 'Opo@hm4b0?PVQhy', 1024 * 1024)
    except Exception as e:
        # Обработка ошибок
        print("Ошибка:", str(e))


# Шифруем базу данных
def cipher() -> object:
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        decrypted_file = os.path.join(base_dir, 'users.sqlite')
        encrypted_file = os.path.join(base_dir, 'users.cw')

        pyAesCrypt.encryptFile(decrypted_file, encrypted_file, 'Opo@hm4b0?PVQhy', 1024 * 1024)

        # Удаляем исходник
        os.remove(decrypted_file)
    except Exception as e:
        # Обработка ошибок
        print("Ошибка:", str(e))