import os
import yfinance as yf
from datetime import datetime

tickers = []
start_date = None
end_date = None
interval = None
save_dir = None

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")
    dscr = "Risk Management & Financial Econometrics "
    banner = f"""
{'*' * len(dscr)}
Stefanos Stavrianos, PhD Candidate
{dscr}
University of Patras, GR
www.stefanstavrianos.eu/en
{'*' * len(dscr)}
"""
    print(banner.strip(), end="\n")

def show_exit_message():
    print("Thank you for using the Data Downloader.")
    print("Wishing you accurate data and insightful research!\n")

def download_data():
    clear_screen()
    print("Start downloading...\n")
    for i, symbol in enumerate(tickers, start=1):
        try:
            ticker_obj = yf.Ticker(symbol)
            info = ticker_obj.info
            name = info.get("shortName") or info.get("longName") or "Unknown"
            display_name = name.strip()
            safe_name = name.replace(" ", "_").replace("/", "_").replace(",", "").replace(":", "")
            data = ticker_obj.history(start=start_date, end=end_date, interval=interval)
            safe_symbol = symbol.replace("=", "").replace("^", "")
            filename = f"{safe_name}_{safe_symbol}_{start_date}_to_{end_date}.csv"
            output_path = os.path.join(save_dir, filename)
            os.makedirs(save_dir, exist_ok=True)
            data.to_csv(output_path)
            print(f"{i}) {display_name}... done")
        except Exception as e:
            print(f"{i}) Error with {symbol}: {e}")
    input("\nPress ENTER to return to the main menu...")
    clear_screen()
    print("All data downloaded successfully!\n")

def set_tickers():
    global tickers
    while True:
        clear_screen()
        print("Enter Yahoo Finance codes separated by comma (,)")
        print("Example: GC=F,^GSPC,AAPL")
        user_input = input("Tickers: ")
        tickers = [x.strip() for x in user_input.split(",") if x.strip()]
        if tickers:
            break
        print("\nAt least one ticker required.")
        input("Press ENTER to try again...")

def set_dates():
    global start_date, end_date
    while True:
        clear_screen()
        s = input("Enter START date (DD-MM-YYYY): ")
        e = input("Enter END date (DD-MM-YYYY): ")
        try:
            datetime.strptime(s, "%d-%m-%Y")
            datetime.strptime(e, "%d-%m-%Y")
            start_date = datetime.strptime(s, "%d-%m-%Y").strftime("%Y-%m-%d")
            end_date = datetime.strptime(e, "%d-%m-%Y").strftime("%Y-%m-%d")
            break
        except ValueError:
            print("\nInvalid date format. Use DD-MM-YYYY.")
            input("Press ENTER to try again...")

def set_interval():
    global interval
    while True:
        clear_screen()
        print("Choose interval")
        print("(a) 1d")
        print("(b) 1wk")
        print("(c) 1mo")
        choice = input("Enter option (a/b/c): ").lower()
        if choice == "a":
            interval = "1d"
            break
        elif choice == "b":
            interval = "1wk"
            break
        elif choice == "c":
            interval = "1mo"
            break
        print("\nInvalid choice.")
        input("Press ENTER to try again...")

def set_location():
    global save_dir
    while True:
        clear_screen()
        print("Choose path or leave it empty to save in the same directory as this program")
        path = input("Directory: ").strip()
        save_dir = path if path else os.getcwd()
        if os.path.isdir(save_dir):
            break
        print("\nPath not valid.")
        input("Press ENTER to try again...")

def configuration_complete():
    return all([tickers, start_date, end_date, interval, save_dir])

def handle_incomplete_config():
    clear_screen()
    print("Configuration incomplete. Please set all required fields.\n")
    while True:
        print("(1) Main Menu")
        print("(2) Exit")
        choice = input("\nChoose option: ").strip()
        match choice:
            case "1":
                return
            case "2":
                clear_screen()
                show_exit_message()
                exit()
            case _:
                clear_screen()
                print("Configuration incomplete. Please set all required fields.\n")

def show_menu():
    while True:
        clear_screen()
        title = "Data Downloader"
        border = "=" * max(len(title), 40)
        print(border)
        print(title)
        print(border)
        print("")
        print("(1) Set Tickers")
        print("(2) Set Date Range")
        print("(3) Set Interval")
        print("(4) Set Save Location")
        print("(5) Exit")
        print("")
        config_header = "Configuration Summary "
        border = "-" * max(len(config_header), 40)
        print(border)
        print(config_header)
        print(border)
        print(f"Tickers: {', '.join(tickers) if tickers else 'Not set'}")
        print(f"Start Date: {start_date if start_date else 'Not set'}")
        print(f"End Date: {end_date if end_date else 'Not set'}")
        print(f"Interval: {interval if interval else 'Not set'}")
        print(f"Save Location: {save_dir if save_dir else 'Not set'}")
        print(border)

        choice = input("\nChoose option or press ENTER to download: \n").strip().upper()
        if choice == "":
            choice = "START"
        match choice:
            case "1":
                set_tickers()
            case "2":
                set_dates()
            case "3":
                set_interval()
            case "4":
                set_location()
            case "5":
                clear_screen()
                show_exit_message()
                break
            case "START":
                if configuration_complete():
                    download_data()
                else:
                    clear_screen()
                    handle_incomplete_config()
            case _:
                handle_incomplete_config()

if __name__ == "__main__":
    try:
        show_menu()
    except KeyboardInterrupt:
        clear_screen()
        show_exit_message()
