from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QListView, QMainWindow, QTextEdit, QPushButton
from add_cntt import Ui_tela_add_contato

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(988, 579)

        self.frame_principal_cntt = QFrame(Form)
        self.frame_principal_cntt.setObjectName(u"frame_principal_cntt")
        self.frame_principal_cntt.setGeometry(QRect(170, 80, 651, 401))
        self.frame_principal_cntt.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.label_Cntt = QLabel(self.frame_principal_cntt)
        self.label_Cntt.setObjectName(u"label_Cntt")
        self.label_Cntt.setGeometry(QRect(30, 20, 71, 16))
        self.label_Cntt.setStyleSheet(u"font: 700 12pt \"Segoe Print\";")

        self.line_buscar_cntt = QLineEdit(self.frame_principal_cntt)
        self.line_buscar_cntt.setObjectName(u"line_buscar_cntt")
        self.line_buscar_cntt.setGeometry(QRect(30, 40, 181, 22))
        self.line_buscar_cntt.setPlaceholderText("Buscar Contatos...")

        self.contatos = ["Abgail", "Bento", "João", "Maria"]
        self.labels_contatos = []
        self.chat_histories = {contato: [] for contato in self.contatos}  

        y_positions = [90, 130, 170, 210]
        for i, nome in enumerate(self.contatos):
            label = QLabel(self.frame_principal_cntt)
            label.setObjectName(f"label_{nome}")
            label.setGeometry(QRect(40, y_positions[i], 50, 16))
            label.setText(nome)
            self.labels_contatos.append(label)
            label.mousePressEvent = lambda event, n=nome: self.abrir_chat(n)  

        # Área do Chat
        self.frame_chat = QFrame(Form)
        self.frame_chat.setObjectName("frame_chat")
        self.frame_chat.setGeometry(QRect(170, 500, 651, 150))
        self.frame_chat.setStyleSheet("background-color: lightgray;")
        self.frame_chat.setVisible(False) 

        self.label_chat = QLabel(self.frame_chat)
        self.label_chat.setObjectName("label_chat")
        self.label_chat.setGeometry(QRect(10, 10, 150, 20))
        self.label_chat.setText("Chat com: ")

        self.chat_area = QTextEdit(self.frame_chat)
        self.chat_area.setObjectName("chat_area")
        self.chat_area.setGeometry(QRect(10, 40, 500, 80))
        self.chat_area.setReadOnly(True)

        self.input_mensagem = QLineEdit(self.frame_chat)
        self.input_mensagem.setObjectName("input_mensagem")
        self.input_mensagem.setGeometry(QRect(10, 130, 420, 20))

        self.botao_enviar = QPushButton(self.frame_chat)
        self.botao_enviar.setObjectName("botao_enviar")
        self.botao_enviar.setGeometry(QRect(440, 130, 70, 20))
        self.botao_enviar.setText("Enviar")
        self.botao_enviar.clicked.connect(self.enviar_mensagem)

        self.contato_atual = None  

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Contatos", None))
        self.label_Cntt.setText(QCoreApplication.translate("Form", "Contatos", None))

    def abrir_chat(self, contato):
        """ Exibe o chat do contato selecionado. """
        self.contato_atual = contato
        self.frame_chat.setVisible(True)
        self.label_chat.setText(f"Chat com: {contato}")
        self.exibir_historico_chat()

    def exibir_historico_chat(self):
        """ Atualiza a área de texto com o histórico do chat do contato atual. """
        if self.contato_atual:
            self.chat_area.setText("\n".join(self.chat_histories[self.contato_atual]))

    def enviar_mensagem(self):
        """ Envia a mensagem e adiciona ao histórico do contato. """
        if self.contato_atual:
            mensagem = self.input_mensagem.text().strip()
            if mensagem:
                self.chat_histories[self.contato_atual].append(f"Você: {mensagem}")
                self.input_mensagem.clear()
                self.exibir_historico_chat()

if __name__ == "__main__":
    app = QApplication([])  
    MainWindow = QMainWindow()  
    ui = Ui_Form()  
    ui.setupUi(MainWindow)  
    MainWindow.show()  
    app.exec()  