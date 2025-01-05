def notas(*num, sit=False):
    """
    -> Função para analisar notas e situação de alunos.
    :param num: Uma ou mais notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou não mostrar a situação dos alunos.
    :return: dicionario com as informações.
    """
    resp = {}
    resp['total'] = len(num)
    for i, v in enumerate(num):
        if i == 0:
            resp['maior'] = resp['menor'] = v
        elif v > resp['maior']:
            resp['maior'] = v
        elif v < resp['menor']:
            resp['menor'] = v
    resp['media'] = sum(num) / len(num)
    if sit:
        if resp['media'] <= 5:
            resp['situação'] = 'ruim'
        elif 5 < resp['media'] < 8:
            resp['situaçâo'] = 'Razoável'
        else:
            resp['situaçâo'] = 'Ótima'

    return resp


resp = notas(5.5, 2.5, 10, 6.5)
help(notas)
