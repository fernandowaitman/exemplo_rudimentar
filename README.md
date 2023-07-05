Exemplo Rudimentar
==================

A ideia deste projeto é exemplificar, em português, uma estrutura básica - mas
bem básica mesmo - de projeto Python, contendo os arquivos e instruções 
essenciais para o seu entendimento, instalação e execução.

Propositalmente, ele ainda não dispõe de mecanismos de empacotamento
(setup.py, etc.), pois isso tornaria o exemplo mais complexo, e portanto, de
mais difícil compreensão para pessoas iniciantes.

O código envolvido não tem qualquer propósito, exceto depender de libs que 
requerem instalação para que funcione (ou seja, para que funcione é necessário
instalar adequadamente o projeto).


Funcionalidades
---------------

Há duas funções disponíveis, ambas devidamente documentadas no arquivo
[exemplo_rudimentar.py]:

* desloca_data_por_uma_quantidade_de_meses(qtde_meses, data=None)
* gera_e_imprime_dicionario_a_partir_de_xml(xml=xml_exemplo)


Requisitos
----------

* Python 3+
* lib python{X}-venv


Instalação
----------

```bash
make install
```


Execução
--------

```bash
make run
```


Make
----
* `install`: cria um virtual environment, e instala nele as libs necessárias.
* `run`: executa o projeto no virtual environment criado.
* `clean`: remove o __pycache__, e também o virtual environment criado.


  [exemplo_rudimentar.py]: https://github.com/fernandowaitman/exemplo_rudimentar/blob/master/exemplo_rudimentar.py