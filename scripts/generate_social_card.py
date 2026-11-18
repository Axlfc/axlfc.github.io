"""Generate the 1200x630 original Axlfc social preview; not a product screenshot."""
import argparse
import base64
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'axlfc-social.png'

def font(size, bold):
    names = [
        f'/usr/share/fonts/truetype/dejavu/DejaVuSans{"-Bold" if bold else ""}.ttf',
        f'/usr/share/fonts/truetype/liberation2/LiberationSans-{"Bold" if bold else "Regular"}.ttf',
    ]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    raise FileNotFoundError('DejaVu Sans or Liberation Sans font required')

def create():
    img = Image.new('RGB', (1200, 630), '#faf9f6')
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 1199, 14), fill='#ad4f35')
    draw.text((82, 71), 'axlfc.', font=font(38, True), fill='#ad4f35')
    draw.text((82, 198), 'Axel Fernández', font=font(80, True), fill='#1c292f')
    draw.text((82, 305), 'Curros.', font=font(80, True), fill='#ad4f35')
    draw.text((85, 432), 'Desarrollo web · software · sistemas', font=font(30, False), fill='#58676b')
    draw.line((82, 554, 1117, 554), fill='#ccd2d0', width=2)
    draw.text((83, 574), 'Portafolio técnico y creativo   /   axlfc.github.io',
              font=font(20, False), fill='#58676b')
    img.quantize(colors=16, method=Image.Quantize.FASTOCTREE).save(OUT, optimize=True, compress_level=9)
    return OUT

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--emit-base64', action='store_true')
    options = args.parse_args()
    path = create()
    print(f'OG card: {path.stat().st_size} bytes / 1200x630')
    if options.emit_base64:
        print('AXLFC_SOCIAL_BEGIN')
        print(base64.b64encode(path.read_bytes()).decode('ascii'))
        print('AXLFC_SOCIAL_END')
