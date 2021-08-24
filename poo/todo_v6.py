#!python
# ---------- Conceito de Metodos Privados ---------#
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # Todo metodo privado comeca com '_'
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        # Se tarefa for do tipo Tarefa, ele chama _add_tarefa se nao chama _add_nova_tarefa
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possicel IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome}, ({len(self.pendentes())} tarefa(s) pendente(s)).'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append(' (Concluida)')
        elif self.vencimento:
            if datetime.now() >= self.vencimento:
                status.append(' (Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f' (Vence em {dias} dias)')

        return f'{self.descricao}' + ' '.join(status)

# ---- HERANÇA ---- #


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        # Soma o vencimento aos dias passados como parametro, por padrão é 7
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa.add(TarefaRecorrente('Trocar lencois', datetime.now(), 7))
    casa.add(casa.procurar('Trocar lencois').concluir())
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'-{tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Fruitas secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, seconds=1))
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()

    for tarefa in mercado:
        print(f'-{tarefa}')

    print(mercado)


if __name__ == '__main__':
    main()
