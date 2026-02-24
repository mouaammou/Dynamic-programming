from rembg import remove, new_session
from PIL import Image, ImageOps
from io import BytesIO
import argparse
import os


DEFAULT_MAX_INPUT_SIZE_BYTES = 500 * 1024  # 500 KB


def _encoded_size_bytes(image: Image.Image, quality: int = 85) -> int:
    """Estimate image size in bytes when encoded as JPEG."""
    buf = BytesIO()
    img = image.convert("RGB") if image.mode not in ("RGB", "L") else image
    img.save(buf, format="JPEG", quality=quality, optimize=True)
    return buf.tell()


def resize_to_max_size(image: Image.Image, max_bytes: int = DEFAULT_MAX_INPUT_SIZE_BYTES) -> Image.Image:
    """Downscale image until estimated encoded size is <= max_bytes."""
    resized = image.copy()
    resampling = getattr(Image, "Resampling", Image).LANCZOS

    while True:
        current_size = _encoded_size_bytes(resized)
        if current_size <= max_bytes:
            break

        scale = (max_bytes / current_size) ** 0.5 * 0.95  # safety margin
        scale = min(scale, 0.95)

        new_w = max(1, int(resized.width * scale))
        new_h = max(1, int(resized.height * scale))

        if (new_w, new_h) == resized.size:
            break

        resized = resized.resize((new_w, new_h), resampling)

    return resized


def remove_background(
    input_path: str,
    output_path: str | None = None,
    max_bytes: int = DEFAULT_MAX_INPUT_SIZE_BYTES,
    model: str | None = None,
) -> str | None:
    if not os.path.isfile(input_path):
        print("❌ Input file does not exist or is not a file.")
        return None

    try:
        with Image.open(input_path) as img:
            input_image = ImageOps.exif_transpose(img).copy()
    except Exception as e:
        print(f"❌ Failed to open image: {e}")
        return None

    try:
        if os.path.getsize(input_path) > max_bytes:
            print(f"ℹ️ Input image exceeds {max_bytes // 1024} KB. Resizing before background removal...")
            input_image = resize_to_max_size(input_image, max_bytes=max_bytes)

        #  session = new_session('u2net_human_seg')
        session = new_session(model) if model else None
        output_image = remove(input_image, session=session) if session else remove(input_image)
    except Exception as e:
        print(f"❌ Background removal failed: {e}")
        return None

    if not output_path:
        filename, _ = os.path.splitext(input_path)
        output_path = f"{filename}_no_bg.png"

    try:
        out_dir = os.path.dirname(output_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        output_image.save(output_path, format="PNG")
    except Exception as e:
        print(f"❌ Failed to save output: {e}")
        return None

    print("✅ Background removed successfully!")
    print(f"Saved as: {output_path}")
    return output_path


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Remove image background using rembg.")
    parser.add_argument("input_image", help="Path to input image")
    parser.add_argument("output_image", nargs="?", default=None, help="Path to output PNG (optional)")
    parser.add_argument(
        "--max-kb",
        type=int,
        default=DEFAULT_MAX_INPUT_SIZE_BYTES // 1024,
        help="Max input size threshold in KB before resizing (default: 500)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help='Optional rembg model, e.g. "birefnet-general"',
    )
    return parser


if __name__ == "__main__":
    args = _build_parser().parse_args()
    remove_background(
        input_path=args.input_image,
        output_path=args.output_image,
        max_bytes=max(1, args.max_kb) * 1024,
        model=args.model,
    )