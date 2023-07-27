# Mandelbrot-Set-Visualizer-in-Python
This is a Python program that visualizes the Mandelbrot set using the Python Imaging Library (PIL). The program generates a Mandelbrot set fractal image and saves it to the specified file location.

# Usage
To run the program, execute the following command:
python3 mandelbrot_visualizer.py

Once the program is running, it will generate a Mandelbrot set image with the specified settings and save it to the specified file location. You can modify the settings of the image by changing the following parameters:

    c: The complex value used as the center of the image.
    w: The complex value used as the width and height of the image.
    px: The number of pixels in the x-axis.
    py: The number of pixels in the y-axis.
    m: The maximum number of iterations used to determine if a point is in the Mandelbrot set.
    out_name: The file name of the image to be saved.

# Mandelbrot Function

The mandelbrot() function takes two arguments, a complex number c and an integer m, and returns an integer that represents the number of iterations required to determine if c is in the Mandelbrot set.

# Sample Funcion
The sample() function takes five arguments, two complex numbers z and w, two integers x and y, and two integers sx and sy. It converts complex numbers to pixels.

# Color Function
The color() function takes two integers i and max_i, and returns a tuple of three integers representing the hue, saturation, and value of the color.

# Render Function
The render_mandelbrot() function takes six arguments, a complex number c, a complex number w, two integers px and py, an integer m, and a string out_name. It renders the Mandelbrot set fractal image and saves it to the specified file location.

# Example Output
Eample Output is example.jpg

# License
This program is licensed under the MIT License. See the LICENSE file for more information.
![example](https://github.com/raphsenn/Mandelbrot-Set-Visualizer-in-Python/assets/88326020/e8af5f44-a834-4149-885c-10b3637374cd)
