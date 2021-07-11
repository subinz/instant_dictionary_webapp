import justpy as jp


class Home:

    path = "/home"
    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage()
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        poinddgonoasdngoh  obssdgb F BUJSDg knodbf OFPIWrijWEFI WEIBOWBE Oongnoe
        """, classes="text-lg")
        return wp

