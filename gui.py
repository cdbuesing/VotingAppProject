from tkinter import *
import logic


class GUI:
    def __init__(self, window):
        self.window = window

        ## Frame to hold pages
        self.container = Frame(self.window)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        ## empty list to hold pages
        self.frames = list()

        ## Frame to hold the voting page frames
        self.frame_voting = Frame(self.container)

        ## Frame and label for the title section
        self.frame_title = Frame(self.frame_voting)
        self.label_title = Label(self.frame_title, text="VOTING APPLICATION")
        self.label_title.pack(side="top")
        self.frame_title.pack(padx=10, pady=10)

        ## Frame, label, and entry box for the id input section
        self.frame_id = Frame(self.frame_voting)
        self.label_id = Label(self.frame_id, text="ID")
        self.entry_id = Entry(self.frame_id)
        self.label_id.pack(side="left")
        self.entry_id.pack(padx=5, side="left")
        self.frame_id.pack(padx=10, pady=10)

        ## Frame, label, and radio buttons for the voting section
        self.frame_candidates = Frame(self.frame_voting)
        self.label_candidates = Label(self.frame_candidates, text="CANDIDATES")
        self.candidate_choice = StringVar()
        self.candidate_choice.set('NA')
        self.candidate_fred = Radiobutton(self.frame_candidates, text='Fred', variable=self.candidate_choice, value='Fred')
        self.candidate_george = Radiobutton(self.frame_candidates, text='George', variable=self.candidate_choice, value='George')
        self.candidate_bob = Radiobutton(self.frame_candidates, text='Bob', variable=self.candidate_choice, value='Bob')
        self.label_candidates.pack(side="top")
        self.candidate_fred.pack(anchor="w", padx=10, side="top")
        self.candidate_george.pack(anchor="w", padx=10, side="top")
        self.candidate_bob.pack(anchor="w", padx=10, side="top")
        self.frame_candidates.pack(padx=10, pady=10)

        ## Frame and button for the submit section
        self.frame_submit = Frame(self.frame_voting)
        self.button_submit = Button(self.frame_submit, text="SUBMIT VOTE", command= lambda:logic.submit(self))
        self.button_submit.pack()
        self.frame_submit.pack(padx=10, pady=10)

        ## Frame and label for the message section
        self.frame_message = Frame(self.frame_voting)
        self.label_message = Label(self.frame_message,text="")
        self.label_message.pack()
        self.frame_message.pack(padx=10, pady=10)

        ## Frame and button for the see results section
        self.frame_done = Frame(self.frame_voting)
        self.button_results = Button(self.frame_done, text="See Current Results", command= lambda:logic.results(self))
        self.button_results.pack()
        self.frame_done.pack(padx=10)

        self.frames.append(self.frame_voting)
        self.frame_voting.grid(row=0, column=0, sticky=NSEW)

        ## Frame and label for the current results page
        self.frame_results = Frame(self.container)
        self.label_results = Label(self.frame_results, text="N/A")
        self.label_results.pack(side="top", fill="both", expand=True)
        self.frames.append(self.frame_results)
        self.frame_results.grid(row=0, column=0, sticky=NSEW)

        self.frame_voting.tkraise()

    def getId(self):
        """
        Returns:
            the current input in the self.entry_id entry box
        """
        return self.entry_id.get()

    def setMessage(self, message, color):
        """
        Sets the text and text color of the Label label_message

        Args:
            message (str): the desired message to set label_message text to
            color (str): the string for the desired text color for label_message

        Returns:
            nothing
        """
        self.label_message.config(text=message, fg=color)

    def getVote(self):
        """
        Returns:
            the selected candidate
        """
        return self.candidate_choice.get()

    def reset(self):
        """
        Clears the id input and unselects candidates

        Returns:
            nothing
        """
        self.entry_id.delete(0,END)
        self.candidate_choice.set('NA')
        self.entry_id.focus()

    def getFrame(self, index):
        """
        Args:
            index (int): the index for the desired frame in the list frames

        Returns:
            the frame in frames at the input index
        """
        return self.frames[index]

    def setResults(self, message):
        """
        Sets the text of the Label label_results to message

        Args:
            message (str): the desired message to set the text of label_results to

        Returns:
            nothing
        """
        self.label_results.config(text=message)