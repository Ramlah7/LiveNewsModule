# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui import NewsGUI
from news_fetcher import fetch_latest_news

def main():
    app = QApplication(sys.argv)
    gui = NewsGUI()

    def refresh_news():
        news_data = fetch_latest_news()
        gui.update_news(news_data)
        try:
            top_3 = news_data["Dawn News"][:3]
            ticker_text = " 🔈 " + " | ".join([x["title"] for x in top_3])
            gui.ticker.setText(ticker_text)
        except:
            gui.ticker.setText("🔈 News ticker unavailable.")

    gui.refresh_button.clicked.connect(refresh_news)
    refresh_news()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
