import tkinter as tk
from tkinter import ttk
import uuid

class ConferenceRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conference Registration System")
        self.root.geometry("800x600")
        self.root.minsize(1200, 600)  # Set minimum width to 1200 pixels

        self.create_widgets()

    def create_widgets(self):
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Register participants tab
        self.register_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.register_tab, text="Register Participants")

        self.create_register_tab()

        # View participants tab
        self.view_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.view_tab, text="View Participants")

        self.create_view_tab()

    def create_register_tab(self):
        # Label and entry widgets for participant information
        tk.Label(self.register_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(self.register_tab)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.register_tab, text="Institution:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.institution_entry = tk.Entry(self.register_tab)
        self.institution_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.register_tab, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(self.register_tab)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.register_tab, text="Phone Number:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.phone_entry = tk.Entry(self.register_tab)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.register_tab, text="Presentation Title:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.presentation_entry = tk.Entry(self.register_tab)
        self.presentation_entry.grid(row=4, column=1, padx=5, pady=5)

        # Register button
        tk.Button(self.register_tab, text="Register", command=self.register_participant).grid(row=5, columnspan=2, padx=5, pady=10)

    def register_participant(self):
        # Generate unique registration ID
        registration_id = str(uuid.uuid4())

        # Get participant information from entry widgets
        name = self.name_entry.get()
        institution = self.institution_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        presentation = self.presentation_entry.get()

        # Write participant data to file
        with open("registreerimis_andmed.txt", "a") as file:
            file.write(f"{name},{institution},{email},{phone},{presentation},{registration_id}\n")

        # Clear entry fields after registration
        self.name_entry.delete(0, tk.END)
        self.institution_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.presentation_entry.delete(0, tk.END)

        # Provide registration confirmation to the user
        tk.messagebox.showinfo("Registration", "Participant registered successfully!")

    def create_view_tab(self):
        # Label and entry for search
        tk.Label(self.view_tab, text="Search:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.search_entry = tk.Entry(self.view_tab)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.view_tab, text="Search", command=self.search_participants).grid(row=0, column=2, padx=5, pady=5)

        # Treeview widget to display participant data
        self.tree = ttk.Treeview(self.view_tab, columns=("Name", "Institution", "Email", "Phone Number", "Presentation Title", "Registration ID"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Institution", text="Institution")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Phone Number", text="Phone Number")
        self.tree.heading("Presentation Title", text="Presentation Title")
        self.tree.heading("Registration ID", text="Registration ID")
        self.tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.NSEW)

        # Scrollbar for the treeview
        scrollbar = ttk.Scrollbar(self.view_tab, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=1, column=3, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Load all participant data initially
        self.load_participant_data()

        # Change button
        tk.Button(self.view_tab, text="Change", command=self.change_participant_info).grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def load_participant_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Load participant data from file
        with open("registreerimis_andmed.txt", "r") as file:
            for line in file:
                participant_data = line.strip().split(",")
                self.tree.insert("", tk.END, values=participant_data)

    def search_participants(self):
        # Clear existing data
        self.load_participant_data()

        # Get search query
        search_query = self.search_entry.get().lower()

        # Filter participant data based on search query
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if any(search_query in value.lower() for value in values):
                self.tree.selection_set(item)
            else:
                self.tree.detach(item)

    def change_participant_info(self):
        # Get selected participant's data
        selected_item = self.tree.selection()
        if not selected_item:
            tk.messagebox.showwarning("Error", "Please select a participant to change.")
            return

        # Open a new window to change participant's information
        change_window = tk.Toplevel(self.root)
        change_window.title("Change Participant Information")

        # Get participant data
        item = self.tree.item(selected_item)
        participant_data = item['values']

        # Create labels and entry widgets to display participant's information
        labels = ["Name:", "Institution:", "Email:", "Phone Number:", "Presentation Title:", "Registration ID:"]
        for i, label_text in enumerate(labels):
            tk.Label(change_window, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entry = tk.Entry(change_window)
            entry.insert(0, participant_data[i])
            entry.grid(row=i, column=1, padx=5, pady=5)

        # Function to update participant information
        def update_info():
            updated_data = [entry.get() for entry in entry_widgets]
            print("Updated Data:", updated_data)  # Print updated data for debugging
            updated_line = ','.join(updated_data) + '\n'
            updated_registration_id = updated_data[-1]  # Get the updated registration ID
            print("Updated Line:", updated_line)  # Print updated line for debugging
            # Read all lines from file
            with open("registreerimis_andmed.txt", "r") as file:
                lines = file.readlines()
            # Update the participant data in the lines list
            updated_lines = []
            for line in lines:
                participant_data = line.strip().split(",")
                if participant_data[-1] == updated_registration_id:
                    updated_lines.append(updated_line)
                    print("Line Updated")  # Print message when line is updated for debugging
                else:
                    updated_lines.append(line)
            # Write updated lines back to the file
            with open("registreerimis_andmed.txt", "w") as file:
                file.writelines(updated_lines)
            # Close the change window
            change_window.destroy()
            # Reload participant data in the main window
            self.load_participant_data()






        # Button to confirm changes
        tk.Button(change_window, text="Update", command=update_info).grid(row=len(labels), columnspan=2, padx=5, pady=10)

        # Entry widgets for participant data
        entry_widgets = []
        for i in range(len(labels)):
            entry_widgets.append(tk.Entry(change_window))

        # Close button
        tk.Button(change_window, text="Close", command=change_window.destroy).grid(row=len(labels)+1, columnspan=2, padx=5, pady=10)

# Main function to run the application
def main():
    root = tk.Tk()
    app = ConferenceRegistrationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
