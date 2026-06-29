from pathlib import Path
import base64

mode = Path("lab_mode.txt").read_text(encoding="utf-8").strip().lower()

if mode not in ["clean", "suspicious"]:
    raise SystemExit("lab_mode.txt must contain either: clean or suspicious")

Path("images").mkdir(exist_ok=True)

# First image: coin
png_data_1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAARElEQVR4nM2SQQrAIAwD/f+nHAaDBwdlYZY1lKJk5SsKiIiYuJGxTTsQVzAe+lfLO1v2ZPqqv8jTezXLMAxrUlXqOQ6SN+gPEhNCDvoY2QAAAABJRU5ErkJggg=="
)

# Second image: TIU picture
png_data_2 = Path("images/TIU1.png").read_bytes()

# Add hidden text only to the TIU image
if mode == "suspicious":
    png_data_2 += b"\ncyberclass: lolol this is secret.\n"

Path("images/student_image.png").write_bytes(png_data_1)
Path("images/student_image2.png").write_bytes(png_data_2)

print("Created images/student_image.png")
print(f"Created images/student_image2.png in {mode} mode")
