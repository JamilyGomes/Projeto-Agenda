from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit, QMainWindow, 
                               QPushButton, QWidget, QMessageBox, QFileDialog, QScrollArea, 
                               QVBoxLayout, QHBoxLayout)
from bancodedados import salvar_usuario

class Ui_Tela_Cadastro(object):
    def setupUi(self, Tela_Cadastro):
        self.foto_data = None  # Garante que a variável existe mesmo se o usuário não selecionar foto

        if not Tela_Cadastro.objectName():
            Tela_Cadastro.setObjectName("Tela_Cadastro")
        Tela_Cadastro.resize(800, 600)
        Tela_Cadastro.setWindowTitle("Agenda de Contatos")
        Tela_Cadastro.setWindowIcon(QIcon("agenda.png"))

        # Widget central com gradiente escuro
        self.centralwidget = QWidget(Tela_Cadastro)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        Tela_Cadastro.setCentralWidget(self.centralwidget)

        # Layout principal (vertical)
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        # Área de rolagem
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgb(40, 40, 50);
                border: none;
                border-radius: 10px;
            }
            QScrollBar:vertical {
                border: none;
                background: rgb(80, 80, 100);
                width: 10px;
                margin: 0px 0px 0px 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: rgb(100, 150, 255);
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        self.main_layout.addWidget(self.scroll_area)

        # Widget de conteúdo dentro da área de rolagem
        self.scroll_widget = QWidget()
        self.scroll_widget_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_widget_layout.setAlignment(Qt.AlignTop)
        self.scroll_widget_layout.setSpacing(10)
        self.scroll_widget_layout.setContentsMargins(20, 20, 20, 20)
        self.scroll_area.setWidget(self.scroll_widget)

        # Frame dentro do widget de rolagem
        self.frame = QFrame()
        self.frame.setStyleSheet("""
            background-color: rgb(40, 40, 50);
            border-radius: 10px;
        """)
        self.frame_layout = QVBoxLayout(self.frame)
        self.frame_layout.setContentsMargins(20, 20, 20, 20)
        self.frame_layout.setSpacing(10)
        self.scroll_widget_layout.addWidget(self.frame)

        # Foto de perfil (inicialmente vazia)
        self.label_foto = QLabel()
        self.label_foto.setFixedSize(100, 100)
        self.label_foto.setStyleSheet("""
            border: 1px solid rgb(80, 80, 100);
            border-radius: 50px;
            background-color: rgb(40, 40, 50);
        """)
        self.label_foto.setAlignment(Qt.AlignCenter)
        self.label_foto.setScaledContents(True)
        self.label_foto.setText("Sem Foto")
        self.frame_layout.addWidget(self.label_foto, alignment=Qt.AlignCenter)

        # Botão para selecionar foto
        self.btn_selecionar_foto = QPushButton("Selecionar Foto")
        self.btn_selecionar_foto.setFixedSize(120, 30)
        self.btn_selecionar_foto.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.btn_selecionar_foto.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(100, 150, 255),
                    stop: 1 rgb(70, 100, 200)
                );
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(120, 170, 255),
                    stop: 1 rgb(90, 120, 220)
                );
            }
            QPushButton:pressed {
                background: rgb(50, 80, 180);
            }
        """)
        self.btn_selecionar_foto.setCursor(Qt.PointingHandCursor)
        self.btn_selecionar_foto.clicked.connect(self.selecionar_foto)
        self.frame_layout.addWidget(self.btn_selecionar_foto, alignment=Qt.AlignCenter)

        # Título
        self.txt_Criar_Conta = QLabel("Crie sua conta")
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_Criar_Conta.setFont(font1)
        self.txt_Criar_Conta.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)
        self.txt_Criar_Conta.setAlignment(Qt.AlignCenter)
        self.frame_layout.addWidget(self.txt_Criar_Conta)

        # Campo Nome
        self.txt_nome = QLabel("Nome:")
        font2 = QFont("Segoe UI", 12)
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet("color: rgb(200, 200, 200);")
        self.frame_layout.addWidget(self.txt_nome)

        self.line_nome = QLineEdit()
        self.line_nome.setFixedHeight(40)
        self.line_nome.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.frame_layout.addWidget(self.line_nome)

        self.asterisco_nome = QLabel("*")
        self.asterisco_nome.setFont(font2)
        self.asterisco_nome.setStyleSheet("color: rgb(255, 100, 100);")
        self.frame_layout.addWidget(self.asterisco_nome)

        # Campo Email
        self.txt_email = QLabel("Email:")
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.frame_layout.addWidget(self.txt_email)

        self.line_email = QLineEdit()
        self.line_email.setFixedHeight(40)
        self.line_email.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.frame_layout.addWidget(self.line_email)

        self.asterisco_email = QLabel("*")
        self.asterisco_email.setFont(font2)
        self.asterisco_email.setStyleSheet("color: rgb(255, 100, 100);")
        self.frame_layout.addWidget(self.asterisco_email)

        # Campo Contato
        self.txt_contato = QLabel("Contato:")
        self.txt_contato.setFont(font2)
        self.txt_contato.setStyleSheet("color: rgb(200, 200, 200);")
        self.frame_layout.addWidget(self.txt_contato)

        self.line_contato = QLineEdit()
        self.line_contato.setFixedHeight(40)
        self.line_contato.setInputMask("(99) 99999-9999")
        self.line_contato.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.frame_layout.addWidget(self.line_contato)

        # Campo Senha
        self.txt_senha = QLabel("Senha:")
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet("color: rgb(200, 200, 200);")
        self.frame_layout.addWidget(self.txt_senha)

        self.line_senha = QLineEdit()
        self.line_senha.setFixedHeight(40)
        self.line_senha.setEchoMode(QLineEdit.Password)
        self.line_senha.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.frame_layout.addWidget(self.line_senha)

        self.asterisco_senha = QLabel("*")
        self.asterisco_senha.setFont(font2)
        self.asterisco_senha.setStyleSheet("color: rgb(255, 100, 100);")
        self.frame_layout.addWidget(self.asterisco_senha)

        # Campo Confirmação de Senha
        self.txt_confrimar_senha = QLabel("Confirmar Senha:")
        self.txt_confrimar_senha.setFont(font2)
        self.txt_confrimar_senha.setStyleSheet("color: rgb(200, 200, 200);")
        self.frame_layout.addWidget(self.txt_confrimar_senha)

        self.line_Confirmar_senha = QLineEdit()
        self.line_Confirmar_senha.setFixedHeight(40)
        self.line_Confirmar_senha.setEchoMode(QLineEdit.Password)
        self.line_Confirmar_senha.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.frame_layout.addWidget(self.line_Confirmar_senha)

        self.asterisco_conf_senha = QLabel("*")
        self.asterisco_conf_senha.setFont(font2)
        self.asterisco_conf_senha.setStyleSheet("color: rgb(255, 100, 100);")
        self.frame_layout.addWidget(self.asterisco_conf_senha)

        # Botões Cadastrar e Voltar
        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignRight)
        self.button_layout.setSpacing(10)

        self.pushButton_Voltar = QPushButton("Voltar")
        self.pushButton_Voltar.setFixedSize(100, 40)
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.pushButton_Voltar.setFont(font3)
        self.pushButton_Voltar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 100, 100),
                    stop: 1 rgb(200, 70, 70)
                );
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 120, 120),
                    stop: 1 rgb(220, 90, 90)
                );
            }
            QPushButton:pressed {
                background: rgb(180, 50, 50);
            }
        """)
        self.pushButton_Voltar.setCursor(Qt.PointingHandCursor)
        self.pushButton_Voltar.clicked.connect(lambda: self.voltar_para_login(Tela_Cadastro))
        self.button_layout.addWidget(self.pushButton_Voltar)

        self.pushButton_Cadastrar = QPushButton("Cadastrar")
        self.pushButton_Cadastrar.setFixedSize(100, 40)
        self.pushButton_Cadastrar.setFont(font3)
        self.pushButton_Cadastrar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(100, 150, 255),
                    stop: 1 rgb(70, 100, 200)
                );
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(120, 170, 255),
                    stop: 1 rgb(90, 120, 220)
                );
            }
            QPushButton:pressed {
                background: rgb(50, 80, 180);
            }
        """)
        self.pushButton_Cadastrar.setCursor(Qt.PointingHandCursor)
        self.pushButton_Cadastrar.clicked.connect(lambda: self.realizar_cadastro(Tela_Cadastro))
        self.button_layout.addWidget(self.pushButton_Cadastrar)

        self.frame_layout.addLayout(self.button_layout)

        # Link Entrar
        self.link_layout = QHBoxLayout()
        self.link_layout.setAlignment(Qt.AlignCenter)
        self.link_layout.setSpacing(5)

        self.txt_jtemconta = QLabel("Já tem conta?")
        self.txt_jtemconta.setFont(font2)
        self.txt_jtemconta.setStyleSheet("color: rgb(200, 200, 200);")
        self.link_layout.addWidget(self.txt_jtemconta)

        self.link_entrar = QLabel("<a href='#'>Entrar</a>")
        self.link_entrar.setFont(font2)
        self.link_entrar.setStyleSheet("""
            color: rgb(220, 220, 255);
            text-decoration: underline;
            background-color: transparent;
        """)
        self.link_entrar.mousePressEvent = lambda event: self.abrir_tela_login(Tela_Cadastro)
        self.link_layout.addWidget(self.link_entrar)

        self.frame_layout.addLayout(self.link_layout)

        # Adicionar um espaço extra no final
        self.frame_layout.addSpacing(20)

        self.retranslateUi(Tela_Cadastro)

    def retranslateUi(self, Tela_Cadastro):
        Tela_Cadastro.setWindowTitle("Cadastro de Usuário")
        self.txt_Criar_Conta.setText("Crie sua conta")
        self.txt_jtemconta.setText("Já tem conta?")
        self.link_entrar.setText("Entrar")
        self.txt_nome.setText("Nome:")
        self.txt_email.setText("Email:")
        self.txt_contato.setText("Contato:")
        self.txt_senha.setText("Senha:")
        self.txt_confrimar_senha.setText("Confirmar Senha:")
        self.pushButton_Cadastrar.setText("Cadastrar")
        self.pushButton_Voltar.setText("Voltar")

    def selecionar_foto(self):
        arquivo, _ = QFileDialog.getOpenFileName(self.frame, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)")
        if arquivo:
            pixmap = QPixmap(arquivo)
            self.label_foto.setPixmap(pixmap)
            with open(arquivo, "rb") as f:
                self.foto_data = f.read()

    def abrir_tela_login(self, Tela_Cadastro):
        from Tela_Login import TelaLogin
        self.tela_login = TelaLogin()
        self.tela_login.show()
        Tela_Cadastro.close()

    def voltar_para_login(self, Tela_Cadastro):
        self.abrir_tela_login(Tela_Cadastro)

    def realizar_cadastro(self, Tela_Cadastro):
        nome = self.line_nome.text()
        email = self.line_email.text()
        contato = self.line_contato.text()
        senha = self.line_senha.text()
        confirmar_senha = self.line_Confirmar_senha.text()

        self.limpar_bordas()

        if senha != confirmar_senha:
            QMessageBox.warning(None, "Erro", "As senhas não coincidem.")
        elif nome == "" or email == "" or senha == "":
            QMessageBox.warning(None, "Erro", "Preencha todos os campos obrigatórios.")
            self.validar_campos_vazios(nome, email, contato, senha, confirmar_senha)
        else:
            if salvar_usuario(nome, email, contato, senha, self.foto_data):
                QMessageBox.information(None, "Sucesso", "Cadastro realizado com sucesso!")
                self.voltar_para_login(Tela_Cadastro)
            else:
                QMessageBox.warning(None, "Erro", "Erro ao cadastrar! Verifique os dados.")

    def limpar_bordas(self):
        self.line_nome.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_email.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_contato.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_senha.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_Confirmar_senha.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)

    def validar_campos_vazios(self, nome, email, contato, senha, confirmar_senha):
        if nome == "":
            self.line_nome.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if email == "":
            self.line_email.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if contato == "":
            self.line_contato.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if senha == "":
            self.line_senha.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if confirmar_senha == "":
            self.line_Confirmar_senha.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_Tela_Cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()