from urllib import request, parse
import json
import csv
import sys


class Github:

    def obter_repositorios_do(self, usuario):
        url = 'https://api.github.com/users/%s/repos' % usuario

        req = request.Request(url, headers={})
        with request.urlopen(req) as response:
            resp = response.read()
            conteudo = json.loads(resp)

        return conteudo

    def obter_dados_dos(self, repositorios):
        resultado = []
        for repositorio in repositorios:
            dados = {
                'nome_repositorio': repositorio.get('name'),
                'estrelas': repositorio.get('stargazers_count'),
                'linguagem': repositorio.get('language'),
                'url_repositorio': repositorio.get('html_url'),
                'usuario': repositorio.get('owner').get('login')
            }
            resultado.append(dados)
        return resultado

    def converter_para_lista(self, repositorios):
        lista = []
        for repositorio in repositorios:
            repos = [
                repositorio.get('nome_repositorio'),
                repositorio.get('estrelas'),
                repositorio.get('linguagem'),
                repositorio.get('url_repositorio'),
                repositorio.get('usuario'),
            ]
            lista.append(repos)
        return lista

    def salvar(self, **kwargs):
        arquivo = kwargs.get('arquivo')
        conteudo = kwargs.get('conteudo')

        with open(arquivo, 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(conteudo)

        return arquivo 


if __name__ == '__main__':
    try:
        usuario = sys.argv[1]
        github = Github()
        repositorios_github = github.obter_repositorios_do(usuario)
        repositorios = github.obter_dados_dos(repositorios_github)
        # import ipdb; ipdb.set_trace()
        lista_convertida = github.converter_para_lista(repositorios)
        arquivo_gerado = github.salvar(arquivo='/tmp/repositorios.csv', conteudo=lista_convertida)
        print('Foi gerado o arquivo %s' % arquivo_gerado)
    except Exception as e:
        print('Deu erro. %s' % e)

        


