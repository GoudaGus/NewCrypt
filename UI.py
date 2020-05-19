from tkinter import *
from tkinter import filedialog
from os import environ
from encrypt import encrypt, decrypt
from digest import encode, decode
# Label, Text, Tk, Button, Entry


class Initial_IO:
    """Create IO."""
    def __init__(self, master):

        def file_explorer():
            filename = filedialog.askopenfilename(initialdir = f"{environ['USERPROFILE']}/Documents",
                                            title = "Select File",
                                            filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))                             
            return filename
            
        def get_file(self):
            self.file_box.insert(0, str(file_explorer()))


        self.master = master
        self.master.title("Encrypt/Decrypt Files")
        self.master['bg'] = '#f2f2f2'
        self.master.geometry("500x200")

        self.file_button = Button(master,
                                text = "Browse Files",
                                command = lambda:get_file(self))
        self.file_button.grid(column=1, row=1, sticky = W)

        self.file_box = Entry(master)
        self.file_box.grid(column = 1, padx = 85, row = 1, sticky = W)

        self.encrypt_button = Button(master,
                                    text = "Encrypt",
                                    command = self.init_encrypt).grid(column = 1, row = 2, pady = 10, padx = 90, sticky = W)

        self.decrypt_button = Button(master,
                                    text = "Decrypt",
                                    command = self.init_decrypt).grid(column = 1, row = 2, pady = 10, padx = 150, sticky = W)

        self.error_label = Label(master, text = "")
        self.error_label.grid(column = 3, row = 1)

        self.output_label = Label(master, text = "Output:")
        self.output_label.grid(column = 1, row = 3, sticky = W)
        self.output_text = Text(master, height = 7, width = 50)
        self.output_text.grid(column = 1, columnspan = 2, pady = 10, row = 3, sticky = W)
        self.output_text_scroll = Scrollbar(master, command = self.output_text.yview)
        self.output_text_scroll.grid(column = 3, row = 3, sticky = W)
        self.output_text.configure(yscrollcommand = self.output_text_scroll.set)

    def write_error(self, error=""):
        self.error_label.configure(text = error)

    def open_file(self, filename, action, contents=None):
        if action == "w":
            try:
                with open(filename, action) as openfile:
                    openfile.write(contents)
                    openfile.close()
            except FileNotFoundError:
                return False
        else:
            try:
                with open(filename, action) as openfile:
                    temp = openfile.read()
                    openfile.close()
                    print(temp)
                    return temp
            except FileNotFoundError:
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
        print(self.save_file_path)
        print(self.file_name)
        # except:
        #     exit()
    
    def init_encrypt(self):
        
        orig_file = self.open_file(self.file_path, "r")
        if orig_file:
            self.get_save_path()
            self.write_error()
            m = encode(str(orig_file))
            output = encrypt(m)
            self.encrypted = output
            self.output_text.insert(END, f"{self.encrypted}")
            self.save_file_path = str(self.save_file_path + self.file_name + "_encrypted.txt")
            self.open_file(self.save_file_path, "w", self.encrypted)
            
        else:
            self.write_error("Error: File not found.")

    def init_decrypt(self):
        self.get_save_path()
        self.write_error()
        self.file_path
        ciph_file = self.open_file(self.file_box.get(), "r")
        temp0 = 0
        temp1 = []
        for i in ciph_file:
            temp0 += 1
            if i == ",":
                temp1.append(temp0)
        c = int(ciph_file[0:temp1[0] - 1])
        d = int(ciph_file[temp1[0] + 1:temp1[1] - 1])
        n = int(ciph_file[temp1[1] + 1:len(ciph_file)])
        ck = (c, (d, n))
        print(ck)
        encoded_text = decrypt(ck)
        plain_text = decode(encoded_text)
        print(plain_text)

        print(c)
        # key1 = False
        # key2 = False
        # temp0 = ""
        # temp1 = ""
        # temp2 = ""

        # for i in self.encrypted:
        #     if i == "," and not key1:
        #         key1 = True
        #     elif i == "," and key1:
        #         key1 == False
        #         key2 = True
        #     if not key1 and not key2 and not i == ",":
        #         temp_m += i
        #     if key1 and not i == ",":
        #         temp_d += i
        #     if key2 and not i == ",":
        #         temp_n += i
        # for i in 
        # self

        # print 
        # temp1 = (temp0, temp1, temp2)
        print(temp1)




        





    
    # def __init__(self, master):
    #     """Initialize IO."""
    #     self.master = master
    #     self.master.title("Encrypt/Decrypt Files")

    #     self.name_Box = Entry(master)
    #     self.name_Box.grid(column=2, row=4)

    #     self.name_Label = Label(text="Name:")
    #     self.name_Label.grid(column=1, row=4)


    #     self.top_Text = Label(master, text="Please select a dog size:")
    #     self.top_Text.grid(column=2, row=1)

    #     self.lg_Button = Button(master, text="Large",
    #                             command=lambda *args: dogtalk(
    #                                                         self, size="large"
    #                                                         ))
    #     self.lg_Button.grid(column=1, row=2)

    #     self.md_Button = Button(master, text="Medium",
    #                             command=lambda *args: dogtalk(
    #                                                         self, size="medium"
    #                                                         ))
    #     self.md_Button.grid(column=2, row=2)

    #     self.sm_Button = Button(master, text="Small",
    #                             command=lambda *args: dogtalk(
    #                                                         self, size="small"
    #                                                         ))
    #     self.sm_Button.grid(column=3, row=2)

    #     self.responce = Label(master)
    #     self.responce.grid(column=2, row=5)

    #     self.goodbye = Label(text="Dog says goodbye")
    #     self.quit = Button(master, text="Quit",
    #                        command=self.quitfun).grid(column=10, row=10)

    #     def dogtalk(self, size):
    #         self.outputdog.config(text=make_Dog(size, self.name_Box.get()))
    #         self.outputdog.grid(column=2, row=6)

    # def quitfun(self):
    #     """Quit program."""
    #     self.outputdog.destroy()
    #     self.goodbye.grid(column=2, row=6)
    #     self.master.after(2000, lambda: self.master.destroy())


def main():
    """Initialize program."""
    root = Tk()
    _ = Initial_IO(root)
    root.mainloop()


if __name__ == "__main__":
    main()