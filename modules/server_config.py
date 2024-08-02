from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

class ServerConfigDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configure Server")
        self.setGeometry(300, 300, 400, 300)
        self.layout = QVBoxLayout()

        self.server_type_label = QLabel("Select Server Type:")
        self.layout.addWidget(self.server_type_label)

        self.server_type_combo = QComboBox()
        self.server_type_combo.addItems([
            "Apache HTTP Server", "Nginx", "Flask", "Django",
            "Node.js", "Ruby on Rails", "Express.js", "Tomcat",
            "Jetty", "Spring Boot", "ASP.NET Core", "Caddy",
            "Golang Gin", "Koa.js", "Play Framework", "Sails.js",
            "Phoenix Framework", "Hapi.js", "Tornado"
        ])
        self.layout.addWidget(self.server_type_combo)

        self.port_label = QLabel("Port:")
        self.port_input = QLineEdit()
        self.layout.addWidget(self.port_label)
        self.layout.addWidget(self.port_input)

        self.ip_label = QLabel("IP Address:")
        self.ip_input = QLineEdit()
        self.layout.addWidget(self.ip_label)
        self.layout.addWidget(self.ip_input)

        self.launch_button = QPushButton("Launch Server")
        self.launch_button.clicked.connect(self.launch_server)
        self.layout.addWidget(self.launch_button)

        self.setLayout(self.layout)

    def launch_server(self):
        server_type = self.server_type_combo.currentText()
        port = self.port_input.text()
        ip = self.ip_input.text()
        # Add server launch logic here
        print(f"Launching {server_type} on {ip}:{port}")
