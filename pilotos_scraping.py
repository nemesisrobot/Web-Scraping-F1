from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import scripts.parserDadosHTMLJSON as parser
import scripts.persistindoDadosNoBanco as salva
    
#criando dicionario com property de agent
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

#criando lista com nome dos pilotos
pilotosnomes = []

#fazendo append de todos os pilotos
pilotosnomes.append('alexander-albon')
pilotosnomes.append('valtteri-bottas')
pilotosnomes.append('pierre-gasly')
pilotosnomes.append('antonio-giovinazzi')
pilotosnomes.append('romain-grosjean')
pilotosnomes.append('lewis-hamilton')
pilotosnomes.append('daniil-kvyat')
pilotosnomes.append('nicholas-latifi')
pilotosnomes.append('charles-leclerc')
pilotosnomes.append('lando-norris')
pilotosnomes.append('kevin-magnussen')
pilotosnomes.append('esteban-ocon')
pilotosnomes.append('sergio-perez')
pilotosnomes.append('kimi-raikkonen')
pilotosnomes.append('daniel-ricciardo')
pilotosnomes.append('george-russell')
pilotosnomes.append('carlos-sainz')
pilotosnomes.append('lance-stroll')
pilotosnomes.append('max-verstappen')
pilotosnomes.append('sebastian-vettel')

try:
    for piloto in pilotosnomes:
        
        #coletando dados do pilo
        requisicao = Request('https://www.formula1.com/en/drivers/{}.html'.format(piloto), headers = header)
        resposta = urlopen(requisicao)
        html = BeautifulSoup(resposta, 'html.parser')

        #filtrando tags html para os dados
        cabecalho = html.findAll('th', {'class':'stat-key'})
        corpo = html.findAll('td', {'class':'stat-value'})


        #criando lista com dados de cabeçalho
        dadoscabecalho = []

        #criando lista com dados de corpo
        dadoscorpo = []

        #integrage em cima de dados
        def interacao(dadoshtml, listadados):
            for dado in dadoshtml:
                listadados.append((dado.getText()).replace('\n',''))


        interacao(cabecalho, dadoscabecalho)
        interacao(corpo, dadoscorpo)

        info=parser.parserDados(dadoscorpo, dadoscabecalho)

        arquivo = open('{}.json'.format(piloto), 'w')
        salva.salvaDadosNaBase(info)
        arquivo.write(str(info))
        arquivo.close()
        
except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)

