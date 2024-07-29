import tkinter as tk  # Import tkinter as tk for consistency
import currencyapicom

client = currencyapicom.Client('cur_live_HHixRkKnXvmIkvzgBWyutpw8zVbQT2QoslX1ZZgu')

def get_info():
    # Fetch data from API
    status = client.status()
    currencies = client.currencies(currencies=['EUR', 'CAD'])
    rate = client.latest()

    # Create Tkinter window
    root = tk.Tk()
    root.title("Currency Converter")
    root.configure(bg='light grey')

    # Create Tkinter variables to hold data
    status_var = tk.StringVar(value=str(status))
    currencies_var = tk.StringVar(value=str(currencies))
    rate_var = tk.StringVar(value=str(rate))

    # Display data using labels
    tk.Label(root, text="Status :", bg="light grey").grid(row=2, sticky=tk.W)
    tk.Label(root, textvariable=status_var, bg="light grey").grid(row=2, column=1, sticky=tk.W)

    tk.Label(root, text="Currencies :", bg="light grey").grid(row=5, sticky=tk.W)
    tk.Label(root, textvariable=currencies_var, bg="light grey").grid(row=5, column=1, sticky=tk.W)

    tk.Label(root, text="Rate of time :", bg="light grey").grid(row=6, sticky=tk.W)
    tk.Label(root, textvariable=rate_var, bg="light grey").grid(row=6, column=1, sticky=tk.W)

    root.mainloop()

# Create the main window and button
main_window = tk.Tk()
main_window.title("Main Window")

tk.Button(main_window, text="Show Currency Info", command=get_info, bg="White").pack()

main_window.mainloop()
