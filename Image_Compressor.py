from PIL import Image
import argparse
import os


def compress_image(input_file, output_dir, quality=85, format="JPEG"):
    """
    Compresses the input image and saves it to the specified output directory.

    Parameters:
    - input_file: Path to the input image file.
    - output_dir: Directory where the compressed image will be saved.
    - quality: Compression quality (0-100, higher is better, default is 85).
    - format: Output image format (default is 'JPEG').

    Returns:
    - None
    """
    try:
        # Open the image file
        with Image.open(input_file) as img:
            # Resize image to maintain aspect ratio
            img = img.resize(img.size, Image.ANTIALIAS)
            
            # Construct the output file path
            output_filename = os.path.join(
                output_dir, f"compressed_{os.path.basename(input_file)}"
            )
            
            # Save the compressed image
            img.save(output_filename, format=format, quality=quality)
            print(f"Image compressed and saved as '{output_filename}'")
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="Image Compression Tool")
    parser.add_argument("input", type=str, help="Input image file")
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default="./compressed",
        help="Output directory for compressed image (default is './compressed')",
    )
    parser.add_argument(
        "-q",
        "--quality",
        type=int,
        default=85,
        help="Compression quality (0-100, higher is better, default is 85)",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="JPEG",
        help="Output image format (e.g., JPEG, PNG, default is JPEG)",
    )

    args = parser.parse_args()

    # Validate and create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Call the image compression function
    compress_image(args.input, args.output_dir, args.quality, args.format)


if __name__ == "__main__":
    main()
