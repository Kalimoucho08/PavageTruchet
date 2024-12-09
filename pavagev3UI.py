import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
import random

def createImg(bg_color, fg_color, border_color, size, mode):
    nsize = size * 10
    thickness = 2 * 10
    imres = Image.new('RGB', (nsize, nsize), bg_color)
    draw = ImageDraw.Draw(imres)
    draw.ellipse((-nsize / 2, -nsize / 2, nsize / 2 + thickness, nsize / 2 + thickness), fill=(border_color))
    draw.ellipse((-nsize / 2 + thickness, -nsize / 2 + thickness, (nsize / 2) - thickness, (nsize / 2) - thickness), fill=(fg_color))
    draw.ellipse((nsize / 2 - thickness, nsize / 2 - thickness, nsize + nsize / 2, nsize + nsize / 2), fill=(border_color))
    draw.ellipse((nsize / 2 + thickness, nsize / 2 + thickness, (nsize + nsize / 2) - thickness, (nsize + nsize / 2) - thickness), fill=(fg_color))
    if mode == 2:
        imres = imres.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    imres = imres.resize((size, size), Image.Resampling.LANCZOS)
    return imres

def generate_image():
    Nbre = int(entry_nbre.get())
    taille = int(entry_taille.get())
    seed = int(entry_seed.get())
    colorborder = tuple(map(int, entry_colorborder.get().split(',')))
    colorfront = tuple(map(int, entry_colorfront.get().split(',')))
    colorback = tuple(map(int, entry_colorback.get().split(',')))

    random.seed(seed)
    tailleImage = taille * Nbre
    new_im = Image.new('RGB', (tailleImage, tailleImage))

    im1 = createImg(colorfront, colorback, colorborder, taille, 1)
    im2 = createImg(colorback, colorfront, colorborder, taille, 1)
    im3 = createImg(colorfront, colorback, colorborder, taille, 2)
    im4 = createImg(colorback, colorfront, colorborder, taille, 2)

    for y in range(0, Nbre):
        for x in range(0, Nbre):
            if (x + y) % 2 == 1:
                if random.randint(0, 100) >= 50:
                    im = im1
                else:
                    im = im4
            else:
                if random.randint(0, 100) >= 50:
                    im = im2
                else:
                    im = im3
            new_im.paste(im, (x * taille, y * taille, x * taille + taille, y * taille + taille))

    global img_tk
    img_tk = ImageTk.PhotoImage(new_im)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

def save_image():
    if 'img_tk' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            new_im.save(file_path, "PNG")

app = tk.Tk()
app.title("Générateur de Pavage Truchet")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Nombre de carrés en ligne et en colonne:").grid(row=0, column=0, sticky=tk.W)
entry_nbre = tk.Entry(frame)
entry_nbre.grid(row=0, column=1)
entry_nbre.insert(0, "11")

tk.Label(frame, text="Taille du carré Truchet en pixels:").grid(row=1, column=0, sticky=tk.W)
entry_taille = tk.Entry(frame)
entry_taille.grid(row=1, column=1)
entry_taille.insert(0, "65")

tk.Label(frame, text="Seed:").grid(row=2, column=0, sticky=tk.W)
entry_seed = tk.Entry(frame)
entry_seed.grid(row=2, column=1)
entry_seed.insert(0, "10")

tk.Label(frame, text="Couleur de la bordure (R,G,B):").grid(row=3, column=0, sticky=tk.W)
entry_colorborder = tk.Entry(frame)
entry_colorborder.grid(row=3, column=1)
entry_colorborder.insert(0, "255,255,255")

tk.Label(frame, text="Couleur de l'avant-plan (R,G,B):").grid(row=4, column=0, sticky=tk.W)
entry_colorfront = tk.Entry(frame)
entry_colorfront.grid(row=4, column=1)
entry_colorfront.insert(0, "255,221,221")

tk.Label(frame, text="Couleur de l'arrière-plan (R,G,B):").grid(row=5, column=0, sticky=tk.W)
entry_colorback = tk.Entry(frame)
entry_colorback.grid(row=5, column=1)
entry_colorback.insert(0, "221,221,255")

generate_button = tk.Button(frame, text="Générer l'image", command=generate_image)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

save_button = tk.Button(frame, text="Sauvegarder l'image", command=save_image)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

canvas = tk.Canvas(app, width=715, height=715)
canvas.pack(padx=10, pady=10)

app.mainloop()
