def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
