import os


def merge_file(file_path):
    chunk_number = 1
    merged_file_path = f"{file_path}"
    with open(merged_file_path, "wb") as merged_file:
        while True:
            chunk_file_path = f"{file_path}.part{chunk_number}"
            if not os.path.exists(chunk_file_path):
                break
            with open(chunk_file_path, "rb") as chunk_file:
                chunk = chunk_file.read()
                merged_file.write(chunk)
            chunk_number += 1


def split_file(file_path):
    chunk_size = 80 * 1024 * 1024  # 80MB in bytes
    with open(file_path, "rb") as file:
        chunk_number = 0
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            chunk_number += 1
            chunk_file_path = f"{file_path}.part{chunk_number}"
            with open(chunk_file_path, "wb") as chunk_file:
                chunk_file.write(chunk)


if __name__ == "__main__":
    split_file("./best_model/model.pdopt")
    os.remove("./best_model/model.pdopt")
