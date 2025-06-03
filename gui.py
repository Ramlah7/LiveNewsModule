from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QGroupBox,
    QHBoxLayout, QFileDialog, QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class NewsCard(QGroupBox):
    def __init__(self, title, articles, icon_path=None):
        super().__init__()
        self.setTitle("")
        layout = QVBoxLayout()
        layout.setSpacing(4)

        header_layout = QHBoxLayout()
        if icon_path:
            logo = QLabel()
            pixmap = QPixmap(icon_path)
            pixmap = pixmap.scaledToHeight(24)
            logo.setPixmap(pixmap)
            header_layout.addWidget(logo)

        title_label = QLabel(f"<b>{title}</b>")
        title_label.setStyleSheet("font-size: 13pt; font-family: Georgia, serif; padding-left: 6px;")
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        layout.addLayout(header_layout)

        for article in articles:
            label = QLabel(f'<a href="{article["link"]}" style="text-decoration:none;">{article["title"]}</a>')
            label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            label.setOpenExternalLinks(True)
            layout.addWidget(label)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setMaximumHeight(400)
        self.setMaximumWidth(650)
        self.setObjectName("NewsCard")


class NewsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📰 Unified News Reader")
        self.setFixedSize(1350, 750)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.theme = "light"
        self.news_data = {}

        self.setStyleSheet(self.get_stylesheet(self.theme))
        self.main_layout = QVBoxLayout()

        self.ticker = QLabel("🔈 Loading top headlines...")
        self.ticker.setObjectName("ticker")
        self.main_layout.addWidget(self.ticker, alignment=Qt.AlignCenter)

        self.refresh_button = QPushButton("🔄 Refresh")
        self.theme_button = QPushButton("🌙 Dark Mode")
        self.export_button = QPushButton("⬇ Export Headlines")

        for btn in [self.refresh_button, self.theme_button, self.export_button]:
            btn.setFixedWidth(180)
            btn.setCursor(Qt.PointingHandCursor)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.refresh_button)
        btn_layout.addWidget(self.theme_button)
        btn_layout.addWidget(self.export_button)
        btn_layout.addStretch()
        self.main_layout.addLayout(btn_layout)

        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_area.setWidgetResizable(True)

        self.left_col = QVBoxLayout()
        self.right_col = QVBoxLayout()

        self.left_col.addWidget(self.section_header("📰 National News"))
        self.right_col.addWidget(self.section_header("🌍 International News"))

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.left_col)
        self.hbox.addSpacing(20)
        self.hbox.addLayout(self.right_col)

        self.scroll_widget.setLayout(self.hbox)
        self.scroll_area.setWidget(self.scroll_widget)
        self.main_layout.addWidget(self.scroll_area)

        footer = QLabel("Made with ❤ using PyQt5")
        footer.setAlignment(Qt.AlignCenter)
        footer.setObjectName("footer")
        self.main_layout.addWidget(footer)

        self.setLayout(self.main_layout)
        self.theme_button.clicked.connect(self.toggle_theme)
        self.export_button.clicked.connect(self.export_headlines)

    def section_header(self, text):
        label = QLabel(text)
        label.setObjectName("sectionHeader")
        return label

    def get_stylesheet(self, theme):
        if theme == "dark":
            return """
                            /* Dark Theme with Full Light Blue NewsCards */
                            QWidget {
                                background: #121212;
                                color: #e0e0e0;
                                font-family: 'Georgia', serif;
                            }

                            /* NewsCard - Full Light Blue Styling */
                            #NewsCard {
                                background-color: #e6f7ff;  /* Light blue background */
                                border: 2px solid #66b3ff;
                                border-radius: 12px;
                                padding: 12px;
                                margin: 10px;
                            }

                            /* All text inside NewsCard */
                            #NewsCard * {
                                background-color: #e6f7ff;  /* Force light blue bg for all child elements */
                                color: #003366;  /* Dark blue text for contrast */
                            }

                            /* Links styling */
                            #NewsCard QLabel a {
                                color: #0066cc;  /* Standard link blue */
                                text-decoration: none;
                                background-color: transparent;  /* Keep link bg transparent */
                            }

                            #NewsCard QLabel a:hover {
                                color: #004080;  /* Darker blue on hover */
                                text-decoration: underline;
                            }

                            /* News source title */
                            #NewsCard QLabel[title] {
                                font-weight: bold;
                                font-size: 13pt;
                            }

                            /* Rest of the UI styling */
                            #sectionHeader {
                                font-size: 14pt;
                                font-weight: bold;
                                padding: 8px 0;
                                color: #66b3ff;
                                background: transparent;
                            }

                            #ticker {
                                font-size: 13pt;
                                font-weight: 600;
                                color: #ff6b6b;
                                padding: 6px;
                                background-color: rgba(30, 30, 30, 0.7);
                                border-radius: 8px;
                            }

                            QPushButton {
                                background-color: #1e3d6b;
                                color: white;
                                border-radius: 8px;
                                padding: 8px;
                                font-size: 12pt;
                            }

                            QPushButton:hover {
                                background-color: #2a4a7a;
                            }

                            #footer {
                                color: #666666;
                                font-size: 10pt;
                                background: transparent;
                            }
                        """
        else:
            return """
             /* Light Theme - Mint Green NewsCards */
                QWidget {
                    background: #f5f9fc;
                    color: #2d3748;
                    font-family: 'Georgia', serif;
                }
                
                #NewsCard {
                    background-color: #e8f8f5;  /* Light mint green */
                    border: 1px solid #88c9b9;
                    border-radius: 12px;
                    padding: 15px;
                    margin: 10px;
                }
                
                #NewsCard * {
                    background-color: #e8f8f5;
                    color: #1a3e34;  /* Dark greenish text */
                }
                
                #NewsCard QLabel a {
                    color: #2a7f62;  /* Medium green-blue links */
                    text-decoration: none;
                    background-color: transparent;
                }
                
                #NewsCard QLabel a:hover {
                    color: #1e5a46;
                    text-decoration: underline;
                }
                
                #sectionHeader {
                    font-size: 14pt;
                    font-weight: bold;
                    padding: 8px 0;
                    color: #2a7f62;
                    background: transparent;
                }
                
                #ticker {
                    font-size: 13pt;
                    font-weight: 600;
                    color: #e74c3c;
                    padding: 6px;
                    background-color: rgba(255, 255, 255, 0.7);
                    border-radius: 8px;
                }
                
                QPushButton {
                    background-color: #2a7f62;
                    color: white;
                    border-radius: 8px;
                    padding: 8px;
                    font-size: 12pt;
                    border: none;
                }
                
                QPushButton:hover {
                    background-color: #1e5a46;
                }
                
                #footer {
                    color: #7f8c8d;
                    font-size: 10pt;
                    background: transparent;
                }
            """

    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.theme_button.setText("🌙 Dark Mode" if self.theme == "light" else "☀ Light Mode")
        self.setStyleSheet(self.get_stylesheet(self.theme))

    def update_news(self, news_dict):
        self.news_data = news_dict
        for layout in [self.left_col, self.right_col]:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, NewsCard):
                    widget.setParent(None)

        for source, articles in news_dict.items():
            icon = self.get_icon_for_source(source)
            card = NewsCard(source, articles, icon_path=icon)
            if source in ["Dawn News", "The News"]:
                self.left_col.addWidget(card)
            else:
                self.right_col.addWidget(card)

    def get_icon_for_source(self, source):
        icons = {
            "Dawn News": "icons/dawn.png",
            "The News": "icons/thenews.png",
            "Al Jazeera": "icons/aljazeera.png",
            "BBC News": "icons/bbc.png"
        }
        return icons.get(source, None)

    def export_headlines(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Headlines", "headlines.txt", "Text Files (*.txt)")
        if not filename:
            return

        with open(filename, "w", encoding="utf-8") as f:
            for source, articles in self.news_data.items():
                f.write(f"=== {source} ===\n")
                for article in articles:
                    f.write(f"- {article['title']}\n  {article['link']}\n")
                f.write("\n")