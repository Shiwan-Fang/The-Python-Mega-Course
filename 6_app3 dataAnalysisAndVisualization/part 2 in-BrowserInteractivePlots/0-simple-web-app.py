# if you want to run the page again, you hagve to quit(ctrl+c) first
import justpy as jp


def app():
    wp = jp.QuasarPage()  # create a webpage,QuasarPage is a javascript framework
    # search "quasar style" and you can find all the style
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes="text-h3 text-center q-pa-md")
    # don't forget connect those elements to the webpage a=wp
    pi = jp.QDiv(a=wp, text="These graphs reprensent course review analysis")
    return wp


jp.justpy(app)  # calling this func
