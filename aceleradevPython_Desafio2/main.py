import abc


class Department:
    '''
    Classe para definir nome e o codigo de cada departamento
    '''
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC):
    '''
    Utilizando Abstract Base Classes para tornar a classe abstrata
    e impedir de ser instanciada diretamente
    '''
    @abc.abstractmethod
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        
    def calc_bonus(self):
       return self.salary * 0.15

    def get_hours(self):
        return 8

'''
Ao adicionar uma classe como parametro, acaba fazendo a herança, 
a Classe Manager vai herdar os atributos e metodos da classe Employee
'''
class Manager(Employee):
    '''
    utiliza o __init__ para iniciar o construtor da classe e receber os 
    parametros
    '''
    def __init__(self, code, name, salary): 
        '''
        super evidencia a Classe Mae e os parametros que vao ser herdados
        a utilização de __ antes do atributo faz com que ele se torne 
        mais protegido, e só podera ser acessado a partir do metodo associado 
        a classe que sera instanciada ex: __departament
        '''
        super().__init__(code, name, salary) 
        self.__departament = Department('managers', 1)
    
    
    def get_departament(self):
        return self.__departament.name
    
    def set_department(self,name,code):
        self.name = name
        self.code = code
        self.__departament = Department(name,code)
        return self.__departament
    

class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self,valor):
        self.__sales += valor
        return self.__sales

    def calc_bonus(self):
        return self.__sales * 0.15
    
    
    def get_departament(self):
        return self.__departament.name
    
    def set_department(self,name):
        self.__departament.name = name
        





