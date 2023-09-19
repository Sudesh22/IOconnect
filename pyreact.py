from reactpy import component, html, run 

# Define your component
@component
def HelloWorld():
    return html.h1("Hello, World!")

# Run it with a development server. For testing purposes only.
run(HelloWorld)