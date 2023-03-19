import pyfiglet, sys

figlet = pyfiglet.Figlet()

fonts = figlet.getFonts()

if len(sys.argv) > 2 and sys.argv[1] == '-f' or sys.argv[1] == '--font':
    font_name = str(sys.argv[2])
    if font_name in fonts:
        figlet.setFont(font = font_name)
    else:
        print(f"Error: font '{font_name}' not found.")
    
else:
    print("Error: invalid command line arguments.")
    sys.exit()

text = input('text: ')

result = figlet.renderText(text)

print(result)