import os
import shutil
import time
import configparser
import logging

def setup_logging():
    logging.basicConfig(
        filename='backup_daemon.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_files_in_directory(directory):
    # Возвращает список файлов в указанной папке
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def backup_folder(source_folder, destination_folder):
    try:
        # Получение списка файлов и папок в папке источника и назначения
        source_items = set(os.listdir(source_folder))
        destination_items = set(os.listdir(destination_folder))

        # Копирование файлов и папок
        copied_items = source_items - destination_items
        for item in copied_items:
            source_item_path = os.path.join(source_folder, item)
            destination_item_path = os.path.join(destination_folder, item)

            if os.path.isdir(source_item_path):
                shutil.copytree(source_item_path, destination_item_path, dirs_exist_ok=True)
                copied_files = get_files_in_directory(source_item_path)
                if copied_files:
                    logging.info(f"Iteration {time.time()}: Copied folder '{item}' with files: {', '.join(copied_files)}")
            elif os.path.isfile(source_item_path):
                shutil.copy2(source_item_path, destination_item_path)
                logging.info(f"Iteration {time.time()}: Copied file '{item}'")

        # Удаление файлов и папок в destination_folder, которых нет в source_folder
        deleted_items = destination_items - source_items
        for item in deleted_items:
            item_path = os.path.join(destination_folder, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                logging.info(f"Iteration {time.time()}: Deleted file '{item}'")
            elif os.path.isdir(item_path):
                deleted_files = get_files_in_directory(item_path)
                shutil.rmtree(item_path)
                if deleted_files:
                    logging.info(f"Iteration {time.time()}: Deleted folder '{item}' with files: {', '.join(deleted_files)}")

        if not copied_items and not deleted_items:
            logging.info(f"Backup completed (nothing changed): {source_folder} -> {destination_folder}")
        else:
            logging.info(f"Backup completed: {source_folder} -> {destination_folder}")
    except Exception as e:
        logging.error(f"Backup failed: {e}")

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Имя вашего конфигурационного файла
    source_folder = config.get('Settings', 'SourceFolder')
    destination_folder = config.get('Settings', 'DestinationFolder')
    interval_seconds = int(config.get('Settings', 'IntervalSeconds'))
    return source_folder, destination_folder, interval_seconds

def main():
    setup_logging()
    source_folder, destination_folder, interval_seconds = read_config()

    while True:
        backup_folder(source_folder, destination_folder)
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
