import os
import zipfile
from PIL import Image

output_dir = "D:/Project/nekogram-desktop/Themes"
os.makedirs(output_dir, exist_ok=True)

# Read base templates
with open("D:/Project/nekogram-desktop/night_extracted/colors.tdesktop-theme", "r", encoding="utf-8") as f:
    night_base = f.read()

with open("D:/Project/nekogram-desktop/day_extracted/colors.tdesktop-theme", "r", encoding="utf-8") as f:
    day_base = f.read()

def apply_overrides(base_text, overrides):
    lines = base_text.splitlines()
    new_lines = []
    overridden_keys = set()
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("//") and ":" in stripped:
            key = stripped.split(":")[0].strip()
            if key in overrides:
                new_lines.append(f"{key}: {overrides[key]};")
                overridden_keys.add(key)
                continue
        new_lines.append(line)
    
    # Append any keys that weren't in base
    for key, val in overrides.items():
        if key not in overridden_keys:
            new_lines.append(f"{key}: {val};")
            
    return "\n".join(new_lines)

def make_bg_image(color_hex, out_path):
    # Create 16x16 solid background
    hex_clean = color_hex.lstrip('#')[:6]
    r = int(hex_clean[0:2], 16)
    g = int(hex_clean[2:4], 16)
    b = int(hex_clean[4:6], 16)
    img = Image.new('RGB', (16, 16), (r, g, b))
    img.save(out_path, format='PNG')

def create_theme(filename, base_type, overrides, bg_color):
    base_text = night_base if base_type == "dark" else day_base
    theme_content = apply_overrides(base_text, overrides)
    
    temp_theme_file = os.path.join(output_dir, "colors.tdesktop-theme")
    temp_bg_file = os.path.join(output_dir, "background.png")
    
    with open(temp_theme_file, "w", encoding="utf-8") as f:
        f.write(theme_content)
        
    make_bg_image(bg_color, temp_bg_file)
    
    zip_path = os.path.join(output_dir, filename)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(temp_theme_file, "colors.tdesktop-theme")
        zf.write(temp_bg_file, "background.png")
        
    os.remove(temp_theme_file)
    os.remove(temp_bg_file)
    print(f"Created theme: {zip_path}")

# ==========================================
# 1. Neko AMOLED (Pure Black)
# ==========================================
amoled_overrides = {
    "windowBg": "#000000",
    "windowFg": "#ffffff",
    "windowBgOver": "#121212",
    "windowBgRipple": "#1c1c1c",
    "windowFgOver": "#ffffff",
    "windowSubTextFg": "#7c7c7c",
    "windowSubTextFgOver": "#999999",
    "windowBoldFg": "#ffffff",
    "windowBoldFgOver": "#ffffff",
    "windowBgActive": "#2f5abb",
    "windowFgActive": "#ffffff",
    "windowActiveTextFg": "#51aaee",
    "windowShadowFg": "#000000",
    "windowShadowFgFallback": "#000000",
    "titleBg": "#000000",
    "titleBgActive": "#000000",
    "titleShadow": "#000000",
    "columnDividerBg": "#1a1a1a",
    "sideBarBg": "#000000",
    "sideBarBgOver": "#121212",
    "sideBarBgActive": "#1a1a1a",
    "dialogsBg": "#000000",
    "dialogsBgOver": "#121212",
    "dialogsBgActive": "#1a2a3a",
    "dialogsNameFg": "#ffffff",
    "dialogsNameFgOver": "#ffffff",
    "dialogsChatIconFg": "#7c7c7c",
    "dialogsDateFg": "#666666",
    "dialogsTextFg": "#888888",
    "dialogsTextFgOver": "#a0a0a0",
    "dialogsDraftFg": "#e54a4a",
    "dialogsVerifiedIconBg": "#366caf",
    "dialogsSendingIconFg": "#666666",
    "dialogsSentIconFg": "#366caf",
    "dialogsUnreadBg": "#366caf",
    "dialogsUnreadBgMuted": "#222222",
    "dialogsUnreadFg": "#ffffff",
    "historyTextInFg": "#fafafa",
    "historyTextInFgSelected": "#ffffff",
    "historyTextOutFg": "#fafafa",
    "historyTextOutFgSelected": "#ffffff",
    "historyLinkInFg": "#51aaee",
    "historyLinkOutFg": "#51aaee",
    "historyFileNameInFg": "#ffffff",
    "historyFileNameOutFg": "#ffffff",
    "historyOutIconFg": "#366caf",
    "historyOutIconFgSelected": "#ffffff",
    "historyIconFgInverted": "#ffffff",
    "msgInBg": "#0d0d0d",
    "msgInBgSelected": "#1c2c3c",
    "msgInShadow": "#00000000",
    "msgOutBg": "#18324f",
    "msgOutBgSelected": "#24456c",
    "msgOutShadow": "#00000000",
    "historyComposeAreaBg": "#000000",
    "historyComposeAreaFg": "#ffffff",
    "historySendIcon": "#366caf",
    "historySendIconOver": "#51aaee",
    "boxBg": "#141414",
    "boxTitleFg": "#ffffff",
    "menuBg": "#141414",
    "menuBgOver": "#222222",
    "mainMenuBg": "#000000",
    "mainMenuCoverBg": "#0a0a0a",
    "activeButtonBg": "#366caf",
    "activeButtonBgOver": "#417dbf",
    "activeButtonBgRipple": "#4a88cc",
}
create_theme("Neko AMOLED (Pure Black).tdesktop-theme", "dark", amoled_overrides, "#000000")

# ==========================================
# 2. Neko Dark Blue
# ==========================================
darkblue_overrides = {
    "windowBg": "#151e27",
    "windowFg": "#fafafa",
    "windowBgOver": "#1d2733",
    "windowBgRipple": "#242f3d",
    "windowFgOver": "#ffffff",
    "windowSubTextFg": "#73889c",
    "windowSubTextFgOver": "#8ca1b5",
    "windowBoldFg": "#ffffff",
    "windowBoldFgOver": "#ffffff",
    "windowBgActive": "#3e618a",
    "windowFgActive": "#ffffff",
    "windowActiveTextFg": "#6ba4e0",
    "dialogsBg": "#151e27",
    "dialogsBgOver": "#1d2733",
    "dialogsBgActive": "#243242",
    "dialogsNameFg": "#ffffff",
    "dialogsUnreadBg": "#3e618a",
    "historyTextInFg": "#fafafa",
    "historyTextOutFg": "#fafafa",
    "msgInBg": "#212d3b",
    "msgInBgSelected": "#2d3e52",
    "msgOutBg": "#36557a",
    "msgOutBgSelected": "#426794",
    "historyComposeAreaBg": "#151e27",
    "boxBg": "#1d2733",
    "menuBg": "#1d2733",
    "mainMenuBg": "#151e27",
}
create_theme("Neko Dark Blue.tdesktop-theme", "dark", darkblue_overrides, "#151e27")

# ==========================================
# 3. Neko Material You Dark (Monet Dark)
# ==========================================
monet_dark_overrides = {
    "windowBg": "#1a1c1e",
    "windowFg": "#e2e2e6",
    "windowBgOver": "#282a2d",
    "windowBgRipple": "#323538",
    "windowFgOver": "#ffffff",
    "windowSubTextFg": "#8c9199",
    "windowSubTextFgOver": "#a6abb3",
    "windowBoldFg": "#ffffff",
    "windowBgActive": "#a8c7fa",
    "windowFgActive": "#04315c",
    "windowActiveTextFg": "#a8c7fa",
    "dialogsBg": "#1a1c1e",
    "dialogsBgOver": "#282a2d",
    "dialogsBgActive": "#004a77",
    "dialogsNameFg": "#ffffff",
    "dialogsUnreadBg": "#a8c7fa",
    "dialogsUnreadFg": "#04315c",
    "historyTextInFg": "#e2e2e6",
    "historyTextOutFg": "#ffffff",
    "msgInBg": "#282a2d",
    "msgInBgSelected": "#004a77",
    "msgOutBg": "#004a77",
    "msgOutBgSelected": "#005d95",
    "historyComposeAreaBg": "#1a1c1e",
    "boxBg": "#222427",
    "menuBg": "#222427",
    "mainMenuBg": "#1a1c1e",
    "activeButtonBg": "#a8c7fa",
    "activeButtonFg": "#04315c",
}
create_theme("Neko Monet Dark.tdesktop-theme", "dark", monet_dark_overrides, "#1a1c1e")

# ==========================================
# 4. Neko Arctic (Ice Blue)
# ==========================================
arctic_overrides = {
    "windowBg": "#ffffff",
    "windowFg": "#1c242c",
    "windowBgOver": "#f2f6fa",
    "windowBgRipple": "#e4edf5",
    "windowFgOver": "#1c242c",
    "windowSubTextFg": "#7e909e",
    "windowSubTextFgOver": "#6c7e8c",
    "windowBoldFg": "#1c242c",
    "windowBgActive": "#3490eb",
    "windowFgActive": "#ffffff",
    "windowActiveTextFg": "#2880d9",
    "dialogsBg": "#ffffff",
    "dialogsBgOver": "#f2f6fa",
    "dialogsBgActive": "#3490eb",
    "dialogsNameFg": "#1c242c",
    "dialogsUnreadBg": "#3490eb",
    "historyTextInFg": "#1c242c",
    "historyTextOutFg": "#ffffff",
    "msgInBg": "#ffffff",
    "msgInBgSelected": "#c5e1fb",
    "msgOutBg": "#3490eb",
    "msgOutBgSelected": "#2480dc",
    "historyComposeAreaBg": "#ffffff",
    "boxBg": "#ffffff",
    "menuBg": "#ffffff",
    "mainMenuBg": "#ffffff",
    "activeButtonBg": "#3490eb",
    "activeButtonFg": "#ffffff",
}
create_theme("Neko Arctic (Ice Blue).tdesktop-theme", "light", arctic_overrides, "#d8e4f3")

# ==========================================
# 5. Neko Blue Bubbles
# ==========================================
bluebubbles_overrides = {
    "windowBg": "#f7f9fa",
    "windowFg": "#111111",
    "windowBgOver": "#edf1f4",
    "windowBgRipple": "#e1e7eb",
    "windowFgOver": "#111111",
    "windowSubTextFg": "#88949e",
    "windowBoldFg": "#111111",
    "windowBgActive": "#2481cc",
    "windowFgActive": "#ffffff",
    "windowActiveTextFg": "#2481cc",
    "dialogsBg": "#ffffff",
    "dialogsBgOver": "#f2f5f7",
    "dialogsBgActive": "#2481cc",
    "dialogsNameFg": "#111111",
    "dialogsUnreadBg": "#2481cc",
    "historyTextInFg": "#111111",
    "historyTextOutFg": "#ffffff",
    "msgInBg": "#ffffff",
    "msgInBgSelected": "#d6eaf8",
    "msgOutBg": "#2481cc",
    "msgOutBgSelected": "#1b6fae",
    "historyComposeAreaBg": "#ffffff",
    "boxBg": "#ffffff",
    "menuBg": "#ffffff",
    "mainMenuBg": "#ffffff",
}
create_theme("Neko Blue Bubbles.tdesktop-theme", "light", bluebubbles_overrides, "#e6f0f8")

# ==========================================
# 6. Neko Material You Light (Monet Light)
# ==========================================
monet_light_overrides = {
    "windowBg": "#fdfcff",
    "windowFg": "#1a1c1e",
    "windowBgOver": "#f1f0f4",
    "windowBgRipple": "#e4e2e6",
    "windowFgOver": "#1a1c1e",
    "windowSubTextFg": "#73777f",
    "windowSubTextFgOver": "#5b5f66",
    "windowBoldFg": "#1a1c1e",
    "windowBgActive": "#00629e",
    "windowFgActive": "#ffffff",
    "windowActiveTextFg": "#00629e",
    "dialogsBg": "#fdfcff",
    "dialogsBgOver": "#f1f0f4",
    "dialogsBgActive": "#d3e4ff",
    "dialogsNameFg": "#1a1c1e",
    "dialogsUnreadBg": "#00629e",
    "historyTextInFg": "#1a1c1e",
    "historyTextOutFg": "#001d36",
    "msgInBg": "#f1f0f4",
    "msgInBgSelected": "#d3e4ff",
    "msgOutBg": "#d3e4ff",
    "msgOutBgSelected": "#b3d2ff",
    "historyComposeAreaBg": "#fdfcff",
    "boxBg": "#fdfcff",
    "menuBg": "#fdfcff",
    "mainMenuBg": "#fdfcff",
    "activeButtonBg": "#00629e",
    "activeButtonFg": "#ffffff",
}
create_theme("Neko Monet Light.tdesktop-theme", "light", monet_light_overrides, "#f4f6fa")

print("\nAll 6 Nekogram Desktop themes created successfully!")
