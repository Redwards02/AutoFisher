import pyautogui
from PIL import ImageGrab
import time

def get_pixel_color(x, y):
    # Capture the screen at the specified coordinates
    screen = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    # Get the color of the pixel
    return screen.getpixel((0, 0))

def is_significant_change(old_color, new_color, tolerance=30):
    # Calculate the absolute difference in RGB values
    r_diff = abs(old_color[0] - new_color[0])
    g_diff = abs(old_color[1] - new_color[1])
    b_diff = abs(old_color[2] - new_color[2])
    # Check if any of the differences exceed the tolerance
    return r_diff > tolerance or g_diff > tolerance or b_diff > tolerance

# Coordinates of the pixel you want to monitor
x, y = 960, 540

# Wait for 7 seconds before starting
print("Waiting for 7 seconds before starting...")
time.sleep(7)

# Get the initial color of the pixel
initial_color = get_pixel_color(x, y)
print(f"Initial color: {initial_color}")

while True:
    # Get the current color of the pixel
    current_color = get_pixel_color(x, y)

    # Check if the color has changed significantly
    if current_color != initial_color and is_significant_change(initial_color, current_color):
        print(f"Color changed from {initial_color} to {current_color}")

        # Perform the first right-click at the current mouse position
        current_mouse_position = pyautogui.position()  # Get the current mouse position
        pyautogui.click(current_mouse_position, button='right')
        print("Performed first right-click")

        # Wait for 2 seconds and perform the second right-click at the same position
        time.sleep(2)
        pyautogui.click(current_mouse_position, button='right')
        print("Performed second right-click")

        # Wait for 2 seconds before checking again
        time.sleep(2)

        # Update the initial color to the new color
        initial_color = get_pixel_color(x, y)
        print(f"Updated initial color to: {initial_color}")

    # Wait for 2 seconds before checking again
    #time.sleep(2)
