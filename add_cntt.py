from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (QMainWindow, QWidget, QFrame, QLabel, QLineEdit, QPushButton, 
                               QDateEdit, QTextEdit, QMessageBox, QScrollArea, QVBoxLayout, 
                               QHBoxLayout)
from bancodedados import salvar_contato
from datetime import datetime

class Ui_tela_add_contato(object):
    def __init__(self):
        self.usuario_id = None

    def setupUi(self, tela_add_contato, tela_contatos):
        self.tela_add_contato = tela_add_contato
        self.tela_contatos = tela_contatos

        tela_add_contato.setObjectName("tela_add_contato")
        tela_add_contato.resize(800, 600)
        tela_add_contato.setWindowTitle("Agenda de Contatos")
        tela_add_contato.setWindowIcon(QIcon("icone.ico"))
        self.centralwidget = QWidget(tela_add_contato)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        tela_add_contato.setCentralWidget(self.centralwidget)

        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self.frame = QFrame()
        self.frame.setStyleSheet("""
            background-color: rgb(40, 40, 50);
            border-radius: 10px;
        """)
        self.main_layout.addWidget(self.frame)

        self.scroll_area = QScrollArea(self.frame)
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

        self.scroll_layout = QVBoxLayout(self.frame)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.addWidget(self.scroll_area)

        self.scroll_widget = QWidget()
        self.scroll_widget_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_widget_layout.setAlignment(Qt.AlignTop)
        self.scroll_widget_layout.setSpacing(10)
        self.scroll_widget_layout.setContentsMargins(20, 20, 20, 20)
        self.scroll_area.setWidget(self.scroll_widget)

        self.txt_add_contato = QLabel("Adicionar Contato")
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_add_contato.setFont(font1)
        self.txt_add_contato.setStyleSheet("color: rgb(220, 220, 255); background-color: transparent;")
        self.txt_add_contato.setAlignment(Qt.AlignCenter)
        self.scroll_widget_layout.addWidget(self.txt_add_contato)

        font2 = QFont("Segoe UI", 12)

        self.txt_nome = QLabel("Nome:")
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_nome)

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
        self.scroll_widget_layout.addWidget(self.line_nome)

        self.asterisco_nome = QLabel("*")
        self.asterisco_nome.setFont(font2)
        self.asterisco_nome.setStyleSheet("color: rgb(255, 100, 100);")
        self.scroll_widget_layout.addWidget(self.asterisco_nome)

        self.txt_email = QLabel("Email:")
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_email)

        self.line_email = QLineEdit()
        self.line_email.setFixedHeight(40)
        self.line_email.setStyleSheet(self.line_nome.styleSheet())
        self.scroll_widget_layout.addWidget(self.line_email)

        self.txt_telefone = QLabel("Telefone:")
        self.txt_telefone.setFont(font2)
        self.txt_telefone.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_telefone)

        self.line_telefone = QLineEdit()
        self.line_telefone.setFixedHeight(40)
        self.line_telefone.setInputMask("(99) 99999-9999")
        self.line_telefone.setStyleSheet(self.line_nome.styleSheet())
        self.scroll_widget_layout.addWidget(self.line_telefone)

        self.txt_data_nascimento = QLabel("Data de Nascimento:")
        self.txt_data_nascimento.setFont(font2)
        self.txt_data_nascimento.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_data_nascimento)

        self.date_nascimento = QDateEdit()
        self.date_nascimento.setFixedHeight(40)
        self.date_nascimento.setCalendarPopup(True)
        self.date_nascimento.setMinimumDate(QDate(1, 1, 1))
        self.date_nascimento.setDate(QDate(1, 1, 1))
        self.date_nascimento.setStyleSheet("""
    QDateEdit {
        background-color: rgb(40, 40, 50);
        color: white;
        border: 1px solid rgb(80, 80, 100);
        border-radius: 5px;
        padding: 5px;
        font-family: Segoe UI;
        font-size: 12pt;
    }
    QDateEdit:focus {
        border: 1px solid rgb(100, 150, 255);
    }
    QCalendarWidget QAbstractItemView {
        background-color: rgb(40, 40, 50);
        color: white;
        selection-background-color: rgb(100, 150, 255);
        selection-color: white;
    }
    QCalendarWidget QWidget {
        alternate-background-color: rgb(40, 40, 50);
    }
""")

        self.scroll_widget_layout.addWidget(self.date_nascimento)

        self.txt_rede_social = QLabel("Rede Social:")
        self.txt_rede_social.setFont(font2)
        self.txt_rede_social.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_rede_social)

        self.line_rede_social = QLineEdit()
        self.line_rede_social.setFixedHeight(40)
        self.line_rede_social.setStyleSheet(self.line_nome.styleSheet())
        self.scroll_widget_layout.addWidget(self.line_rede_social)

        self.txt_notas = QLabel("Notas:")
        self.txt_notas.setFont(font2)
        self.txt_notas.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_notas)

        self.line_notas = QTextEdit()
        self.line_notas.setFixedHeight(80)
        self.line_notas.setStyleSheet(self.line_nome.styleSheet().replace("QLineEdit", "QTextEdit"))
        self.scroll_widget_layout.addWidget(self.line_notas)

        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignRight)
        self.button_layout.setSpacing(10)

        font3 = QFont("Segoe UI", 12, QFont.Bold)

        self.pushButton_voltar = QPushButton("Voltar")
        self.pushButton_voltar.setFixedSize(100, 40)
        self.pushButton_voltar.setFont(font3)
        self.pushButton_voltar.setStyleSheet("""
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
        self.pushButton_voltar.setCursor(Qt.PointingHandCursor)
        self.pushButton_voltar.clicked.connect(lambda: self.tela_add_contato.close())
        self.button_layout.addWidget(self.pushButton_voltar)

        self.pushButton_salvar = QPushButton("Salvar")
        self.pushButton_salvar.setFixedSize(100, 40)
        self.pushButton_salvar.setFont(font3)
        self.pushButton_salvar.setStyleSheet(self.pushButton_voltar.styleSheet().replace("255, 100, 100", "100, 150, 255").replace("200, 70, 70", "70, 100, 200"))
        self.pushButton_salvar.setCursor(Qt.PointingHandCursor)
        self.pushButton_salvar.clicked.connect(self.salvar_contato)
        self.button_layout.addWidget(self.pushButton_salvar)

        self.scroll_widget_layout.addLayout(self.button_layout)
        self.scroll_widget_layout.addSpacing(20)

    def salvar_contato(self):
        nome = self.line_nome.text()
        email = self.line_email.text()
        telefone = self.line_telefone.text()
        data_nascimento = self.date_nascimento.date()
        data_nascimento_str = None if data_nascimento == QDate(1, 1, 1) else data_nascimento.toString("yyyy-MM-dd")
        perfil_rede_social = self.line_rede_social.text()
        notas = self.line_notas.toPlainText()

        if nome == "":
            QMessageBox.warning(None, "Erro", "O campo Nome é obrigatório.")
            self.line_nome.setStyleSheet(self.line_nome.styleSheet().replace("rgb(80, 80, 100)", "rgb(255, 100, 100)"))
            return

        if salvar_contato(nome, email, telefone, data_nascimento_str, perfil_rede_social, notas, self.usuario_id, None):
            QMessageBox.information(None, "Sucesso", "Contato salvo com sucesso!")
            
            # Verificar se o contato salvo faz aniversário hoje
            hoje = datetime.now()
            dia_atual = hoje.day
            mes_atual = hoje.month
            if data_nascimento_str:
                data_nasc = datetime.strptime(data_nascimento_str, "%Y-%m-%d")
                if data_nasc.day == dia_atual and data_nasc.month == mes_atual:
                    if not self.tela_contatos.mensagem_aniversario_exibida:
                        self.tela_contatos.exibir_mensagem_aniversario([nome])

            self.tela_contatos.carregar_contatos()
            self.tela_add_contato.close()
        else:
            QMessageBox.warning(None, "Erro", "Erro ao salvar contato. Tente novamente.")