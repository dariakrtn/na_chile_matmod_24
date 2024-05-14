import svgwrite
import cairosvg
from PIL import Image
import io


def svg_to_gif(svg_strings, gif_output):
    frames = []

    for svg_string in svg_strings:
        # Convert SVG string to PNG bytes
        png_bytes = cairosvg.svg2png(bytestring=svg_string.encode('utf-8'))

        # Convert PNG bytes to PIL Image
        png_image = Image.open(io.BytesIO(png_bytes))
        frames.append(png_image)

    # Save frames as GIF
    frames[0].save(gif_output, save_all=True, append_images=frames, loop=0, duration=1000)


# Example usage
# svg_strings = list(svg_cadr[2].items())[0][1]
# print(list(svg_cadr[2].items())[0])
# output_gif = "output.gif"
# svg_to_gif(svg_strings, output_gif)

# Для установски cairsvg
# sudo apt-get update
# sudo apt-get install libcairo2
# pip install CairoSVG