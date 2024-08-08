from PIL import Image, ImageFilter
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def load_image(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        console.print(Panel(f"Error loading image: {e}", style="red"))
        return None

def save_image(image, path):
    try:
        image.save(path)
        console.print(Panel(f"Image saved to {path}", style="green"))
    except Exception as e:
        console.print(Panel(f"Error saving image: {e}", style="red"))

def apply_grayscale(image):
    return image.convert("L")

def apply_blur(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))

def rotate_image(image, angle):
    return image.rotate(angle, expand=True)

def resize_image(image, width, height):
    return image.resize((width, height))

def show_menu():
    options = {
        "1": "Grayscale",
        "2": "Blur",
        "3": "Rotate",
        "4": "Resize",
        "5": "Save Image",
        "6": "Exit"
    }
  
    console.print(Panel("Image Manipulation Tool", style="bold blue", title="Menu", title_align="left"))
    for key, value in options.items():
        console.print(f"[bold magenta]{key}[/bold magenta]: {value}")
    return Prompt.ask("Choose an option", choices=list(options.keys()), default="6")

def main():
    image_path = Prompt.ask("Enter the path to the image")
    image = load_image(image_path)
  
    if not image:
        return
    
    while True:
        choice = show_menu()
        if choice == "1":
            image = apply_grayscale(image)
            console.print(Panel("Applied grayscale filter", style="cyan"))
          
        elif choice == "2":
            radius = int(Prompt.ask("Enter blur radius", default="2"))
            image = apply_blur(image, radius)
            console.print(Panel(f"Applied blur filter with radius {radius}", style="cyan"))
          
        elif choice == "3":
            angle = int(Prompt.ask("Enter rotation angle", default="90"))
            image = rotate_image(image, angle)
            console.print(Panel(f"Rotated image by {angle} degrees", style="cyan"))
          
        elif choice == "4":
            width = int(Prompt.ask("Enter new width", default="800"))
            height = int(Prompt.ask("Enter new height", default="600"))
            image = resize_image(image, width, height)
            console.print(Panel(f"Resized image to {width}x{height}", style="cyan"))
          
        elif choice == "5":
            save_path = Prompt.ask("Enter the path to save the image")
            save_image(image, save_path)
          
        elif choice == "6":
            console.print(Panel("Goodbye!", style="bold green"))
            break

if __name__ == "__main__":
    main()
