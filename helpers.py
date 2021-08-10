import re


class Helpers():
    def validar_cpf(cpf):
        cpf = ''.join(re.findall('\d', str(cpf)))

        if (not cpf) or (len(cpf) < 11):
            return False

        # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos que faltam
        inteiros = list(map(int, cpf))
        novo = inteiros[:9]

        while len(novo) < 11:
            r = sum([(len(novo) + 1 - i) * v for i, v in enumerate(novo)]) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            novo.append(f)

        # Se o número gerado coincidir com o número original, é válido
        if novo == inteiros:
            return True
        return False

    def validar_cnpj(cnpj):

        cnpj = ''.join(re.findall('\d', str(cnpj)))

        if (not cnpj) or (len(cnpj) < 14):
            return False

        # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
        inteiros = list(map(int, cnpj))
        novo = inteiros[:12]

        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        while len(novo) < 14:
            r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            novo.append(f)
            prod.insert(0, 6)

        # Se o número gerado coincidir com o número original, é válido
        if novo == inteiros:
            return True
        return False