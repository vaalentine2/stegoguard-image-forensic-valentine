from pathlib import Path
import base64

mode = Path("lab_mode.txt").read_text(encoding="utf-8").strip().lower()

if mode not in ["clean", "suspicious"]:
    raise SystemExit("lab_mode.txt must contain either: clean or suspicious")

Path("images").mkdir(exist_ok=True)

# Small valid 16x16 PNG image (pixel-art coin).
png_data = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAARElEQVR4nM2SQQrAIAwD/f+nHAaDBwdlYZY1lKJk5SsKiIiYuJGxTTsQVzAe+lfLO1v2ZPqqv8jTezXLMAxrUlXqOQ6SN+gPEhNCDvoY2QAAAABJRU5ErkJggg=="
)

if mode == "suspicious":
    png_data += b"\nCONFIDENTIAL: lolol this is secret.\n"

Path("images/student_image.png").write_bytes(png_data)

print(f"Created images/student_image.png in {mode} mode")
