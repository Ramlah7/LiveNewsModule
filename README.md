
# Civic Participation System - News Module

## Project Overview
The **Civic Participation System** is a community-based platform designed to engage citizens in social and civic activities, fostering awareness and encouraging participation in governance and societal matters. This project incorporates multiple modules, each designed for a specific function. The **News Module** is one of the core components, which dynamically fetches and displays the latest news from top news outlets.

The **News Module** allows users to stay updated on the latest headlines with a clean, easy-to-use interface. The module is built using PyQt5 for the GUI and Python to handle backend functionality, including fetching news data from various RSS feeds.

## Features
- **News Display**: Displays articles from major news sources such as Dawn News, The News, Al Jazeera, and BBC News.
- **Dark Mode**: Toggle between light and dark themes for better user experience.
- **Export Headlines**: Allows users to download the latest headlines into a text file.
- **Real-time News Updates**: Fetches and displays the latest headlines when the "Refresh" button is clicked.
- **Interactive Interface**: A simple and interactive UI designed using PyQt5.

## Technologies Used
- **Frontend**: PyQt5 for creating the GUI components.
- **Backend**: Python for fetching news data from RSS feeds using the `feedparser` library.
- **Libraries**: 
  - PyQt5
  - feedparser

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ramlah7/LiveNewsModule.git
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Enjoy the News Feed!**

## Directory Structure
```
civic-participation-system/
│
├── gui.py            # Contains the NewsGUI class and layout for the news display
├── main.py           # Main file to run the application
├── news_fetcher.py   # Contains functions to fetch the latest news via RSS
├── icons/            # Folder with icon images for news sources like al jazeera,the new, dawn, bbc
├── requirements.txt  # List of required dependencies
└── README.md         # This file
```

## How it Works
1. When the user clicks the "Latest News" button, the **main.py** triggers the `refresh_news()` function.
2. The function fetches the latest news from multiple sources using the `fetch_latest_news()` function from **news_fetcher.py**.
3. The articles are then displayed in the GUI as clickable links under relevant categories (National, International).
4. Users can toggle between dark and light themes and export the displayed headlines to a `.txt` file.

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Make changes and test them.
4. Commit your changes and push your branch.
5. Open a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).
