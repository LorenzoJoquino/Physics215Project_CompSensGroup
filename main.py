from fasthtml.common import *
import numpy as np

app, rt = fast_app()

@rt
def get():
    return Div(P("Hello World"), hx_get="/change")

serve()