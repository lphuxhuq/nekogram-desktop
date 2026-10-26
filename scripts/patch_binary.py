import sys

def patch_exe(path):
    with open(path, 'rb') as f:
        data = f.read()

    old_b = b'"lng_settings_enhanced": "Enhanced Settings",'
    new_b = b'"lng_settings_enhanced": "Neko Settings"    ,'

    assert len(old_b) == len(new_b), "Length mismatch"

    if old_b in data:
        data = data.replace(old_b, new_b)
        with open(path, 'wb') as f:
            f.write(data)
        print(f"Patched 'Neko Settings' into {path} successfully.")
    else:
        print(f"Pattern not found in {path} (already patched or different binary).")

if __name__ == '__main__':
    exe_file = sys.argv[1] if len(sys.argv) > 1 else 'dist/Nekogram.exe'
    patch_exe(exe_file)
