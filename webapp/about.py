import justpy as jp
from webapp import layout, page


class About(page.Page):
    path = "/about"

    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage()

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        A web app that lets users type in a term in a text box and returns the English definition
        of that term instantly as soon as the user has finished typing.
        The web app consists of a website with a navigation menu, a Home, Dictionary, and About page.
        """, classes="text-lg")
        return wp
