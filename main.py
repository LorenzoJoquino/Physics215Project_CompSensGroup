#Demonstration of importing from physics 215 Project Code 
from physics215ProjectCode import testFunction
from physics215ProjectCode import testFunction
text = "Joquino,Lorenzo Gabriel, Palad"
result = testFunction.splitText(text)
print(result)


from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get(): return Div(P(f"Hello World! {testFunction.splitText(text)}"), hx_get="/change")

serve()