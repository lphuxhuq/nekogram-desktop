import sys

# All variants must be exactly the same byte length (45) so the embedded
# language JSON can be rewritten in place without shifting the resource.
OLD_EN = b'"lng_settings_enhanced": "Enhanced Settings",'
OLD_NEKO = b'"lng_settings_enhanced": "Neko Settings"    ,'
NEW_VI = b'"lng_settings_enhanced": "C\xc3\xa0i \xc4\x91\xe1\xba\xb7t Neko" ,'

for _b in (OLD_EN, OLD_NEKO, NEW_VI):
    assert len(_b) == 45, (len(_b), _b)


def patch_exe(path):
    with open(path, 'rb') as f:
        data = f.read()

    if NEW_VI in data:
        print('Already Vietnamese:', path)
        return

    for old in (OLD_EN, OLD_NEKO):
        if old in data:
            data = data.replace(old, NEW_VI)
            with open(path, 'wb') as f:
                f.write(data)
            print('Patched -> "Cai dat Neko":', path)
            return

    print('Pattern not found in', path, '(different binary build)')


if __name__ == '__main__':
    patch_exe(sys.argv[1] if len(sys.argv) > 1 else 'dist/Nekogram.exe')
