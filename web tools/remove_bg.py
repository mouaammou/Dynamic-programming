from rembg import remove, new_session
from PIL import Image
import sys
import os
from io import BytesIO

MAX_INPUT_SIZE_BYTES = 1 * 1024 * 1024  # 1 MB


def _encoded_size_bytes(image: Image.Image, quality: int = 85) -> int:
    """Estimate image size in bytes when encoded as JPEG."""
    buf = BytesIO()
    img = image.convert("RGB") if image.mode not in ("RGB", "L") else image
    img.save(buf, format="JPEG", quality=quality, optimize=True)
    return buf.tell()


def resize_to_max_1mb(image: Image.Image, max_bytes: int = MAX_INPUT_SIZE_BYTES) -> Image.Image:
    """Downscale image until estimated encoded size is <= max_bytes."""
    resized = image.copy()
    resampling = getattr(Image, "Resampling", Image).LANCZOS

    while _encoded_size_bytes(resized) > max_bytes:
        current_size = _encoded_size_bytes(resized)
        scale = (max_bytes / current_size) ** 0.5 * 0.95  # safety margin
        scale = min(scale, 0.95)

        new_w = max(1, int(resized.width * scale))
        new_h = max(1, int(resized.height * scale))

        if (new_w, new_h) == resized.size:
            break

        resized = resized.resize((new_w, new_h), resampling)

    return resized


def remove_background(input_path, output_path=None):
    if not os.path.exists(input_path):
        print("❌ Input file does not exist.")
        return

    session = new_session("birefnet-general")

    # Open image
    input_image = Image.open(input_path)

    # If input file exceeds 1 MB, resize before background removal
    if os.path.getsize(input_path) > MAX_INPUT_SIZE_BYTES:
        print("ℹ️ Input image exceeds 1 MB. Resizing before background removal...")
        input_image = resize_to_max_1mb(input_image)

    # Remove background
    output_image = remove(input_image, session=session)

    # If no output path provided, generate one
    if not output_path:
        filename, _ = os.path.splitext(input_path)
        output_path = f"{filename}_no_bg.png"

    # Save as PNG (important for transparency)
    output_image.save(output_path)

    print("✅ Background removed successfully!")
    print(f"Saved as: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_bg.py input_image.jpg [output_image.png]")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        remove_background(input_path, output_path)