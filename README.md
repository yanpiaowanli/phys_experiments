# Data Analysis Tools for University Physics Experiments Courses of TJU
This is a repo built for TJU's "University Physics Experiments" courses, a pointless, frustrating ordeal forced on students. Hours of useless labs with outdated equipment, leaving everyone annoyed and exhausted. No one learns anything meaningful, but it's mandatory, so we’re all wasting time on it.

However, life must go on, so I created these automation tools to handle experiment data. They're primarily for my own use, but if any TJU's poor inmates stumble across this repo, I hope these imperfect, error-filled scripts (btw I appreciate GPT as my loyal debugger, despite its sometimes noob-like code almost drove me crazy) can save you some time and sanity. You should spend that time reading books, watching movies—*The Grand Budapest Hotel* and *Eternal Sunshine of the Spotless Mind* are great picks (just saying). But seriously, this repo is far from being perfect, so treat it as a tool, not a crutch—**don’t rely on it completely**.

Before you start, I must remind you that **you should not use the scripts when your instructor is Cheng Peng, who is a disgusting teacher who opposed to technology**.

# How do I start?
## Installation
1. Install Python 3.8 or later.
2. Download this repo.
3. Install the required packages by running `pip install -r requirements.txt`. If you don't have pip, make sure you have successfully installed Python 3.8 or later first. If it still doesn't work, try rebooting your computer.

## Fill in the data
1. Open the `data` folder in the explorer.
2. Fill in the data in the `config.py` file using notepad. The data should be in the same format as the example data.
3. Fill in the data in the csv files using **EXCEL**, or **NOTEPAD**, **NOT** **WPS**. After that, **SAVE** and **QUIT**.

## Run the scripts
1. Open exp folder in explorer, enter `cmd` in the address bar, and press Enter. This will open a terminal in the folder.
2. Run the script by running `python main.py` in the terminal.

## Exp 1 Verification of Newton's Second Law
This contains 3 sub-experiments, which I won't waste any time trying to describe in English. We will only mention some of the bugs that appear in my code.

### Exp 1-1
### Exp 1-2
### Exp 1-3
Recheck the sig figs of the data. Some of them may be wrong.

## Exp 2 Calculation of the Young's Modulus of a Wire
**DON'T USE THIS IF YOUR EXPERIMENT INSTRUCTOR IS CHENG PENG, HE DOES NOT ALLOW COMPUTER GRAPHICS AND CALCULATION**
n_delta in result chart 1 is duplicated due to data processing, unique it yourself.
Same as d_avg in result chart 2.
Recheck the sig figs of the data. Some of them may be wrong.

## Exp 3 Torsional pendulum method for measuring the moment of inertia
Recheck the sig figs of the data. Some of them may be wrong.

## Exp 4 Wheatstone bridge method for measuring the resistance
Recheck the sig figs of the data. Some of them may be wrong.
