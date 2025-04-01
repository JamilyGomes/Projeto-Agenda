import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from Tela_Login import Ui_Tela_Login
from cadastro_proj import Ui_Tela_Cadastro

class LoginScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Tela_Login()
        self.ui.setupUi(self)  # ✅ Agora configura um QWidget corretamente

class CadastroScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Tela_Cadastro()
        self.ui.setupUi(self)  # ✅ Configurando um QWidget corretamente

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Principal")

        # Criando o QStackedWidget
        self.stacked_widget = QStackedWidget(self)

        # Criando as telas
        self.login_window = LoginScreen()
        self.cadastro_window = CadastroScreen()

        # Adicionando ao QStackedWidget
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.cadastro_window)

        # Definindo o QStackedWidget como central
        self.setCentralWidget(self.stacked_widget)

        # Conectando os botões para alternar entre as telas
        self.login_window.ui.botao_cadastro.clicked.connect(self.show_cadastro_screen)
        self.cadastro_window.ui.botao_voltar.clicked.connect(self.show_login_screen)

    def show_cadastro_screen(self):
        """Exibe a tela de cadastro."""
        self.stacked_widget.setCurrentWidget(self.cadastro_window)

    def show_login_screen(self):
        """Exibe a tela de login."""
        self.stacked_widget.setCurrentWidget(self.login_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec())  
