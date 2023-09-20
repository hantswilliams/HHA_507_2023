---
marp: true
title: Flask-Matplotlib
paginate: true
theme: default
---


# Introduction to Flask with Matplotlib

Flask is a lightweight web framework written in Python. It is ideal for building small web applications, microservices, and APIs.

Matplotlib is a popular visualization library in Python.

Combining Flask with Matplotlib allows you to create dynamic web visualizations easily.

---

# Setting Up Flask

To set up a Flask environment:

```bash
pip install flask
```

Create a simple Flask app:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

---

# Integrating Flask with Matplotlib

To integrate Flask with Matplotlib:

1. Install required libraries:
```bash
pip install flask matplotlib pandas
```

2. Use Matplotlib to generate plots and return them as images.

3. Display images in Flask views.

---

# Example: Binge Drinking Visualization

Load the dataset:

```python
import pandas as pd
url = "https://your_data_url_here.csv"
df = pd.read_csv(url)
```

---

# Creating a Dynamic Plot with Flask & Matplotlib

Filter and visualize the data:

```python
import matplotlib.pyplot as plt
import io
import base64

def create_plot(data):
    # Matplotlib code here
    fig, ax = plt.subplots()
    # ... your plotting logic ...

    # Convert plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return base64.b64encode(img.getvalue()).decode()
```
---

# The Role of `io` and `base64` in Flask Visualizations

When serving dynamic images (like Matplotlib plots) in Flask, we often can't just save the image to disk and reference it. We need a way to:

1. Generate the image in memory.
2. Convert the image to a format that can be easily embedded in a webpage.

This is where `io` and `base64` come into play.

---

# `io.BytesIO()`: Dynamic In-Memory Bytes Buffers

- The `io` module provides Python's main facilities for dealing with various types of I/O.
- `io.BytesIO()` is a class that provides a **buffer** in memory which behaves like a binary file opened in write mode.

```python
img = io.BytesIO()
plt.savefig(img, format='png')
```

Here, we're using Matplotlib's `savefig` to save the plot to this in-memory buffer instead of saving it to disk.

---

# `base64`: Binary-to-Text Encoding

- Web pages can't directly interpret raw binary image data.
- `base64` encoding converts binary data (our image) to a string format which can be embedded in HTML.
  
```python
base64.b64encode(img.getvalue())
```

This code takes our image from the in-memory buffer, encodes it to base64, and gets us a string representation of the image.

---

# `.decode()`: Bytes to String Conversion

- The result of `base64.b64encode()` is in bytes.
- To embed the image in an HTML template, we need it as a string.

```python
base64.b64encode(img.getvalue()).decode()
```

`.decode()` does the conversion from bytes to a UTF-8 string.

---

# Embedding the Image in HTML

With our base64-encoded string, embedding in HTML becomes straightforward:

```html
<img src="data:image/png;base64,{{ img }}" alt="Visualization" />
```

This is known as a **Data URI**. It embeds the image data directly into the document, eliminating the need for an external file.

---

# In Summary

The combination of `io`, `base64`, and `.decode()` allows us to:

1. Create images dynamically in memory.
2. Convert and serve them as embeddable strings in our web pages.

It's a powerful technique for serving dynamic content without the need for static files.

--- 

# Displaying the Plot in Flask

Integrate the plotting function with a Flask route:

```python
from flask import render_template

@app.route('/')
def index():
    img = create_plot(df)
    return render_template("index.html", img=img)
```

Display the image in the HTML template:

```html
<img src="data:image/png;base64,{{ img }}" alt="Visualization" />
```

---

# Benefits of Flask with Matplotlib

1. **Flexibility:** Build custom visualizations tailored to your requirements.
2. **Dynamic Content:** Easily update visualizations based on user input or updated data.
3. **Integration:** Combine with other Python libraries or Flask extensions.
4. **Deployment:** Flask apps can be deployed in various environments, including cloud platforms.

---

# Conclusion

Flask with Matplotlib offers a powerful combination for web-based data visualizations. With a few lines of code, you can build interactive and dynamic visualizations tailored to your needs.

---

You can then use a tool like MARP or another Markdown slide presenter to visualize these slides.