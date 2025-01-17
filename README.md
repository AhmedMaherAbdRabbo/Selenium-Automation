# Selenium Automation for LiveRankFPL

## Overview

This script automates interactions with the LiveFPL website, which displays rankings for the Fantasy Premier League (FPL). Users can input their FPL ID and choose a group to view rankings. The script performs the necessary interactions with the website and captures a screenshot of the rankings page, saving it with a timestamped filename.

## Features

- **Automated Input**: Enter your FPL ID and select the group ranking you want to view.
- **Screenshot Capture**: Automatically takes a screenshot of the rankings page.
- **Organized Storage**: Saves the screenshot in a designated folder with a timestamped filename for easy retrieval.

## Requirements

### User Input:

- **FPL ID**: The user must provide their FPL ID to view their ranking.
- **Group Selection**: The user must select a group from the dropdown menu to view the rankings for that specific group.
- **A Designated Folder Path**: The user must specify a folder path for saving screenshots (e.g., `D:\JupyterNotebook\task 2 Selenium\screenshots`).

### Software Requirements:

1. Python 3.x
2. Selenium library (`pip install selenium`)
3. ChromeDriver (automatically managed by `webdriver_manager`)
4. Google Chrome browser

## How the Script Works

1. **Initialization**: The script initializes the Chrome WebDriver using Selenium and navigates to the LiveFPL website.
2. **Input FPL ID**: The script locates the input field for the FPL ID and enters the provided ID.
3. **Group Selection**: The script waits for the group selection dropdown to be clickable, then selects the specified group (e.g., "Free Palestine 🇵🇸✌🏻").
4. **Scroll Page**: The script scrolls down the page to ensure the ranking information is visible.
5. **Capture Screenshot**: The script captures a screenshot of the ranking page and saves it in the specified directory with a timestamped filename.
6. **Open Screenshot**: The script automatically opens the saved screenshot using the default image viewer.

## Code Overview

The script leverages the Selenium library for browser automation and interaction with the LiveFPL website. Key elements include:

- `WebDriverWait` for handling dynamic page elements.
- `Select` for interacting with dropdown menus.
- `execute_script` for scrolling actions.
- `get_screenshot_as_file` for saving screenshots.

## Directory Structure

```
Project Folder
|
|-- script.py   # The automation script
|
|-- screenshots/  # Folder to store screenshots
    |-- SS_<timestamp>.png  # Timestamped screenshot files
```

## Input

- **FPL ID**: The unique ID associated with your Fantasy Premier League account.
- **Group Name**: The name of the group whose rankings you wish to view.
- **A Designated Folder Path**: The folder where screenshots will be saved (e.g., `D:\JupyterNotebook\task 2 Selenium\screenshots`).

## Output

- A screenshot of the rankings page saved in the designated folder with a filename format: `SS_<dd-mm_hh-mm>.png`.

## Example Usage

1. Ensure all requirements are installed.
2. Run the script:
   ```bash
   python script.py
   ```

The script will automatically:

- Navigate to the LiveRankFPL website.
- Input the FPL ID and select the group.
- Capture and save a screenshot of the ranking page.
- Open the saved screenshot.

## Notes

- Ensure the Chrome browser is installed and up-to-date.
- The script is designed to work with the specific structure of the LiveRankFPL website. If the website structure changes, the script may need to be updated accordingly.


<br>

<hr>