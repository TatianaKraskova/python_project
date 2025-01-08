class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}")

app_user_one = User("nn@nn.com", "Nana", "pwd1", "Devops engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("Developer")
app_user_one.get_user_info()

app_user_two = User("nn1@nn.com", "Mary", "pwd1", "Teacher")
app_user_two.get_user_info()