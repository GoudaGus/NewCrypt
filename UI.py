# pylint: disable-msg=invalid-name

"""Create GUI element to control encrypt.py."""

from tkinter import *
from tkinter import filedialog
from os import environ
from encrypt import encrypt, decrypt
from digest import encode, decode
# filedialog, Label, Button, Text, Entry, Scrollbar, Tk


class Initial_IO:
    """Create IO."""
    def __init__(self, master):

        def file_explorer():
            filename = filedialog.askopenfilename(
                    initialdir=f"{environ['USERPROFILE']}/Documents",
                    title="Select File",
                    filetypes=(("Text files",
                                "*.txt*"),
                                ("all files",
                                "*.*")))
            return filename
            
        def get_file(self):
            self.file_box.delete(0, END)
            self.file_box.insert(0, str(file_explorer()))

        self.master = master
        self.master.title("Encrypt/Decrypt Files")
        self.master['bg'] = '#f2f2f2'
        self.master.geometry("500x200")

        self.file_button = Button(master,
                                text = "Browse Files",
                                command = lambda:get_file(self))
        self.file_button.grid(
                            column=1,
                            row=1,
                            sticky = "w"
                            )

        self.file_box = Entry(master)
        self.file_box.grid(
                        column = 1,
                        ipadx = 70,
                        padx = 85,
                        row = 1,
                        sticky = "w"
                        )

        self.encrypt_button = Button(master,
                                    text = "Encrypt",
                                    command = self.init_encrypt
                                    )
        self.encrypt_button.grid(
                                column = 1,
                                row = 1,
                                # pady = 10,
                                padx = 360,
                                sticky = "w"
                                )

        self.decrypt_button = Button(master,
                                    text = "Decrypt",
                                    command = self.init_decrypt
                                    )
        self.decrypt_button.grid(
                                column = 1,
                                row = 1,
                                # pady = 10,
                                padx = 415,
                                sticky = "w"
                                )

        self.error_label = Label(master, text = "")
        self.error_label.grid(
                            column = 1,
                            # columnspan = 2,
                            padx = 100,
                            row = 2,
                            sticky = "w"
                            )

        # self.output_label = Label(master, text = "Output:")
        # self.output_label.grid(column = 1, row = 2, sticky = "w")
        self.output_text = Text(master, height = 7, width = 50)
        self.output_text.grid(
                            column = 1,
                            columnspan = 2,
                            pady = 10,
                            padx = 18,
                            row = 3,
                            sticky = "w"
                            )
        self.output_text_scroll = Scrollbar(master, command = self.output_text.yview)
        self.output_text_scroll.grid(column = 1, row = 3, sticky = "w", ipady = 35)
        self.output_text.configure(yscrollcommand = self.output_text_scroll.set)

        self.quit_button = Button(master, text = "Quit", command = lambda: exit())
        self.quit_button.grid(
                            column = 1,
                            # columnspan = 2,
                            row = 3,
                            sticky = "s",
                            pady = 0,
                            padx = 100
                            )

    def write_error(self, error=""):
        self.error_label.configure(text = error)

    def write_output(self, info=""):
        output = f"Output:\n{info}"
        self.output_text.insert(END, str(output))
        

    def open_file(self, filename, action, contents=None):
        if action == "w":
            try:
                with open(filename, action) as openfile:
                    openfile.write(contents)
                    openfile.close()
            except OSError:
                self.write_error("Error: Invalid file location")
                return False
        else:
            try:
                with open(filename, action) as openfile:
                    temp = openfile.read()
                    openfile.close()
                    return temp
            except FileNotFoundError:
                self.write_error("Error: File not found")
                return False
            except OSError:
                self.write_error("Error: Invalid file location")
                return False

    def get_save_path(self):
        self.file_path = self.file_box.get()
        o = 0
        for i in self.file_path[::-1]:
            o += 1
            if i == "/":
                break
        # try:
        self.save_file_path = self.file_path[0:len(self.file_path) - o]
        self.file_name = self.file_path[len(self.file_path) - o:len(self.file_path) - 4]
        # except:
        #     exit()
    
    def init_encrypt(self):
        self.get_save_path()
        orig_file = self.open_file(self.file_path, "r")
        if orig_file:
            self.write_error()
            m = encode(str(orig_file))
            output = encrypt(m)
            self.encrypted = output
            self.write_output(self.encrypted)
            self.save_file_path = str(self.save_file_path + self.file_name + "_encrypted.txt")
            self.open_file(self.save_file_path, "w", self.encrypted)
            self.write_error(f"Successfully encrypted to {self.save_file_path}.")

    def init_decrypt(self):
        self.get_save_path()
        self.write_error()
        ciph_file = self.open_file(self.file_box.get(), "r")
        if ciph_file:
            try:
                contents = [i.strip() for i in ciph_file.split(",")]
                ck = (int(contents[0]), (int(contents[1]), int(contents[2])))
                # temp0 = 0
                # temp1 = []
                # for i in ciph_file:
                #     temp0 += 1
                #     if i == ",":
                #         temp1.append(temp0)
                # c = int(ciph_file[0:temp1[0] - 1])
                # d = int(ciph_file[temp1[0]:temp1[1] - 1])
                # n = int(ciph_file[temp1[1]:len(ciph_file)])
                # ck = (c, (d, n))
                encoded_text = decrypt(ck)
                plain_text = decode(encoded_text)
                decrypted_save_path = self.save_file_path + self.file_name + "_decrypted.txt"

                self.write_output(plain_text)
                self.open_file(decrypted_save_path, "w", plain_text)
                self.write_error(f"Successfully decrypted to {decrypted_save_path}.")
            except IndexError:
                self.write_error("Error: Invalid encrypted file")


def main():
    """Initialize program."""
    root = Tk()
    _ = Initial_IO(root)
    root.mainloop()


if __name__ == "__main__":
    main()
