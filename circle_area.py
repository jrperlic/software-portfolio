import tkinter as tk
import math

class FloatEntry(tk.Entry):
    """An Entry widget that accepts only
    numbers between a lower and upper bound.
    """
    def __init__(self, parent, lower, upper, **kwargs):
        super().__init__(parent)
        if lower > 0:
            lower = 0
        if upper < 0:
            upper = 0
        self.lower = lower
        self.upper = upper
        vcmd = (parent.register(self.validate), "%P")
        if not "justify" in kwargs:
            kwargs["justify"] = "right"
        if not "width" in kwargs:
            kwargs["width"] = max(len(str(lower)), len(str(upper)))
        self.config(validate="key", validatecommand=vcmd, **kwargs)

    def validate(self, value_if_allowed):
        valid = False
        try:
            i = float(value_if_allowed)
            valid = (self.lower <= i and i <= self.upper)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower < 0 and value_if_allowed == "-"))
        return valid

    def get(self):
        """Return the number that the user entered."""
        return float(super().get())

    def set(self, n):
        """Display the number n for the user to see."""
        self.delete(0, tk.END)
        self.insert(0, str(float(n)))

class CircleWindow(tk.Frame):
    """The main window of this application."""

    def __init__(self, parent):
        """Initialize a Frame object."""

        # Call __init__ in the parent class.
        super().__init__(parent)

        # Create a label that displays "Radius:"
        lblRadius = tk.Label(self, text="Radius:")

        # Create a text field where the user will enter the radius.
        txtRadius = FloatEntry(self, 0, 200, width=5)

        # Create a label that displays "Area:"
        lblArea = tk.Label(self, text="Area:")

        # Create a label that will display the output.
        lblOut = tk.Label(self, width=7)

        # Create the Error message.
        lblError = tk.Label(self, text="")

        # Create the Clear button.
        btnClear = tk.Button(self, text="Clear")

        # Layout all the labels, text fields, and buttons in a grid.
        lblRadius.grid(  row=0, column=0, padx=3, pady=2)
        txtRadius.grid(  row=0, column=1, padx=3, pady=2)
        lblArea.grid(row=0, column=2, padx=(30,3), pady=2)
        lblOut.grid( row=0, column=3, padx=3, pady=2)
        lblError.grid(row=1, column=0, padx=3, pady=2)
        btnClear.grid(row=2, column=0, padx=3, pady=2, columnspan=5, sticky="W")

        self.master.title("Circle Area")
        self.grid(padx=3, pady=3)

        # This function is called each time the user releases a key.
        def calc(event):
            """Compute and display the area of the circle."""
            try:
                # Get the radius.
                radius = txtRadius.get()

                # Compute the area.
                area = round(math.pi * radius**2, 2)

                # Display the area.
                lblOut.config(text=str(area))

                # Display no error message.
                lblError.config(text="")

            except ValueError:
                # When the user deletes all the digits in the radius
                # text field, clear the area label.
                lblOut.config(text="")
                lblError.config(text="Error")

        # This function is called each time
        # the user presses the "Clear" button.
        def clear():
            """Clear all the inputs and outputs."""
            txtRadius.delete(0, tk.END)
            lblOut.config(text="")
            lblError.config(text="")
            txtRadius.focus()

        # Bind the calc function to the radius text field so
        # that the calc function will be called when the
        # user changes the text in the text field.
        txtRadius.bind("<KeyRelease>", calc)

        # Bind the clear function to the clear button so
        # that the clear function will be called when the
        # user clicks the clear button.
        btnClear.config(command=clear)

        # Give the keyboard focus to the radius text field.
        txtRadius.focus()

def main():
    try:
        # Create the root Tk object.
        app = tk.Tk()

        # Create a CircleWindow object which will call
        # the __init__ function in the CircleWindow class.
        CircleWindow(app)

        # Start the tkinter loop that processes user events
        # such as key presses and mouse button clicks.
        app.mainloop()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")

# Call the main function so that
# this program will start executing.
main()