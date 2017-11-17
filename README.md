Tutorial Mindu 1.0
==================
por José Falero

Nota: este tutorial é voltado a programadores que dominam a linguagem de programação Python.

Sobre o Mindu
-------------
Esta seção limita-se a uma rápida apresentação do Mindu; se você deseja apenas aprender a usá-lo, sinta-se à vontade para saltar direto para a seção seguinte.

O Mindu é uma ferramenta baseada em Pygame para desenvolvimento rápido e fácil de jogos 2D. Originalmente concebido com finalidades didáticas, embora o Mindu nem de longe seja a ferramenta Python mais poderosa voltada à programação de jogos 2D, possivelmente seja a mais fácil de aprender e usar, o que o torna ideal para inciantes na área de jogos, ou mesmo para programadores experientes que precisem desenvolver um projeto simples rapidamente.

Conforme dito, o Mindu é baseado em Pygame: isso significa que você precisa ter o pacote Pygame instalado em sua máquina para poder usar o Mindu. Mas é importante ressaltar desde já que o Mindu não foi projetado para ser usado com Pygame, e sim como uma alternativa ao Pygame. Em outras palavras, o Mindu não provê funcionalidades projetadas de modo que o seu código possa utilizá-las em conjunto com as funcionalidades nativas do Pygame: ou você desenvolve o seu jogo usando o Pygame diretamente, ou então o desenvolve usando o Mindu.

Ok, mas qual a diferença entre programar com Pygame e programar com Mindu? A resposta é simples: o Pygame é mais poderoso e genérico, ao passo que o Mindu é mais intuitivo e específico. Tudo o que você pode fazer com o Mindu, pode fazer também com o Pygame, mas nem tudo o que é possível fazer com o Pygame é possível fazer com o Mindu; por outro lado, o Mindu é mais fácil de aprender e usar, está mais em conformidade com o modelo e o estilo da programação em Python, além de o seu uso resultar em código mais conciso e limpo, o que representa boa economia de tempo e dor de cabeça. Na realidade, todas as diferenças fundamentais entre o Mindu e o Pygame refletem o fato de que quanto mais poderosa e genérica for uma ferramenta, maior será a curva de aprendizado para dominá-la.

No que diz respeito a desempenho, não há diferenças significativas entre o Mindu e o Pygame, especialmente em face da capacidade de processamento dos computadores modernos. Na verdade, como o Mindu é apenas uma fina camada de código Python em torno do próprio Pygame, quando o seu programa utiliza as funcionalidades do Mindu para realizar uma determinada tarefa, tudo o que ele faz é utilizar as funcionalidades mais adequadas do próprio Pygame para fazer as coisas acontecerem; o resultado é que o desempenho de algo feito a partir do Mindu será idêntico (ou pelo menos muito parecido) ao de algo feito diretamente com o Pygame. Afinal, como o poder do Pygame se deve justamente ao fato de ele ser bastante "cru", ao desenvolver algo utilizando-o diretamente, o programador se vê obrigado a implementar, por si mesmo, uma série de coisas que o Mindu já trás prontas; assim sendo, se você optar por desenvolver o seu jogo diretamente com o Pygame, em vez de usar o Mindu, existe uma grande probabilidade de você acabar implementando algo semelhante ao Mindu como parte central do seu projeto, o que, em termos de desempenho, daria no mesmo que usar o Mindu desde o começo.

### O Mindu requer
* Python 3.x (recomendado) ou Python 2.x (não-testado);
* Pygame >= 1.9.3 (recomendado) ou Pygame < 1.9.3 (não-testado).

O loop interno do Mindu
-----------------------
Os jogos digitais, ou pelo menos a grande maioria deles, são programas de computador que possuem em comum uma mesma estrutura básica: existe um loop, e o programa inteiro normalmente se divide em antes, durante e depois desse loop. Antes do loop, o programa costuma carregar arquivos de configuração, iniciar variáveis etc., preparando os dados e operações que serão necessários quando o loop começar a rodar. Então, durante o loop, uma determinada quantidade de comandos é executada repetidamente e de forma constante, com a velocidade de execução sob controle; nesse processo, imagens são desenhadas na tela, sons são reproduzidos, a entrada do usuário é lida através do teclado, do mouse, de dispositivos de joystick etc., tudo se repetindo uma vez a cada iteração do loop. E por fim, depois do loop, o programa costuma fazer operações de finalização, como salvar em disco o progresso feito no jogo ou informações sobre recordes atingidos etc.

Tirando proveito dessa estrutura básica da maioria dos jogos, o Mindu já vem com um loop interno previamente implementado, para que você não perca tempo implementando um por si mesmo em seu jogo. Esse loop é o coração do Mindu: compreender como ele funciona é a chave mais fundamental para compreender o funcionamento do próprio Mindu como um todo, e por essa razão este é o primeiro tópico abordado neste tutorial. Mas não se preocupe: conforme você vai descobrir a seguir, interagir com o loop interno do Mindu é uma tarefa notavelmente simples: acompanhe.

Para começar, o Mindu provê acesso ao seu loop interno através do objeto mindu.loop. Abaixo, você vê a lista completa dos métodos que compõem a sua interface:
```python
mindu.loop.start() -> None
mindu.loop.on_iterate(callable, *pargs, **kwargs) -> callable
mindu.loop.stop() -> None
mindu.loop.running() -> bool
mindu.loop.get_ips() -> int
mindu.loop.set_ips(ips) -> None
```
Trata-se de uma interface bem fácil de entender, como você pode ver: são apenas 6 métodos, cujos nomes já dão uma boa ideia de para que cada um deles serve. Vamos começar falando sobre o método start().

Conforme você deve supor, esse método é responsável por iniciar o loop interno do Mindu. Ele funciona como a função main() de outras bibliotecas: uma vez chamado este método, o loop interno do Mindu inicia-se e retém o fluxo de execução do programa, devolvendo-o ao seu código apenas quando algo o interrompe.

A estrutura básica comum dos jogos digitais, abordada ainda há pouco, assume a seguinte forma num programa que utiliza o Mindu:
1. importar o Mindu (import mindu), para ter-se acesso às suas funcionalidades;
2. usar as funcionalidades do Mindu para "modelar" o jogo;
3. iniciar o loop interno do Mindu com o método start() do objeto loop;
4. realizar tarefas de finalização depois que o loop interno do Mindu tiver devolvido o fluxo de execução.

Na verdade, a etapa 4, que normalmente implica em salvar dados em disco, é um assunto que foge completamente ao escopo deste tutorial, e portanto não será abordada aqui em nenhuma parte. E a etapa 2, que implica em conhecer as funcionalidades do Mindu para poder "modelar" o jogo, será abordada posteriormente. Por enquanto, como o objetivo desta seção é apenas ilustrar as formas de se interagir com o loop interno do Mindu, não convém ofuscar estas explicações com outros assuntos. Dito isso, vamos a um primeiro exemplo; abaixo, você vê o programa Mindu mais simples possível:
```python

import mindu

mindu.loop.start()
```
Se você executar esse código, verá que ele realmente funciona bem: uma janela se abre, com o título "Mindu Window" e com o ícone do Mindu, que é um peixe azul. A janela não apresenta qualquer conteúdo, mas responde bem quando o usuário tenta fechá-la: ela realmente se fecha, e o programa, então, termina.

Embora esse exemplo seja artificial ao extremo, ele serve para ilustrar alguma coisa. Por exemplo, você talvez esteja se perguntando como o Mindu foi capaz de criar uma janela, com título, ícone e tudo o mais, sem que as duas linhas de código mostradas tenham feito qualquer orientação nesse sentido. A verdade é que o Mindu não provê qualquer comando de criação de janela ou coisa parecida; em vez disso, a tela do jogo, que pode assumir a forma de uma janela ou ocupar o monitor inteiro (tela-cheia), sempre é criada automaticamente assim que o loop interno do Mindu começa a rodar, do mesmo modo que é destruída automaticamente sempre que o loop é interrompido por algum motivo. Portanto, a única forma de se criar uma tela, em modo janela ou em modo tela-cheia, é iniciando o loop interno do Mindu, e a única forma de fazê-la sumir é interrompendo-o. Mas não se engane: conforme você descobrirá mais tarde, o Mindu provê funcionalidades poderosas para lidar com a tela do jogo!

E por falar em tela, embora ela não seja o assunto aqui, vale a pena esclarecer um detalhe relacionado. No parágrafo anterior foi dito que a tela é destruída somente quando o loop interno do Mindu é interrompido, e isso é mais literal do que você talvez suponha. Por exemplo, o código de duas linhas apresentado inicia o loop interno do Mindu, o qual retém o fluxo de execução do programa, e uma tela em modo janela é criada automaticamente como efeito colateral; depois, quando o usuário tenta fechar essa janela, ela realmente se fecha, o loop interno do Mindu é interrompido e o fluxo de execução é devolvido ao script inicial. Bem, isso talvez tenha lhe dado a falsa impressão de que foi o fechamento da janela que ocasionou a interrupção do loop, em vez do contrário, mas se você pensa assim, está enganado. Na verdade, conforme você verá depois, o Mindu provê uma maneira de interceptar o momento em que o usuário tenta fechar a janela, de modo que você pode decidir o que vai acontecer como resultado disso; entretanto, como as duas linhas de código mostradas não estabelecem coisa alguma nesse sentido, a tela do Mindu adota o precedimento padrão, que é interromper o loop interno quando o usuário tenta fechá-la; então, no momento em que o loop é interrompido, a janela é destruída como um efeito colateral. Portanto, lembre-se sempre de que, do mesmo modo que o Mindu não provê um comando específico para a criação da janela, também não oferece nenhum para destruí-la.

Esse mecanismo, na realidade, é uma conveniência um tanto útil, e as coisas são assim justamente para facilitar a sua vida. O conceito por trás disso não poderia ser mais simples: sempre existe tela enquanto o loop roda, e nunca existe tela se o loop não estiver rodando; desse modo, você fica livre da digitação de código que seria necessária para fazer a tela surgir e desaparecer nos momentos corretos. Afinal de contas, no contexto de programação em que o Mindu procura ser útil de alguma forma, não faz sentido existir uma tela sem um loop rodando para desenhar coisas nela a todo instante, do mesmo modo que não faz sentido existir o loop e a tela não existir; com base nisso, o Mindu se encarrega de fazer a tela existir ou deixar de existir nos momentos apropriados.

Agora, vejamos o método on_iterate() em ação. Basicamente, o que esse método faz é cadastrar um objeto chamável qualquer para que seja chamado uma vez a cada iteração do loop interno do Mindu. Repare:
```python

import mindu

def imprime_spam():
    print("spam")

mindu.loop.on_iterate(imprime_spam)
mindu.loop.start()
```
Se você executar esse código, verá que, exatamente como aconteceu na execução do exemplo anterior, uma janela é aberta automaticamente, com o título "Mindu Window" e o ícone do Mindu. A diferença é que, desta vez, a string "spam" é impressa na saída padrão 60 vezes por segundo. Isso acontece porque o loop interno do Mindu, uma vez iniciado com o método start(), passa a fazer 60 iterações por segundo, e a cada iteração chama a função imprime_spam(), conforme havia sido instruído a fazer.

O método on_iterate() retorna de volta o mesmo objeto chamável que recebeu, para facilitar o seu uso como um decorador. Portanto, você poderia fazer o seguinte:
import mindu
```python
@mindu.loop.on_iterate
def imprime_spam():
    print("spam")

mindu.loop.start()
```
Na verdade, como o método on_iterate() aceita argumentos posicionais extras (*pargs) a serem repassados para o objeto chamável a cada chamada, o mais simples seria fazer o seguinte, caso realmente quiséssemos que a string "spam" fosse impressa uma vez a cada iteração:
```python
import mindu

# A cada iteração, chame print() e passe "spam" como argumento.
mindu.loop.on_iterate(print, "spam")
mindu.loop.start()
```
Argumentos de palavra-chave extras (**kwargs) também são suportados:
```python

import mindu

mindu.loop.on_iterate(print, "spam", "eggs", sep="\n", end="\n\n")
mindu.loop.start()
```
Claro que estamos vendo apenas exemplos artificiais aqui. Em casos reais, os objetos chamáveis passados para o método on_iterate() representam nada mais, nada menos que as próprias cenas dos jogos, porque, chamados constantemente no interior do loop interno do Mindu, são esses objetos que desenham imagens, rótulos e animações na tela, gerenciam a execução de áudio nos canais de som, processam a entrada do usuário através do teclado, do mouse, dos joysticks etc. Assim sendo, como um jogo normalmente é composto por várias cenas diferentes, o método on_iterate() pode ser chamado a qualquer momento para registrar um objeto chamável diferente, mesmo que o loop interno do Mindu já esteja rodando. Veja:
```python
import mindu

num = 1

def cena1():
    global num

    print(num)

    num += 1

    if num == 100:
        mindu.loop.on_iterate(cena2)

def cena2():
    global num

    print(num)

    num -= 1

    if num == 1:
        mindu.loop.on_iterate(cena1)

mindu.loop.on_iterate(cena1)
mindu.loop.start()
```
Na medida em que o seu jogo se tornar mais complexo, você pode começar a achar (e com razão) que é inconveniente manter os dados das cenas no espaço de nome global como foi feito nesse exemplo. Como programador Python, pelo menos uma vez na vida você já deve ter escrito "import this", e deve ter lido, entre outras coisas, a frase: "Namespaces are one honking great idea -- let's do more of those!".

Há pelo menos duas razões sérias para você não querer usar o espaço de nome global da forma mostrada. Em primeiro lugar, o código do seu jogo se tornaria uma bagunça em pouco tempo: se diversas cenas, cada qual com diversos elementos, mantiverem tudo o que necessitam no espaço de nome global, a tendência é o seu código tornar-se confuso e difícil de ler. Em segundo lugar, não convém ocupar a memória do computador com mais coisas do que o necessário: quando o seu código estiver usando centenas de imagens, animações e sons em cada cena, obviamente não será uma boa ideia carregar tudo de uma vez na memória e deixar armazenado no escopo global; em vez disso, o ideal é que cada cena, quando criada, carregue as coisas de que precisa, e que essas coisas desapareçam da memória junto com a cena, quando uma cena seguinte for criada. Bem, quando você estiver começando a ter essas preocupações, lembre-se de que o método on_iterate() não aceita apenas funções, e sim qualquer tipo de objeto chamável, inclusive classes. Veja:
```python
import mindu

@mindu.loop.on_iterate
class Cena1(object):

    def __init__(self):
        self.dados = "spam"
        mindu.loop.on_iterate(self.imprime_dados)

    def __del__(self):
        print("Cena 1 e seus dados varridos da memória!")

    def imprime_dados(self):
        print(self.dados)
        mindu.loop.on_iterate(Cena2)

class Cena2(object):

    def __init__(self):
        self.dados = "eggs"
        mindu.loop.on_iterate(self.imprime_dados)

    def __del__(self):
        print("Cena 2 e seus dados varridos da memória!")

    def imprime_dados(self):
        print(self.dados)

        # Não chame coisa alguma a cada iteração.
        mindu.loop.on_iterate(None)

mindu.loop.start()
```
Conforme você pode ver, o código a cima executa duas cenas distintas; cada uma delas guarda os seus dados como atributo da própria instância, de modo que os dados somem da memória junto com a instância quando a coleta de lixo do Python a atinge. Claro, no caso apresentado os dados são apenas strings simples, mas num caso real poderiam ser diversas imagens, animações e sons. Note, também, que a última cena, antes de sair, passa None como argumento para o método on_iterate(): isso restaura a rotina de callback padrão do loop interno do Mindu, que é nenhuma, ou seja, nenhum objeto é chamado a cada iteração.

Quanto maior for a sua intimidade com as técnicas de programação em Python, mais proveito você conseguirá tirar da interface provida pelo loop interno do Mindu. Abaixo, você vê outra maneira elegante de encapsular os dados de uma cena e garantir que eles só existam na memória enquanto a própria cena existe:
```python
import mindu

def cena():
    dados = "spam"

    for x in range(3):

        # Esperando 1 segundo.
        for x in range(60): yield

        print(dados)

    mindu.loop.on_iterate(None)
    yield

mindu.loop.on_iterate(next, cena())
mindu.loop.start()
```
Aqui, a cena é implementada com uma função geradora: quando chamada, essa função cria e retorna um objeto gerador, e é nesse momento que os dados da cena (a string "spam") são carregados na memória. O loop interno do Mindu, na verdade, é instruído a chamar a função next() do Python a cada iteração, passando como argumento o objeto gerador criado e retornado pela função. Por sua vez, o gerador, sempre que posto em funcionamento pela função next(), faz o que precisa fazer e devolve o fluxo de execução sem demora, com o comando yield.

Bem, explicar o protocolo e o funcionamento dos geradores do Python definitivamente não é um dos objetivos deste tutorial; entretanto, o exemplo mostrado ilustra uma coisa importante relacionada ao loop interno do Mindu.

Conforme você já deve ter começado a reparar, o Mindu se esforça para realizar o máximo de trabalho genérico automaticamente, para que você não tenha que perder tempo implementando coisas básicas e possa se manter focado única e exclusivamente na lógica do seu jogo em particular. E, na medida em que você avançar neste tutorial, perceberá claramente que todas as funcionalidades providas pelo Mindu refletem esse propósito de tornar as coisas o mais simples possível para você. Entretanto, para que essas funcionalidades respondam de maneira adequada, o loop interno do Mindu precisa rodar livremente, pois é o centro do sistema inteiro, responsável por manter tudo funcionando bem. Em outras palavras, o loop não é apenas um timer que se limita a chamar periodicamente os objetos chamáveis designados por você: a cada iteração, ele também realiza um bocado de trabalho por baixo dos panos para manter atualizadas todas as funcionalidades que o Mindu disponibiliza. Assim sendo, você não deve, em hipótese alguma, criar delays manuais que impeçam o loop interno do Mindu de rodar livremente, e é por isso que o exemplo apresentado a cima devolve o fluxo de execução 60 vezes seguidas com o comando yield, como forma de simular 1 segundo de inatividade, já que o loop interno do Mindu faz 60 iterações por segundo.

Para ficar mais claro, veja no código abaixo o que você jamais deve fazer:
```python
import time
import mindu

@mindu.loop.on_iterate
def cena():
    time.sleep(5)
    print("spam")

mindu.loop.start()
```
Esse código imprime a string "spam" a cada 5 segundos. O problema é que, durante os 5 segundos de inatividade, o fluxo de execução fica retido na função sleep(), sem que o loop interno do Mindu possa trabalhar. O resultado é que o seu programa ficará congelado durante os 5 segundos: não será possível fechar a janela, não será possível ativar ou desativar a tela-cheia, não será possível reproduzir sons, não será possível desenhar imagens etc. O seu código pode ficar 5 segundos sem fazer nada, claro, mas precisa manter o loop interno do Mindu rodando livremente. Para isso, basta lembrar que o loop faz 60 iterações por segundo, ou seja, 300 iterações a cada 5 segundos. Veja:
```python
import mindu

dormir = 300

@mindu.loop.on_iterate
def cena():
    global dormir

    if dormir:
        dormir -= 1
        return

    dormir = 300
    print("spam")

mindu.loop.start()
```
Esse código, sim, imprime a string "spam" a cada 5 segundos da maneira correta, ou seja, sem impedir o loop interno do Mindu de trabalhar.

Bem, agora que já sabe como usar o método on_iterate() para que o seu código seja executado a cada iteração do loop interno do Mindu, saiba que o método start() não suporta recursividade, ou seja, você não pode iniciar o loop mais de uma vez. Isso significa que um erro será propagado se você tentar fazer o seguinte:
```python
import mindu

@mindu.loop.on_iterate
def cena():
    mindu.loop.start()

mindu.loop.start()
```
Conforme você viu, a abordagem dos métodos start() e on_iterate(), além de ilustrar o funcionamento desses métodos em particular, também trouxe um panorama geral sobre o loop interno do Mindu. Assim sendo, agora estamos livres para abordar os métodos restantes com muito menos explicações. Acompanhe:

O método stop() serve para interromper o loop:
```python
import mindu

dormir = 180

@mindu.loop.on_iterate
def cena():
    global dormir

    if dormir:
        dormir -= 1
        return

    mindu.loop.stop()

mindu.loop.start()
```
Mas, da mesma forma que você não pode chamar start() se o loop estiver rodando, também não pode chamar stop() se o loop estiver parado. Logo, o código abaixo propaga um erro:
```python
import mindu

mindu.loop.stop()
```
O método running() retorna True se o loop estiver rodando, e False caso contrário:
```python
import mindu

print(mindu.loop.running())

@mindu.loop.on_iterate
def cena():
    print(mindu.loop.running())
    mindu.loop.stop()

mindu.loop.start()

print(mindu.loop.running())
```
O método get_ips() retorna um inteiro, indicando quantas iterações por segundo o loop interno do Mindu faz. Até aqui, vem sendo dito que o loop faz 60 iterações por segundo, mas isso é apenas o padrão; na realidade, a taxa de iterações por segundo é personalizável, e o método get_ips() permite verificá-la a qualquer momento, esteja o loop rodando ou não:
```python
import mindu

print(mindu.loop.get_ips())

@mindu.loop.on_iterate
def cena():
    print(mindu.loop.get_ips())
    mindu.loop.stop()

mindu.loop.start()

print(mindu.loop.get_ips())
```
E por fim, o método set_fps() serve para definir quantas iterações por segundo o loop interno do Mindu deve fazer, e também pode ser chamado a qualquer momento, esteja o loop rodando ou não:
```python
import mindu

mindu.loop.set_ips(30)

def cena():
    for x in range(3):
        # Esperando 1 segundo.
        for x in range(30): yield
        print("spam")

    mindu.loop.set_ips(60)

    for x in range(3):
        # Esperando 0,5 segundo.
        for x in range(30): yield
        print("eggs")

    mindu.loop.on_iterate(None)
    yield

mindu.loop.on_iterate(next, cena())
mindu.loop.start()
```
E isso é tudo o que há para saber sobre o loop interno. Agora, vejamos como você faz para processar a entrada do usuário utilizando o Mindu.

Teclado, mouse e joysticks

Vamos começar falando do teclado.

Assim como o Mindu provê acesso ao seu loop interno através do objeto mindu.loop, também provê acesso ao teclado do computador através de um objeto: trata‑se do objeto mindu.keyboard. Abaixo, você vê a lista completa dos métodos que compõem a sua interface:
```python
mindu.keyboard.get_symbols() -> tuple
mindu.keyboard.busy(symbol) -> bool
mindu.keyboard.ding(symbol) -> bool
mindu.keyboard.dong(symbol) -> bool
mindu.keyboard.time(symbol) -> int
mindu.keyboard.get() -> str ou None
mindu.keyboard.on_ding(callable, *pargs, **kwargs) -> callable
mindu.keyboard.on_dong(callable, *pargs, **kwargs) -> callable
```
Como você pode ver, são apenas 8 métodos, todos eles muito fáceis de entender.

Para início de conversa, você precisa ter em mente que os dispositivos de entrada possuem símbolos associados aos seus elementos. No caso do teclado, cujos elementos são teclas, cada tecla possui um símbolo associado para identificá-la. Esses símbolos são apenas strings simples. Por exemplo, a tecla ESPAÇO é identificada pelo símbolo "space", a tecla A é identificada pelo símbolo "a" etc. O método get_symbols() retorna uma tupla com todos os símbolos do teclado. Faça o teste:
```python
import mindu

print(mindu.keyboard.get_symbols())
```
O método busy() recebe um símbolo e retorna True se a tecla correspondente estiver ocupada, isto é, pressionada; caso contrário, retorna False:
```python
import mindu

@mindu.loop.on_iterate
def cena():
    if mindu.keyboard.busy("space"):
        print("a tecla ESPAÇO está pressionada")

mindu.loop.start()
```
O método ding() recebe um símbolo e retorna True se a tecla correspondente tornou-se ocupada, isto é, desceu; caso contrário, retorna False:
```python
import mindu

@mindu.loop.on_iterate
def cena():
    if mindu.keyboard.ding("space"):
        print("a tecla ESPAÇO desceu")

mindu.loop.start()
```
O método dong() recebe um símbolo e retorna True se a tecla correspondente tornou-se desocupada, isto é, subiu; caso contrário, retorna False:
```python
import mindu

@mindu.loop.on_iterate
def cena():
    if mindu.keyboard.dong("space"):
        print("a tecla ESPAÇO subiu")

mindu.loop.start()
```
O método time() recebe um símbolo e retorna um inteiro indicando há quantos milissegundos a tecla correspondente está pressionada:
```python
import mindu

@mindu.loop.on_iterate
def cena():
    tempo = mindu.keyboard.time("space")
    print("a tecla ESPAÇO está pressionada há {} milissegundos".format(tempo))

mindu.loop.start()
```
O método get() retorna o símbolo da tecla que tornou-se ocupada, isto é, desceu, ou retorna None se nenhuma tecla tornou-se ocupada:
```python
import mindu

@mindu.loop.on_iterate
def cena():
    s = mindu.keyboard.get()
    if s is None: return
    print("a tecla {} foi pressionada".format(s))

mindu.loop.start()

O método on_ding() exige um pouco mais de explicação. Para ilustrar a utilidade desse método, suponha que você queira que o seu jogo imprima a string "spam" sempre que a tecla ESPAÇO for pressionada. Naturalmente, isso seria possível com o método ding(), conforme você vê no código abaixo:
```python
import mindu

@mindu.loop.on_iterate
def cena():
    if mindu.keyboard.ding("space"):
        print("spam")

mindu.loop.start()
```
O código a cima funciona bem. Entretanto, se você deseja esse comportamento em todas as cenas do seu jogo, quanto mais cenas o seu jogo possuir, mais inconveniente se tornará o uso de ding(), pois o código de teste precisará estar presente em todas elas. É aí que entra o método on_ding(), que funciona de forma idêntica ao método on_iterate() do objeto loop. Basicamente, o que on_ding() faz é cadastrar um objeto chamável para que seja chamado sempre que uma tecla se torna ocupada, isto é, desce. O objeto chamável precisa aceitar chamadas com pelo menos 1 argumento, para receber o símbolo da tecla que tornou-se ocupada. Na prática, é muito simples, veja:
```python
import mindu

@mindu.keyboard.on_ding
def imprime_spam(s):
    if s == "space":
        print("spam")

def cena1():
    print("iniciando cena 1")

    for x in range(180): yield

    mindu.loop.on_iterate(next, cena2())
    yield

def cena2():
    print("iniciando cena 2")

    for x in range(180): yield

    mindu.loop.on_iterate(next, cena1())
    yield

mindu.loop.on_iterate(next, cena1())
mindu.loop.start()
```
O código a cima alterna entre duas cenas. Cada uma delas dura três segundos, e, não importando qual delas seja a cena atual, a string "spam" é impressa sempre que a tecla ESPAÇO é pressionada. Isso acontece porque, independente da cena corrente, o objeto keyboard chama a função imprime_spam() sempre que uma tecla é pressionada, e lhe passa como argumento o símbolo correspondente; a função imprime_spam(), por sua vez, verifica se o símbolo recebido corresponde à tecla ESPAÇO, e imprime a string "spam" em caso positivo.

Do mesmo modo que o método on_iterate() do objeto loop, o método on_ding() também retorna de volta o mesmo objeto chamável que recebeu, para facilitar o seu uso como um decorador, exatamente como foi feito no exemplo a cima. Além disso, on_ding() também aceita argumentos posicionais extras (*pargs) e argumentos de palavra-chave extras (**kwargs):
```python
import mindu

mindu.keyboard.on_ding(print, "spam", "eggs", sep="\n", end="\n\n")
mindu.loop.start()
```
E por fim, o método on_dong(), que funciona da mesma maneira que on_ding(). A única diferença é que on_dong() cadastra um objeto chamável para que seja chamado sempre que uma tecla se torna desocupada, em vez de ocupada:
```python
import mindu

mindu.keyboard.on_dong(print, "spam", "eggs", sep="\n", end="\n\n")
mindu.loop.start()
```
E isso é tudo o que há para saber sobre o teclado, de modo que podemos passar aos joysticks.

O Mindu provê a tupla mindu.joysticks. Cada objeto presente nessa tupla representa um dos dispositivos de joystick que estava conectado ao computador no momento em que o Mindu foi importado pela primeira vez. Se essa tupla estiver vazia, significa que não havia nenhum dispositivo de joystick conectado ao computador quando o Mindu foi importado pela primeira vez.

Antes de falar sobre os joysticks em si, saiba que o Mindu provê a função mindu.reload_joysticks(). Essa função permite a você recarregar os dispositivos de joystick conectados ao computador, sem a necessidade de reiniciar o programa. Para ficar claro, execute o código abaixo sem nenhum joystick conectado ao computador. Depois, quando o código já estiver rodando, conecte um joystick ao computador e pressione a tecla ESPAÇO no teclado:
```python
import mindu

print("joysticks: {}".format(mindu.joysticks))

@mindu.loop.on_iterate
def cena():
    if mindu.keyboard.ding("space"):
        mindu.reload_joysticks()
        print("joysticks: {}".format(mindu.joysticks))

mindu.loop.start()
```
Como o Mindu expõe os joysticks em uma tupla, naturalmente tudo o que você precisa fazer para acessar um determinado joystick é indexar a tupla. Por exemplo:
```python
import mindu

joy = mindu.joysticks[0]
print(joy)
```
Agora, uma boa notícia: absolutamente tudo o que foi dito sobre o teclado funciona da mesma maneira com todo e qualquer joystick. Ou seja, a interface dos joysticks é exatamente igual à do teclado, de modo que todos os exemplos mostrados com o teclado funcionam do mesmo modo com os joysticks, exceto pelo fato de que cada joystick possui seus próprios símbolos, de acordo com os seus elementos. E, para saber quais são os símbolos de um determinado joystick, basta usar o mesmo método get_symbols() que já usamos com o teclado. Veja:
```python
import mindu

joy = mindu.joysticks[0]

print(joy.get_symbols())
```
Sinta-se à vontade para refazer todos os testes mostrados com o teclado, desta vez usando um joystick: você verá que, de fato, tudo funciona da mesmíssima maneira. E essa é realmente uma notícia muito boa: o fato de o teclado e os joysticks poderem ser tratados de maneira idêntica facilita a sua vida na hora de escrever código genérico para processar a entrada do usuário, independente do dispositivo através do qual ocorra essa entrada. Veja:
```python
import mindu

joy = mindu.joysticks[0]

def cena_escolhe_disp():
    tecla = mindu.keyboard.get()
    if tecla == "j": disp = joy
    elif tecla == "t": disp = mindu.keyboard
    else: return
    print("Dê um comando no dispositivo escolhido...")
    mindu.loop.on_iterate(cena_escolhe_cmd, disp)

def cena_escolhe_cmd(disp):
    cmd = disp.get()
    if cmd is None: return
    print("Ok, agora, repita o comando...")
    mindu.loop.on_iterate(cena_spam, disp, cmd)

def cena_spam(disp, cmd):
    if disp.get() == cmd: print("spam")

print("Pressione J para usar o joystick 0, ou T para usar o teclado...")
mindu.loop.on_iterate(cena_escolhe_disp)
mindu.loop.start()
```
É sempre bom lembrar que estamos vendo exemplos artificiais aqui. Em um caso real, como um jogo de luta, os lutadores poderiam ser instâncias de uma classe comum; para criar um novo lutador, o construtor dessa classe poderia receber como argumentos um dispositivo de entrada qualquer seguido de uma lista de símbolos, um para cada ação do lutador; depois, um método de atualização poderia facilmente processar a entrada do usuário, sem a menor preocupação com o fato de que o usuário pode estar jogando através do teclado ou de um joystick.

Você deve ter reparado que foi mostrada uma lista completa dos métodos de teclado, mas não foi mostrada nenhuma lista com métodos de joystick. A razão é óbvia: os joysticks possuem todos os 8 métodos que o teclado possui, e que já haviam sido mostrados. Entretanto, há 1 método que os joysticks possuem, e o teclado não: trata-se do método get_name(), cujo nome já diz tudo. Repare:
```python
import mindu

print(mindu.joysticks[0].get_name())
```
Conforme você deve imaginar, o método get_name() apenas retorna uma string, representando o nome do dispositivo de joystick.

Agora, vamos falar sobre o mouse. Para começar, saiba que o mouse também é provido através de um objeto: o objeto mindu.mouse. E, sim, todos os 8 métodos que o teclado e os joysticks possuem em comum (busy(), ding(), dong() etc.), o mouse também possui. Contudo, se os joysticks possuem 1 método exclusivo, que é o get_name(), eis que o mouse possui 10 métodos exclusivos! Mas não se preocupe: todos eles são notavelmente simples e fáceis de entender. Abaixo, a lista:
```python
mindu.mouse.get_cursor() -> Image
mindu.mouse.set_cursor(cursor) -> None
mindu.mouse.get_visible() -> bool
mindu.mouse.set_visible(visible) -> None
mindu.mouse.toggle_visible() -> None
mindu.mouse.get_position() -> tuple
mindu.mouse.set_position(position) -> None
mindu.mouse.idle() -> bool
mindu.mouse.get_idle_time() -> int
mindu.mouse.set_idle_time(time) -> None
```
O método get_cursor() obtém o cursor do mouse como um objeto Image do Mindu (os objetos Image serão abordados na seção seguinte).
```python
import mindu

print(mindu.mouse.get_cursor())
```
O método set_cursor() é o contrário: recebe como argumento um objeto Image para definir o cursor do mouse. O argumento também pode ser None para restaurar o cursor padrão.
```python
import mindu

mindu.mouse.set_cursor(mindu.Image("imagem.png"))
```
O método get_visible() retorna True se o cursor do mouse estiver visível, e False caso contrário.
```python
import mindu

print(mindu.mouse.get_visible())
```
O método set_visible() é o contrário: recebe True ou False para tornar o cursor do mouse visível ou invisível.
```python
import mindu

mindu.mouse.set_visible(False)
print(mindu.mouse.get_visible())
```
O método toggle_visible() alterna o cursor do mouse entre visível e invisível.

import mindu

mindu.mouse.toggle_visible()
print(mindu.mouse.get_visible())
mindu.mouse.toggle_visible()
print(mindu.mouse.get_visible())
```
O método get_position() retorna uma tupla de inteiros (x, y) representando as coordenadas X e Y da posição do cursor do mouse.
```python
import mindu

@mindu.loop.on_iterate
def cena(): print(mindu.mouse.get_position())

mindu.loop.start()
```
O método set_position() é o contrário: recebe uma lista ou tupla de inteiros (x, y) para definir a posição do cursor do mouse.
```python
import mindu

print("pressione uma tecla para fechar a janela")

@mindu.loop.on_iterate
def cena():
    mindu.mouse.set_position([10, 10])
    if mindu.keyboard.get(): mindu.loop.stop()

mindu.loop.start()
```
O método idle() retorna True se o cursor do mouse está ocioso, isto é, se não se movimenta há um determinado tempo, e retorna False caso contrário. Você pode usar isso para implementar dicas de ferramenta que só surgem na tela quando o cursor do mouse fica parado sobre um elemento de GUI, por exemplo. Outra utilidade é fazer o cursor do mouse desaparecer quando fica muito tempo parado. Por padrão, o cursor do mouse é considerado ocioso a partir de 500 milissegundos sem se mover, mas esse tempo pode ser personalizado.
```python
import mindu

@mindu.loop.on_iterate
def cena():
    if mindu.mouse.idle(): mindu.mouse.set_visible(False)
    else: mindu.mouse.set_visible(True)

mindu.loop.start()
```
O método get_idle_time() retorna um inteiro, indicando a partir de quantos milissegundos sem se mover o cursor do mouse é considerado ocioso.
```python
import mindu

print(mindu.mouse.get_idle_time())
```
O método set_idle_time() é o contrário: recebe um inteiro para definir a partir de quantos milissegundos sem se mover o cursor do mouse passará a ser considerado ocioso.
```python
import mindu

print(mindu.mouse.get_idle_time())
mindu.mouse.set_idle_time(1000)
print(mindu.mouse.get_idle_time())
```
E isso é tudo o que há para saber sobre os dispositivos de entrada. Agora, vejamos como você desenha coisas na tela utilizando o Mindu.

Imagens, animações e rótulos

O Mindu oferece 3 tipos de sprites, isto é, objetos que podem ser desenhados na tela: Image, Animation e Label. Todos os 3 possuem várias funcionalidades, conforme você verá, mas, assim como tudo o que já foi apresentado até aqui, as funcionalidades dos sprites também são muito intuitivas e fáceis de compreender.

Vamos começar falando do objeto Image. Abaixo, você vê a lista completa de métodos e propriedades que compõem a sua interface:
```python
mindu.Image(file, alpha=True, osd=False, **position) -> Image
mindu.Image.grab(sprite) -> tuple
mindu.Image.contains(sprite) -> bool
mindu.Image.collide(sprite) -> bool
mindu.Image.collide_point(point) -> bool
mindu.Image.move(x, y) -> None
mindu.Image.get_osd() -> bool
mindu.Image.set_osd(osd) -> None
mindu.Image.toggle_osd() -> None
mindu.Image.copy() -> Image
mindu.Image.flip(hbool, vbool) -> Image
mindu.Image.resize(size) -> Image
mindu.Image.rotate(angle) -> Image
mindu.Image.scale(scale) -> Image
mindu.Image.width -> int, somente leitura
mindu.Image.height -> int, somente leitura
mindu.Image.size -> tuple, somente leitura
mindu.Image.top -> int, leitura e escrita
mindu.Image.left -> int, leitura e escrita
mindu.Image.bottom -> int, leitura e escrita
mindu.Image.right -> int, leitura e escrita
mindu.Image.centerx -> int, leitura e escrita
mindu.Image.centery -> int, leitura e escrita
mindu.Image.topleft -> tuple, leitura e escrita
mindu.Image.bottomleft -> tuple, leitura e escrita
mindu.Image.bottomright -> tuple, leitura e escrita
mindu.Image.topright -> tuple, leitura e escrita
mindu.Image.midtop -> tuple, leitura e escrita
mindu.Image.midleft -> tuple, leitura e escrita
mindu.Image.midbottom -> tuple, leitura e escrita
mindu.Image.midright -> tuple, leitura e escrita
mindu.Image.center -> tuple, leitura e escrita
```
