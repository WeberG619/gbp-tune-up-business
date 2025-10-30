#!/usr/bin/env python3
"""
Photo Batch Processor - AI upscale, background cleanup, and batch optimization

Usage:
    python photo_processor.py input_folder/ output_folder/
    python photo_processor.py single_image.jpg output/
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple
from PIL import Image, ImageEnhance, ImageFilter
import pillow_heif  # For HEIF/HEIC support


class PhotoProcessor:
    """Process and optimize photos for Google Business Profile"""

    # GBP optimal sizes
    GBP_MIN_SIZE = (720, 720)
    GBP_OPTIMAL_SIZE = (2048, 2048)
    GBP_MAX_SIZE = (10240, 10240)

    # Quality settings
    JPEG_QUALITY = 90
    WEBP_QUALITY = 85

    def __init__(self, enhance: bool = True, resize: bool = True, background_cleanup: bool = False):
        """
        Initialize processor

        Args:
            enhance: Apply auto-enhancement (brightness, contrast, sharpness)
            resize: Resize to optimal GBP dimensions
            background_cleanup: Remove/blur backgrounds (basic implementation)
        """
        self.enhance = enhance
        self.resize = resize
        self.background_cleanup = background_cleanup

        # Register HEIF opener (for iPhone photos)
        try:
            pillow_heif.register_heif_opener()
        except:
            pass

    def process_image(self, input_path: str, output_path: str,
                     format: str = 'JPEG') -> bool:
        """
        Process single image

        Args:
            input_path: Path to input image
            output_path: Path to save processed image
            format: Output format (JPEG, PNG, WEBP)

        Returns:
            True if successful
        """
        try:
            print(f"📷 Processing: {Path(input_path).name}")

            # Load image
            img = Image.open(input_path)

            # Convert RGBA to RGB if saving as JPEG
            if img.mode == 'RGBA' and format == 'JPEG':
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])  # Alpha channel as mask
                img = background
            elif img.mode != 'RGB' and format == 'JPEG':
                img = img.convert('RGB')

            # Auto-rotate based on EXIF
            img = self._auto_rotate(img)

            # Resize to optimal dimensions
            if self.resize:
                img = self._smart_resize(img)

            # Enhance image quality
            if self.enhance:
                img = self._enhance_image(img)

            # Background cleanup (basic blur for now)
            if self.background_cleanup:
                img = self._blur_background(img)

            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)

            # Save with optimal settings
            save_kwargs = {
                'optimize': True,
                'quality': self.JPEG_QUALITY if format == 'JPEG' else self.WEBP_QUALITY
            }

            if format == 'JPEG':
                save_kwargs['progressive'] = True

            img.save(output_path, format=format, **save_kwargs)

            # Get file size reduction
            original_size = os.path.getsize(input_path)
            new_size = os.path.getsize(output_path)
            reduction = (1 - new_size / original_size) * 100

            print(f"  ✅ Saved: {Path(output_path).name} ({reduction:.1f}% smaller)")
            return True

        except Exception as e:
            print(f"  ❌ Error processing {input_path}: {e}")
            return False

    def process_batch(self, input_dir: str, output_dir: str,
                     formats: List[str] = ['JPEG']) -> Tuple[int, int]:
        """
        Process all images in a directory

        Args:
            input_dir: Directory containing input images
            output_dir: Directory to save processed images
            formats: List of output formats to generate

        Returns:
            Tuple of (successful_count, failed_count)
        """
        input_path = Path(input_dir)
        output_path = Path(output_dir)

        # Supported extensions
        extensions = {'.jpg', '.jpeg', '.png', '.heic', '.heif', '.webp', '.bmp', '.tiff'}

        # Find all images
        images = [f for f in input_path.iterdir()
                 if f.suffix.lower() in extensions and f.is_file()]

        if not images:
            print(f"❌ No images found in {input_dir}")
            return 0, 0

        print(f"\n🚀 Processing {len(images)} images...")
        print(f"   Input: {input_dir}")
        print(f"   Output: {output_dir}")
        print(f"   Formats: {', '.join(formats)}\n")

        success = 0
        failed = 0

        for img_file in images:
            for fmt in formats:
                # Generate output filename
                stem = img_file.stem
                ext = '.jpg' if fmt == 'JPEG' else f'.{fmt.lower()}'
                output_file = output_path / f"{stem}_optimized{ext}"

                if self.process_image(str(img_file), str(output_file), format=fmt):
                    success += 1
                else:
                    failed += 1

        print(f"\n✨ Complete: {success} successful, {failed} failed")
        return success, failed

    def _auto_rotate(self, img: Image.Image) -> Image.Image:
        """Auto-rotate image based on EXIF orientation"""
        try:
            exif = img._getexif()
            if exif is not None:
                orientation = exif.get(0x0112)  # Orientation tag
                if orientation:
                    rotations = {
                        3: 180,
                        6: 270,
                        8: 90
                    }
                    if orientation in rotations:
                        img = img.rotate(rotations[orientation], expand=True)
        except:
            pass
        return img

    def _smart_resize(self, img: Image.Image) -> Image.Image:
        """Resize image to optimal GBP dimensions while maintaining aspect ratio"""
        width, height = img.size

        # Skip if already optimal size
        if width == self.GBP_OPTIMAL_SIZE[0] and height == self.GBP_OPTIMAL_SIZE[1]:
            return img

        # Calculate aspect ratio
        aspect = width / height

        # Determine target size
        if width < self.GBP_MIN_SIZE[0] or height < self.GBP_MIN_SIZE[1]:
            # Upscale small images
            if aspect >= 1:
                new_width = self.GBP_OPTIMAL_SIZE[0]
                new_height = int(new_width / aspect)
            else:
                new_height = self.GBP_OPTIMAL_SIZE[1]
                new_width = int(new_height * aspect)
        elif width > self.GBP_MAX_SIZE[0] or height > self.GBP_MAX_SIZE[1]:
            # Downscale very large images
            if aspect >= 1:
                new_width = self.GBP_MAX_SIZE[0]
                new_height = int(new_width / aspect)
            else:
                new_height = self.GBP_MAX_SIZE[1]
                new_width = int(new_height * aspect)
        else:
            # Optimize to standard size
            if aspect >= 1:
                new_width = self.GBP_OPTIMAL_SIZE[0]
                new_height = int(new_width / aspect)
            else:
                new_height = self.GBP_OPTIMAL_SIZE[1]
                new_width = int(new_height * aspect)

        # Use high-quality resampling
        return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def _enhance_image(self, img: Image.Image) -> Image.Image:
        """Auto-enhance image quality"""

        # Sharpen slightly
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.1)

        # Boost contrast slightly
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.05)

        # Boost color saturation slightly
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.1)

        return img

    def _blur_background(self, img: Image.Image) -> Image.Image:
        """
        Simple background blur effect
        Note: For proper background removal, use AI models like:
        - rembg (U2-Net)
        - backgroundremover
        - Photoshop/GIMP
        """
        # Apply subtle gaussian blur to entire image
        # In production, you'd segment foreground/background first
        blurred = img.filter(ImageFilter.GaussianBlur(radius=2))

        # Blend original and blurred (simple approach)
        return Image.blend(img, blurred, alpha=0.3)


def create_thumbnail_grid(images: List[str], output_path: str, cols: int = 4):
    """Create a thumbnail grid preview of multiple images"""

    if not images:
        return

    thumb_size = (300, 300)
    gap = 10

    # Load and create thumbnails
    thumbnails = []
    for img_path in images[:16]:  # Max 16 images
        try:
            img = Image.open(img_path)
            img.thumbnail(thumb_size, Image.Resampling.LANCZOS)
            thumbnails.append(img)
        except:
            continue

    if not thumbnails:
        return

    # Calculate grid size
    rows = (len(thumbnails) + cols - 1) // cols
    grid_width = cols * thumb_size[0] + (cols + 1) * gap
    grid_height = rows * thumb_size[1] + (rows + 1) * gap

    # Create white background
    grid = Image.new('RGB', (grid_width, grid_height), (255, 255, 255))

    # Paste thumbnails
    for idx, thumb in enumerate(thumbnails):
        row = idx // cols
        col = idx % cols
        x = col * thumb_size[0] + (col + 1) * gap
        y = row * thumb_size[1] + (row + 1) * gap
        grid.paste(thumb, (x, y))

    grid.save(output_path, 'JPEG', quality=90)
    print(f"📸 Grid preview saved: {output_path}")


def main():
    """Main CLI entry point"""

    parser = argparse.ArgumentParser(
        description='Batch process photos for Google Business Profile'
    )
    parser.add_argument('input', help='Input file or directory')
    parser.add_argument('output', help='Output file or directory')
    parser.add_argument('--enhance', action='store_true', default=True,
                       help='Apply auto-enhancement (default: enabled)')
    parser.add_argument('--resize', action='store_true', default=True,
                       help='Resize to optimal dimensions (default: enabled)')
    parser.add_argument('--format', choices=['JPEG', 'PNG', 'WEBP'],
                       default='JPEG', help='Output format')
    parser.add_argument('--grid', action='store_true',
                       help='Create thumbnail grid preview')

    args = parser.parse_args()

    processor = PhotoProcessor(
        enhance=args.enhance,
        resize=args.resize
    )

    input_path = Path(args.input)
    output_path = Path(args.output)

    # Process single file or batch
    if input_path.is_file():
        # Single file
        if output_path.is_dir():
            output_file = output_path / f"{input_path.stem}_optimized.jpg"
        else:
            output_file = output_path

        processor.process_image(str(input_path), str(output_file), format=args.format)

    elif input_path.is_dir():
        # Batch processing
        success, failed = processor.process_batch(
            str(input_path),
            str(output_path),
            formats=[args.format]
        )

        # Create preview grid
        if args.grid and success > 0:
            images = list(output_path.glob('*_optimized.*'))
            create_thumbnail_grid(
                [str(img) for img in images],
                str(output_path / 'preview_grid.jpg')
            )

    else:
        print(f"❌ Invalid input: {input_path}")
        sys.exit(1)


if __name__ == '__main__':
    main()
