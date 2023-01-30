from validate_docbr import CPF, CNPJ


class Documento:
    
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError(
                'O documento está incorreto!'
            )

class DocCPF:
    
    def __init__(self, documento):
        if documento.valida():
            self.cpf = documento
        else:
            raise ValueError(
                'CPF inválido!'
            )

    def __str__(self):
        return format(self.documento)

    def valida(self):
        validador = CPF()
        return validador.validate(self.documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.documento)

class DocCNPJ:
    
    def __init__(self, documento):
        if documento.valida():
            self.cnpj = documento
        else:
            raise ValueError(
                'CNPJ inválido!'
            )

    def __str__(self):
        return format(self.documento)

    def valida(self):
        validador = CNPJ()
        return validador.validate(self.documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)
