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
    dscr = "Risk Management & Financial Econometrics"
    print("*"*len(dscr))
    print("Stefanos Stavrianos, PhD Candidate")
    print(dscr)
    print("University of Patras")
    print("website: www.stefanstavrianos.eu/en")
    print("*"*len(dscr))
    print("")
 
def download_data():
    for symbol in tickers:
        try:
            print(f"Downloading {symbol}...")
            data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
            safe_symbol = symbol.replace("=", "").replace("^", "")
            filename = f"{safe_symbol}_{start_date}_to_{end_date}.csv"
            output_path = os.path.join(save_dir, filename)
            os.makedirs(save_dir, exist_ok=True)
            data.to_csv(output_path)
            print(f"Saved to {output_path}")
        except Exception as e:
            print(f"Error with {symbol}: {e}")
    input("\nPress ENTER to continue...")
    clear_screen()
    print("All data downloaded successfully!\n")
 
def set_tickers():
    clear_screen()
    print("Enter Yahoo Finance codes separated by comma (,)")
    print('Example: GC=F,^GSPC,AAPL')
    user_input = input("Tickers: ")
    global tickers
    tickers = [x.strip() for x in user_input.split(",") if x.strip()]
 
def set_dates():
    global start_date, end_date
    clear_screen()
    try:
        s = input("Enter START date (DD-MM-YYYY): ")
        e = input("Enter END date (DD-MM-YYYY): ")
        datetime.strptime(s, "%d-%m-%Y")
        datetime.strptime(e, "%d-%m-%Y")
        start_date = datetime.strptime(s, "%d-%m-%Y").strftime("%Y-%m-%d")
        end_date = datetime.strptime(e, "%d-%m-%Y").strftime("%Y-%m-%d")
    except ValueError:
        clear_screen()
        print("Invalid date format. Use DD-MM-YYYY.\n")
        input("Press ENTER to return to menu...")
 
def set_interval():
    global interval
    clear_screen()
    print("Choose interval:")
    print("(a) 1d")
    print("(b) 1wk")
    print("(c) 1mo")
    choice = input("Enter option (a/b/c): ").lower()
    if choice == "a":
        interval = "1d"
    elif choice == "b":
        interval = "1wk"
    elif choice == "c":
        interval = "1mo"
    else:
        clear_screen()
        print("Invalid interval format.\n")
        input("Press ENTER to return to menu...")
 
def set_location():
    global save_dir
    clear_screen()
    print("Choose path or leave it empty to save in the same directory as this program")
    path = input("Directory: ").strip()
    save_dir = path if path else os.getcwd()
 
def configuration_complete():
    return all([tickers, start_date, end_date, interval, save_dir])
 
def handle_incomplete_config():
    clear_screen()
    print("Configuration incomplete. Please set all required fields.\n")
    while True:
        print("(1) Main Menu")
        print("(2) Exit")
        choice = input("\nChoose option: ").strip()
        if choice == "1":
            return
        elif choice == "2":
            print("Exiting.")
            exit()
        else:
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
        choice = input("\nChoose option or type START: ").strip().upper()
        if choice == "1":
            set_tickers()
        elif choice == "2":
            set_dates()
        elif choice == "3":
            set_interval()
        elif choice == "4":
            set_location()
        elif choice == "5":
            clear_screen()
            print("Thank you for using the Data Downloader.")
            print("Wishing you accurate data and insightful research!\n")
            break
        elif choice == "START":
            if configuration_complete():
                download_data()
            else:
                clear_screen()
                handle_incomplete_config()
        else:
        	handle_incomplete_config()
 
if __name__ == "__main__":
    show_menu()
