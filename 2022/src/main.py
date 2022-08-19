from exif import Image
import folium

def placeDuPoint(filename):
    place = 0
    for i in str(filename):
        if i == '.':
            return place
        place += 1
    print("Sélectionnez un fichier")

def coupeExtension(filename):
    """
    Les chaînes de caractères qui commencent par '.' sont exclues
    """
    removed = ""
    for i in str(filename):
        if i == '.':
            return removed
        removed += i
    print("Sélectionnez un fichier")

def jpgTohtml(image):
    extension = image[placeDuPoint(image) :]
    html = ""
    extensions = [".jpg", ".jpeg", ".jpe",".jif", ".jfif", ".jfi"]
    for i in extensions:
        if  i == extension:
            html = coupeExtension(image) + ".html"
            return html
    print("Sélectionnez une image")

def openImage(nom): #nom est une chaîne de caractères qui représente ici une photo
    with open(nom, 'rb') as imageFile:
        return Image(imageFile)
    imageFile.close()

def convertTodecimale(tuple):
    """
    entrée: tuple(degré, minutes, secondes)
    sortie: flottant
    """

    pass



my_image = openImage("photo.jpg")
print(my_image.gps_longitude)

