import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from modules.create_account import create_account
from modules.scrape_data import login_and_scrape
from modules.solve_captcha import solve_captcha

class BlackDiamondPortfolioManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Black Diamond Portfolio Manager")
        self.setGeometry(100, 100, 1200, 800)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.create_menu_bar()
        self.create_main_widgets()

        with open("material_style.qss", "r") as file:
            self.setStyleSheet(file.read())

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')
        server_menu = menu_bar.addMenu('Servers')

        new_action = QAction('New', self)
        file_menu.addAction(new_action)

        launch_server_action = QAction('Launch New Server', self)
        launch_server_action.triggered.connect(self.launch_server)
        server_menu.addAction(launch_server_action)

    def create_main_widgets(self):
        tabs = QTabWidget()
        tabs.addTab(FileExplorer(), "File Explorer")
        tabs.addTab(CodeEditor(), "Code Editor")
        tabs.addTab(Terminal(), "Terminal")
        tabs.addTab(WebScraperWidget(), "Web Scraper")

        self.layout.addWidget(tabs)

    def launch_server(self):
        self.server_config_dialog = ServerConfigDialog()
        self.server_config_dialog.show()

class WebScraperWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter email")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter password")

        self.captcha_api_key_input = QLineEdit(self)
        self.captcha_api_key_input.setPlaceholderText("Enter CAPTCHA API key")

        self.create_account_button = QPushButton("Create Account", self)
        self.create_account_button.clicked.connect(self.create_account)

        self.scrape_data_button = QPushButton("Scrape Data", self)
        self.scrape_data_button.clicked.connect(self.scrape_data)

        self.layout.addWidget(QLabel("Account Creation"))
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.captcha_api_key_input)
        self.layout.addWidget(self.create_account_button)
        self.layout.addWidget(QLabel("Scrape Data"))
        self.layout.addWidget(self.scrape_data_button)

        self.setLayout(self.layout)

    def create_account(self):
        email = self.email_input.text()
        password = self.password_input.text()
        captcha_api_key = self.captcha_api_key_input.text()

        captcha_solution = solve_captcha(captcha_api_key, "captcha_image_path")
        if captcha_solution:
            create_account(email, password, captcha_solution)
        else:
            print("Failed to solve CAPTCHA")

    def scrape_data(self):
        email = self.email_input.text()
        password = self.password_input.text()
        login_and_scrape(email, password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = BlackDiamondPortfolioManager()
    main_window.show()
    sys.exit(app.exec())
