import unittest
import os
from github import Github


class GithubTest(unittest.TestCase):

    def test_deve_retornar_todos_repos_do_usuario(self):
        usuario = 'willianresille'
        github = Github()
        repositorios = github.obter_repositorios_do(usuario)
        self.assertEqual(10, len(repositorios))

    def test_obter_dados_dos_repositorios(self):
        repo1 = {
            'name': 'repo1',
            'stargazers_count': 2,
            'language': 'python',
            'html_url': 'http://',
            'owner': {
                'login': 'usuario1'
            }
        }
        repositorios = [repo1]

        github = Github()
        resultado = github.obter_dados_dos(repositorios)
        dados = resultado[0]
        self.assertEqual(repo1.get('name'), dados.get('nome_repositorio'))
        self.assertEqual(repo1.get('stargazers_count'), dados.get('estrelas'))
        self.assertEqual(repo1.get('language'), dados.get('linguagem'))
        self.assertEqual(repo1.get('html_url'), dados.get('url_repositorio'))
        self.assertEqual(repo1.get('owner').get('login'), dados.get('usuario'))

    def test_converter_dados_para_salvar_no_csv(self):
        repositorios = [
            {
                'nome_repositorio': 'repo1',
                'estrelas': 2,
                'linguagem': 'python',
                'url_repositorio': 'http://',
                'usuario': 'usuario1'
            }
        ]
        github = Github()
        lista = github.converter_para_lista(repositorios)
        self.assertEqual(1, len(lista))
        primeiro = lista[0]
        self.assertEqual('repo1', primeiro[0])
        self.assertEqual(2, primeiro[1])
        self.assertEqual('python', primeiro[2])

    def test_deve_criar_arquivo_csv(self):
        nome_arquivo = '/tmp/repositorios.csv'
        conteudo = [['repo1', 2, 'python', 'http://', 'usuario1']]
        github = Github()
        arquivo_gerado = github.salvar(arquivo=nome_arquivo, conteudo=conteudo)
        self.assertTrue(os.path.exists(arquivo_gerado))



if __name__ == '__main__':
    unittest.main()
