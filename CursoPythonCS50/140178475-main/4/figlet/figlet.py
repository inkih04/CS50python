import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

#El formato de entrada es incorrecto
if len(sys.argv) == 2 or len(sys.argv) > 3:
    print("Invalid usage")
    sys.exit(1)
## Caso sin especificar la fuente
if len(sys.argv) == 1:
    txt = input("Input: ")
    print(figlet.renderText(txt))
    sys.exit(0)
if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
    txt = input("Input: ")
    print(figlet.renderText(txt))
    sys.exit(0)
else:
    print("Invalid usage")
    sys.exit(1)
