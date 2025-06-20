import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These grapghs represent course review analysis.")
    # jp.Div(text='¡Hola, JustPy!', classes='text-4xl m-2', a=wp)
    return wp

jp.justpy(app)