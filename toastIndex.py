from win10toast import ToastNotifier
import webbrowser

toast = ToastNotifier()
notiPermission = True
url = "https://www.friendlywallet.net/cyberpunk2077"
#url = ""

def openBrowser():
    global url
    if not url:
        url = "https://www.friendlywallet.net"

    webbrowser.open(url, 1, True)

if notiPermission == True:
    toast.show_toast("FriendlyWallet", "Cyperpunk 2077 is now ON SALE!",
                     "/resources/python.ico", 5, False, openBrowser)
