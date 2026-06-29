from pathlib import Path
import base64

mode = Path("lab_mode.txt").read_text(encoding="utf-8").strip().lower()

if mode not in ["clean", "suspicious"]:
    raise SystemExit("lab_mode.txt must contain either: clean or suspicious")

Path("images").mkdir(exist_ok=True)

# Small valid 16x16 PNG image (pixel-art coin).
png_data = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAhUlEQVR4nKWT2RGAIAxEU4SVWJPdWBEdpAPLiTOoY44NIH7sB8d7QCaQiJAOEUkWv7fu97CUO8d6pbxzSBJhB+7bUpNJIqwgDyNJCmsAzT0SI8hObD3FFC6D0ToUfMmUoH0D7sNVwC0B44KZsReYPuB4VTQ2fQDbeKB4/b8wAAfB7984kxOTwXamWcXf/AAAAABJRU5ErkJggg=="
)

if mode == "suspicious":
    png_data += b"\nPRIVATEKEY: lolol this is secret.\n"

Path("images/student_image.png").write_bytes(png_data)

print(f"Created images/student_image.png in {mode} mode")
