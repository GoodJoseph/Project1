import tkinter as tk
from Project1 import Vote
import csv

class VoteGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vote System")
        self.geometry("300x250")
        self.Project1 = Vote()
        self.vote_box()

    def vote_box(self):
        
        label = tk.Label(self, text="Votes for candidates:")
        label.pack()
        
        self.vote_labels = {
            'Cameron': tk.Label(self, text='Cameron: 0'),
            'Allison': tk.Label(self, text='Allison: 0'),
            'Diego': tk.Label(self, text='Diego: 0')
            }
        
        for label in self.vote_labels.values():
            label.pack()
        
        self.display_label = tk.Label(self, text="Please select one of the options below:")
        self.display_label.pack()
        
        cameron_button = tk.Button(self, text="Cameron", command=self.vote_cameron)
        cameron_button.pack()

        allison_button = tk.Button(self, text="Allison", command=self.vote_allison)
        allison_button.pack()

        diego_button = tk.Button(self, text="Diego", command=self.vote_diego)
        diego_button.pack()

        total_button = tk.Button(self, text="Save Totals", command=self.save_totals)
        total_button.pack()

        reset_button = tk.Button(self, text="Reset Votes", command=self.reset_votes)
        reset_button.pack()
        
    def update_vote_labels(self):
        totals = self.Project1.get_totals()
        for candidate, label in self.vote_labels.items():
            label.config(text=f'{candidate}: {totals[candidate]}')

    def vote_cameron(self):
        self.Project1.vote_cameron()
        self.update_vote_labels()
        self.display_label.config(text="Voted Cameron!")

    def vote_allison(self):
        self.Project1.vote_allison()
        self.update_vote_labels()
        self.display_label.config(text="Voted Allison!")

    def vote_diego(self):
        self.Project1.vote_diego()
        self.update_vote_labels()
        self.display_label.config(text="Voted Diego!")

    def save_totals(self):
        totals = self.Project1.get_totals()
        with open('data.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(totals)
            writer.writerow(totals.values())
            self.display_label.config(text='Saved total votes to: "data.csv".')

    def reset_votes(self):
        self.Project1.reset_votes()
        self.update_vote_labels()
        self.display_label.config(text="Successfully Reset Votes!")

if __name__ == "__main__":
    VoteGUI().mainloop()