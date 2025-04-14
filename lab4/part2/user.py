# -------------------------------
# Title:    Simple Game Editor
# Author:   Belindo Bosco
# Date:     [Current Date]
# Purpose:  Basic game details viewer/editor
# -------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
#endregion

#region GLOBAL VARIABLES
window = tk.Tk()
lbxGames = tk.Listbox(window, height=15, width=30)
lblDetails = tk.Label(window, text="Select a game", justify=tk.LEFT)

#lists for game data
games = ["Game 1: Raptors vs Heat", "Game 2: Lakers vs Bulls"]
home_scores = [112, 98]
away_scores = [108, 102]
#endregion


#region FUNCTIONS

#region tools
def show_game_details():
    '''Display details of selected game'''
    selection = lbxGames.curselection()
    if not selection:
        messagebox.showwarning("Error", "Please select a game first")
        return
    
    index = selection[0]
    home, away = games[index].split(" vs ")
    home = home.split(": ")[1]
    
    details = f"Home: {home} ({home_scores[index]})\nAway: {away} ({away_scores[index]})"
    lblDetails.config(text=details)
#endregion

#region events
def btnExit_Click():
    '''Exit the program'''
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()

def btnShow_Click():
    '''Show game details'''
    show_game_details()
#endregion

#endregion


#region interface
def create_ui():
    '''Create the main window and widgets'''
    window.title("Game Editor")
    window.geometry("400x300")
    
    # Game list
    lbxGames.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="ns")
    
    # Details display
    lblDetails.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    # Buttons
    btnShow = tk.Button(window, text="SHOW", width=8, command=btnShow_Click)
    btnShow.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    Hovertip(btnShow, "Show game details")
    
    btnExit = tk.Button(window, text="EXIT", width=8, command=btnExit_Click)
    btnExit.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    Hovertip(btnExit, "Exit the program")

def load_data():
    '''Load game data into listbox'''
    for game in games:
        lbxGames.insert(tk.END, game)
#endregion

#region main
create_ui()
load_data()
window.mainloop()
exit()
#endregion