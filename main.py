from fasthtml.common import *

app,rt = fast_app()

@rt('/change')
def get(): return P('Testing')

@rt('/')
def get():
    return Html(
        Head(
            Script(src="https://unpkg.com/htmx.org@1.9.10")
        ),
        Body(
            Div(
                Div(P('One two three'), id="target"),
                Button("Click Me", hx_get="/change", hx_target="#target", hx_trigger="click")
            )
        )
    )

if __name__ == "__main__":
    serve()