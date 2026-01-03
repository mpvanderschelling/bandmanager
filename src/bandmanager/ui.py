from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from .documents import Contract, Invoice, Quotation
from .gig import Gig, create_id
from .io import open_json, save_json

NUMBER_OF_LISTITEMS = 5


def create_variables(number_of_listitems: int) -> dict:
    variables = {
        "id": tk.StringVar(),
        "gig_name": tk.StringVar(),
        "name": tk.StringVar(),
        "email": tk.StringVar(),
        "address": tk.StringVar(),
        "zipcode": tk.StringVar(),
        "date": tk.StringVar(),
        "location": tk.StringVar(),
        "starting_time": tk.StringVar(),
        "duration": tk.StringVar(),
        "full_setup": tk.BooleanVar(),
        "dj_set": tk.BooleanVar(),
        "dj_furniture": tk.BooleanVar(),
    }

    variables["id"].set(create_id())

    for i in range(1, number_of_listitems + 1):
        variables[f"listitem_{i}_quantity"] = tk.IntVar()
        variables[f"listitem_{i}_description"] = tk.StringVar()
        variables[f"listitem_{i}_price"] = tk.DoubleVar()

        variables[f"listitem_{i}_quantity"].set(1)

    return variables


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x1200")
        self.root.title("De Klittenband Manager")

        self.main_panel = tk.Frame(self.root)
        self.main_panel.columnconfigure(0, weight=1)
        self.main_panel.pack(fill=tk.BOTH, expand=True)

        self.v = create_variables(NUMBER_OF_LISTITEMS)

        self.v["listitem_1_description"].set("De Klittenband show")
        self.v["listitem_2_description"].set("Licht- en geluidstechniek")

        # ID Section
        # ID Section
        self.create(
            "ID",
            self.v["id"],
            ("Genereer", self.generate_id),
            ("Open", self.open_id),
            ("Clear", self.clear_all_variables),
            root=self.main_panel,
        )

        self.create("Naam van gig:", self.v["gig_name"], root=self.main_panel)

        # Opdrachtgever Section
        self.create_title("Opdrachtgever", root=self.main_panel)

        self.create(
            "Naam opdrachtgever:", self.v["name"], root=self.main_panel
        )
        self.create("E-mail:", self.v["email"], root=self.main_panel)
        self.create(
            "Straatnaam en nummer:", self.v["address"], root=self.main_panel
        )
        self.create(
            "Postcode en plaats:", self.v["zipcode"], root=self.main_panel
        )

        # Show Section
        self.create_title("Show", root=self.main_panel)

        self.create("Datum:", self.v["date"], root=self.main_panel)
        self.create("Locatie:", self.v["location"], root=self.main_panel)
        self.create(
            "Begintijd:", self.v["starting_time"], root=self.main_panel
        )
        self.create("Duur van show:", self.v["duration"], root=self.main_panel)

        # Techniek Section
        self.create_title("Techniek", root=self.main_panel)

        self.create(
            "Volledige setup:",
            self.v["full_setup"],
            "DJ-set:",
            self.v["dj_set"],
            "DJ meubel:",
            self.v["dj_furniture"],
            root=self.main_panel,
        )

        # Prijsopgave Section
        self.create_title("Prijsopgave", root=self.main_panel)

        self.create("Aantal", "Omschrijving", "Prijs", root=self.main_panel)

        for i in range(1, NUMBER_OF_LISTITEMS + 1):
            self.create(
                self.v[f"listitem_{i}_quantity"],
                self.v[f"listitem_{i}_description"],
                self.v[f"listitem_{i}_price"],
                root=self.main_panel,
            )

        # Action Buttons
        self.create(
            ("Offerte", self.make_quotation),
            ("Contract", self.make_contract),
            ("Factuur", self.make_invoice),
            ("Opslaan", self.submit_form),
            root=self.main_panel,
        )

    def open_id(self):
        info_dict = open_json(self.v["id"].get())
        self.set_variables_from_dict(info_dict)
        print(f"Open ID: {self.v['id'].get()}")

    def generate_id(self):
        self.v["id"].set(create_id())

    def run(self):
        self.root.mainloop()

    def create_title(self, title: str, root: tk.Widget):
        label = ttk.Label(root, text=title, font=("Helvetica", 16, "bold"))
        label.pack(padx=5, pady=5)

    def create(self, *entries: str | tk.Variable | None, root: tk.Widget):
        frame = tk.Frame(root)
        for index, entry_data in enumerate(entries):
            frame.columnconfigure(index, weight=1)
            if entry_data is None:
                continue

            if isinstance(entry_data, (str | ttk.Label)):
                widget = ttk.Label(
                    frame, text=entry_data, width=20, font=("Helvetica", 12)
                )
            elif any(
                isinstance(entry_data, dtype)
                for dtype in [tk.DoubleVar | tk.StringVar | tk.IntVar]
            ):
                widget = ttk.Entry(
                    frame,
                    textvariable=entry_data,
                    width=20,
                    font=("Helvetica", 12),
                )
            elif isinstance(entry_data, tk.BooleanVar):
                widget = ttk.Checkbutton(frame, variable=entry_data)
            elif isinstance(entry_data, tuple):  # Button
                widget = ttk.Button(
                    frame, text=entry_data[0], command=entry_data[1]
                )

            widget.grid(
                row=0, column=index, padx=5, pady=2, sticky=tk.W + tk.E
            )

        frame.pack(fill=tk.X, pady=1)

    def submit_form(self) -> dict:
        info_dict = {
            "gig_name": self.v["gig_name"].get(),
            "id": self.v["id"].get(),
            "show": {
                "location": self.v["location"].get(),
                "date": self.v["date"].get(),
                "starting_time": self.v["starting_time"].get(),
                "duration": self.v["duration"].get(),
            },
            "client": {
                "name": self.v["name"].get(),
                "email": self.v["email"].get(),
                "address": self.v["address"].get(),
                "zipcode": self.v["zipcode"].get(),
            },
            "technical_specs": {
                "full_setup": self.v["full_setup"].get(),
                "dj_set": self.v["dj_set"].get(),
                "dj_furniture": self.v["dj_furniture"].get(),
            },
            "line_items": [
                {
                    "quantity": self.v["listitem_1_quantity"].get(),
                    "description": self.v["listitem_1_description"].get(),
                    "price": int(self.v["listitem_1_price"].get() * 100),
                },
                {
                    "quantity": self.v["listitem_2_quantity"].get(),
                    "description": self.v["listitem_2_description"].get(),
                    "price": int(self.v["listitem_2_price"].get() * 100),
                },
                {
                    "quantity": self.v["listitem_3_quantity"].get(),
                    "description": self.v["listitem_3_description"].get(),
                    "price": int(self.v["listitem_3_price"].get() * 100),
                },
                {
                    "quantity": self.v["listitem_4_quantity"].get(),
                    "description": self.v["listitem_4_description"].get(),
                    "price": int(self.v["listitem_4_price"].get() * 100),
                },
                {
                    "quantity": self.v["listitem_5_quantity"].get(),
                    "description": self.v["listitem_5_description"].get(),
                    "price": int(self.v["listitem_5_price"].get() * 100),
                },
            ],
        }

        print(info_dict)
        save_json(info_dict)

        return info_dict

    def make_quotation(self):
        gig = Gig.from_dict(self.submit_form())
        Quotation(gig=gig).run()

    def make_contract(self):
        gig = Gig.from_dict(self.submit_form())
        Contract(gig=gig).run()

    def make_invoice(self):
        gig = Gig.from_dict(self.submit_form())
        Invoice(gig=gig).run()

    def clear_all_variables(self):
        for var in self.v.values():
            if isinstance(var, tk.StringVar):
                var.set("")
            elif isinstance(var, tk.BooleanVar):
                var.set(False)
            elif isinstance(var, tk.IntVar):
                var.set(1)
            elif isinstance(var, tk.DoubleVar):
                var.set(0.0)

    def set_variables_from_dict(self, info_dict):
        self.v["gig_name"].set(info_dict.get("gig_name", ""))
        self.v["id"].set(info_dict.get("id", ""))
        self.v["location"].set(info_dict.get("show", {}).get("location", ""))
        self.v["date"].set(info_dict.get("show", {}).get("date", ""))
        self.v["starting_time"].set(
            info_dict.get("show", {}).get("starting_time", "")
        )
        self.v["duration"].set(info_dict.get("show", {}).get("duration", ""))
        self.v["name"].set(info_dict.get("client", {}).get("name", ""))
        self.v["email"].set(info_dict.get("client", {}).get("email", ""))
        self.v["address"].set(info_dict.get("client", {}).get("address", ""))
        self.v["zipcode"].set(info_dict.get("client", {}).get("zipcode", ""))
        self.v["full_setup"].set(
            info_dict.get("technical_specs", {}).get("full_setup", False)
        )
        self.v["dj_set"].set(
            info_dict.get("technical_specs", {}).get("dj_set", False)
        )
        self.v["dj_furniture"].set(
            info_dict.get("technical_specs", {}).get("dj_furniture", False)
        )

        # Update line items
        line_items = info_dict.get("line_items", [])
        self.set_line_item_vars(line_items)

    def set_line_item_vars(self, line_items):
        for i in range(1, NUMBER_OF_LISTITEMS + 1):
            line_item = line_items[i - 1] if i - 1 < len(line_items) else {}
            self.v[f"listitem_{i}_quantity"].set(line_item.get("quantity", 0))
            self.v[f"listitem_{i}_description"].set(
                line_item.get("description", "")
            )
            self.v[f"listitem_{i}_price"].set(line_item.get("price", 0) / 100)


if __name__ == "__main__":
    ui = UI()
    ui.run()
