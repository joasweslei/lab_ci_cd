# Laboratório de CI/CD: Automatizando a Classe Aluno

Bem-vindo ao Lab de Engenharia de Software! Hoje vamos implementar um pipeline de CI (Integração Contínua) utilizando **GitHub Actions**.

## O Desafio
Você tem uma classe `Aluno` que calcula a aprovação. Seu objetivo é garantir que nenhuma alteração seja aceita no projeto sem antes passar pelos nossos testes automatizados.

### Passos:
1. **Fork:** Faça um fork deste repositório para o seu GitHub.
2. **Setup:** Instale as dependências localmente: `pip install pytest`.
3. **Teste:** Execute `pytest` no terminal para garantir que tudo está ok.
4. **Pipeline:** Crie um arquivo em `.github/workflows/ci.yml` que execute os testes automaticamente a cada `push`.
5. **Proteção:** Configure a `branch protection rule` na aba *Settings* para exigir que o Status Check do seu CI passe antes de permitir um *Merge*.
6. **Quebra de Build:** Altere a lógica da classe `Aluno` para que um teste falhe. Faça o `push` e observe o GitHub Actions em ação!

### Como obter o projeto na sua máquina e executar os testes
git clone https://github.com/joasweslei/lab_ci_cd.git

pip install pytest

python -m pytest