# LED-Matrix-Bitcoin-Ticker
This project fetches the current value of Bitcoin in various currencies and displays it on a 64x32 matrix display. It's designed to run on the Metro M4 Airlift with an RGB Matrix shield.

## Features:
- Display Bitcoin value in USD, EUR, or GBP.
- Data fetched from CoinDesk API.
- Smooth scrolling of the Bitcoin value on the matrix display.

## Prerequisites:

- Hardware:
  - Metro M4 Airlift
  - RGB Matrix shield
  - 64x32 matrix display
  
- Libraries:
  - `time`
  - `board`
  - `terminalio`
  - `adafruit_matrixportal`

## Quick Start:

1. Ensure you have all the prerequisites installed and set up.
2. Clone/download this repository.
3. Update `CURRENCY` variable in the script if you wish to change from the default USD to EUR or GBP.
4. Run the script on your Metro M4 Airlift with the display connected.

## Configuration:

- `CURRENCY`: Change this variable's value to "USD", "EUR", or "GBP" depending on which currency you want to display the Bitcoin value in.
- `SCROLL_DELAY`: Adjust the speed of the scrolling text. A smaller value will make the text scroll faster.
  
## Acknowledgments:

- Data is fetched from [CoinDesk API](https://www.coindesk.com/coindesk-api).
- Special thanks to [Adafruit](https://www.adafruit.com/) for their libraries and portions of the code.
