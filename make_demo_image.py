from pathlib import Path
import base64

Path("images").mkdir(exist_ok=True)

# First image: clean coin image
png_data_1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAARElEQVR4nM2SQQrAIAwD/f+nHAaDBwdlYZY1lKJk5SsKiIiYuJGxTTsQVzAe+lfLO1v2ZPqqv8jTezXLMAxrUlXqOQ6SN+gPEhNCDvoY2QAAAABJRU5ErkJggg=="
)

# Second image: TIU image
png_data_2 = Path("images/TIU1.png").read_bytes()

# Add suspicious hidden text to second image
png_data_2 += b"\ncyberclass: lolol this is secret.\n"

Path("images/student_image.png").write_bytes(png_data_1)
Path("images/student_image2.png").write_bytes(png_data_2)

print("Created images/student_image.png")
print("Created images/student_image2.png")
