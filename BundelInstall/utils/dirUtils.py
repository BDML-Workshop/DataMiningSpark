import os

def create_dir_if_not_exists(logger, dir_path):
    if not os.path.exists(dir_path):
        logger.info("Creating %s directory", dir_path)
        os.makedirs(dir_path)
    else:
        logger.info(f"Directory {dir_path} exists" 