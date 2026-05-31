from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle #tambahkan

app = QApplication([])
layout_card = QVBoxLayout() #tambahkan
window = QWidget()
window.setLayout(layout_card) #tambhkan
window.setWindowTitle('Memo Card')
btn_OK = QPushButton('Answer') 
lb_Question = QLabel('The most difficult question in the world!')

RadioGroupBox = QGroupBox("Answer options") 
rbtn_1 = QRadioButton('Option 1') #ganti
rbtn_2 = QRadioButton('Option 2') #ganti
rbtn_3 = QRadioButton('Option 3') #ganti
rbtn_4 = QRadioButton('Option 4') #ganti

RadioGroup = QButtonGroup() #tambahkan
RadioGroup.addButton(rbtn_1) #tambahkan
RadioGroup.addButton(rbtn_2) #tambahkan
RadioGroup.addButton(rbtn_3) #tambahkan
RadioGroup.addButton(rbtn_4) #tambahkan

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Test result")

lb_Result = QLabel('are you correct or not?')
lb_Correct = QLabel('the answer will be here!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) #tambahkan
    rbtn_1.setChecked(False)#tambahkan
    rbtn_2.setChecked(False)#tambahkan
    rbtn_3.setChecked(False)#tambahkan
    rbtn_4.setChecked(False)#tambahkan
    RadioGroup.setExclusive(True) #tambahkan

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] #tambahkan
def ask(question, right_answer, wrong1, wrong2, wrong3): #tambahkan
    shuffle(answers) #tambahkan
    answers[0].setText(right_answer) #tambahkan
    answers[1].setText(wrong1) #tambahkan
    answers[2].setText(wrong2) #tambahkan
    answers[3].setText(wrong3) #tambahkan
    lb_Question.setText(question) #tambahkan
    lb_Correct.setText(right_answer)  #tambahkan
    show_question() #tambahkan

def show_correct(res):#tambahkan
    lb_Result.setText(res)#tambahkan
    show_result()#tambahkan

def check_answer():#tambahkan
    if answers[0].isChecked():#tambahkan
        show_correct('Correct!')#tambahkan
    else: #tambahkan
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():#tambahkan
            show_correct('Incorrect!')#tambahkan
ask('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')#tambahkan
btn_OK.clicked.connect(check_answer) #ganti jadi check answer

window.show()
app.exec()
