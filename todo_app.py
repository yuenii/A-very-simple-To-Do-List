import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel, QColorDialog
from PyQt5 import QtCore, QtGui

#add font box
# add title bar
# change colours 

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daily Tasks")
        self.setGeometry(100, 100, 350, 300)


        self.tasks = []
        
        self.layout = QVBoxLayout()
        self.input_field = QLineEdit()


        #labels 
        self.label1 = QLabel("Task List")
        self.label2 = QLabel("Add a task:")


        #add task button
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        #delete task button
        self.delete_button = QPushButton("Delete Task")
        # self.delete_button.setGeometry(10, 10, 10, 40) doesn't work 
        self.delete_button.clicked.connect(self.delete_task)

        self.task_list = QListWidget()
        

        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.input_field)

        #shift to add task
        self.input_field.returnPressed.connect(self.add_task) 
        self.layout.addWidget(self.input_field)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)
        
        
        self.setLayout(self.layout)

    
    #add a selected task
    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()

    #delete a selected task
    def delete_task(self):
        selected_task = self.task_list.selectedItems()
        if not selected_task: return

        for item in selected_task:
            self.task_list.takeItem(self.task_list.row(item))

    #add task by shift 
    def update_task_list(self):
        self.input_field.clear()
        self.tasks_list.setText("\n".join(self.tasks))


    #delete by delete key 
    def keyPressEvent(self, event):
        selected_task = self.task_list.selectedItems()
        if not selected_task: return

        for item in selected_task:
            self.task_list.takeItem(self.task_list.row(item))
        
        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())