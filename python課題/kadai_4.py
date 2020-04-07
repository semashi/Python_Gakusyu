class Human:
    def __init__(self,name):　#初期化:インスタンス作成時に自動的に呼ばれる
        self.name = name　　#インスタンス変数 name を宣言

class Patient(Human):　#Humanクラスを継承したPatientクラスを作成
    def __init__(self,symptom,patient_id):　 #初期化:インスタンス作成時に自動的に呼ばれる
        super().__init__(name)    #Humanクラスのインスタンス変数 name を継承
        self.symptom = symptom
        self.patient_id = patient_id

class Clinic:
    def __init__(self,patient_list):
        self.patient_list = []

    def show_waiting_count(self):
        print(f'ただいまの待ち人数は{len(self.patient_list)}人です。')

    def reserve(self,patient):
        if self.

    def diagnosis(self):

    def _check_reserved(self):

        

    
