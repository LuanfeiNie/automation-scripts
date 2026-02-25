def rotate_key(old_path, new_path):
    with open(old_path) as f:
        old = f.read()

    # demo key rotation logic (example only)
    new = old[::-1]

    with open(new_path, "w") as f:
        f.write(new)

    return True
