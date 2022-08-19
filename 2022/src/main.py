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
    return tuple[0] + tuple[1]/60 + tuple[2]/3600

def imageToGpsPoint(image):
    f1 = convertTodecimale(image.gps_latitude)
    f2 = convertTodecimale(image.gps_longitude)
    if image.gps_latitude_ref == "S":
        f1 = -abs(f1)
    if image.gps_longitude_ref == "W":
        f2 = -abs(f2)
    return (f1, f2)

def listeAvantMidi(liste):
    avantmidi = []
    for i in liste:
        if int(openImage("photo.jpg").datetime[11:13]) < 12:
            avantmidi.append(i)
    return avantmidi




my_image = openImage("photo.jpg")
photo_liste = ["photo.jpg"]

