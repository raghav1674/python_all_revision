class Patient:
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_ssn(self,ssn):
        self.__ssn=ssn
    def get_ssn(self):
        return self.__ssn
ram=Patient()
ram.set_id("P102")
ram.set_name("Ram")
ram.set_ssn("S102")
print("Patient I.D.:",ram.get_id(),"\nPatient Name:",ram.get_name(),"\nPatient ssn:",ram.get_ssn())