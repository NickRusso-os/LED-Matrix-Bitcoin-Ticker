# Run on Metro M4 Airlift w RGB Matrix shield and 64x32 matrix display
# show current value of Bitcoin in USD

import time
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal

# You can display in 'GBP', 'EUR' or 'USD'
CURRENCY = "USD"
# Set up where we'll be fetching data from
DATA_SOURCE = "https://api.coindesk.com/v1/bpi/currentprice.json"
DATA_LOCATION = ["bpi", CURRENCY, "rate_float"]

def text_transform(val):
    if CURRENCY == "USD":
        return "Bitcoin:$%s" % val
    if CURRENCY == "EUR":
        return "€%d" % val
    if CURRENCY == "GBP":
        return "£%d" % val
    return "%d" % val



# the current working directory (where this file is)
#cwd = ("/" + __file__).rsplit("/", 1)[0]

matrixportal = MatrixPortal(
    url=DATA_SOURCE,
    json_path=DATA_LOCATION,
    status_neopixel=board.NEOPIXEL,
    debug=False,

)
SCROLL_DELAY = .01
matrixportal.add_text(

    text_font=terminalio.FONT,
    text_position=(0, 16),
    text_color=0xFFD700,
    text_transform=text_transform,
    text_scale=3,
    scrolling=True,

)


matrixportal.preload_font(b"$012345789")  # preload numbers
matrixportal.preload_font((0x00A3, 0x20AC))  # preload gbp/euro symbol


last_check = None
while True:
    if last_check is None or time.monotonic() > last_check:
        try:
            value = matrixportal.fetch()
            print("Response is", value)
            last_check = time.monotonic()
        except (ValueError, RuntimeError) as e:
            print("Some error occured, retrying! -", e)
        matrixportal.scroll_text(SCROLL_DELAY) # Scroll the scrollable text block
        time.sleep(.03) # update every .3 seconds
