import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image
from io import BytesIO

size_px = 3000
dpi = 300
fig_size_in = size_px / dpi

fig = plt.figure(figsize=(fig_size_in, fig_size_in), dpi=dpi)
ax = plt.axes([0, 0, 1, 1])
ax.set_aspect('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

circle = Circle((0.5, 0.5), 0.42, fill=False, edgecolor='black', linewidth=0.01 * size_px)
ax.add_patch(circle)

ax.text(0.5, 0.5, 'a', fontsize=0.25 * size_px, fontname='DejaVu Serif',
        ha='center', va='center', color='black')

buf = BytesIO()
fig.savefig(buf, format='png', dpi=dpi, facecolor='white', bbox_inches=None, pad_inches=0)
plt.close(fig)

buf.seek(0)
img = Image.open(buf).convert('L')
bw = img.point(lambda p: 255 if p > 128 else 0, mode='1')
bw = bw.resize((3000, 3000))
bw.save('pfp.png')
