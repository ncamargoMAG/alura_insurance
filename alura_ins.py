import pandas as pd

class Afiliado:
    def __init__(self, nome, sobrenome, nascimento, cpf, rg, endereco, contato):
        self.nome= nome.title()
        self.sobrenome= sobrenome.title()
        self._nascimento=nascimento.datatime()
        self.cpf=cpf
        self._rg=rg
        self.endereco=endereco
        self.contato=contato
    
    
    def nome_completo(self): 
        return f"{self.nome} {self.sobrenome}"
    
    @property
    def nascimento(self):
        return self._nascimento
    
    @property
    def rg(self):
        return self._rg
    


class ContaSegurado(Afiliado):
    def __init__(self, nome, sobrenome, nascimento, cpf, rg, endereco, contato,beneficiarios):
        self.beneficiarios = beneficiarios
        Afiliado.__init__(self, nome, sobrenome, nascimento, cpf, rg, endereco, contato)
        
class ContaBeneficiario(Afiliado):
    def __init__(self, nome, sobrenome, nascimento, cpf, rg, endereco, contato, tipo):
        self._tipo=tipo
        Afiliado.__init__(self, nome, sobrenome, nascimento, cpf, rg, endereco, contato)
        
class Apolice:
    def __init__(self,numero,tipo,valor_beneficio,segurado,corretor,vigencia,datadecriacao,status):
        self._numero=numero
        self._tipo=tipo
        self._valor_beneficio=valor_beneficio
        self._segurado=segurado
        self._corretor=corretor
        self._vigencia=vigencia
        self._datadecriacao=datadecriacao
        self._status=status        
                
class Corretor(Afiliado):
    def __init__(self, nome, sobrenome, NumeroSusep, apolices, contato):
        super().__init__(self, nome, sobrenome)
        self.NumeroSusep=NumeroSusep
        self.apolices=apolices
        self.contato=contato        
        
seg1=ContaSegurado("Lucio","Almeida","23/07/1982","51432875526","198919788","Rua Naoseioque, 12", "11987654321", "Cezar Almeida")
Benef=ContaBeneficiario("Cezar","Almeida","23/07/2002","51432875527","198919789","Rua Naoseioque, 12", "11987654322", "Filho")

seg1.nome_completo()
Benef.nome_completo()

clientes=[seg1,Benef]

for Afiliado in clientes:
    detalhes = Afiliado.beneficiarios if hasattr(Afiliado, 'beneficiarios') else Afiliado._tipo
    print(f'Nome: {Afiliado.nome_completo()} - Data de Nascimento: {Afiliado.nascimento} - CPF: {Afiliado.cpf} - RG: {Afiliado.rg} - Endereço: {Afiliado.endereco} - Contato: {Afiliado.contato} - {detalhes}')

apol1=Apolice("3214687","VIDA","500000","José Silva","Jonas Macedo","24/03/2024","11/03/2016","ATIVA")
apol2=Apolice("3215688","CARRO","300000","José Silva","Jonas Macedo","24/03/2024","11/03/2016","ATIVA")




