# Projeto Devops utilizando IaaS

Projeto que visa ajudar no fluxo de devops e ratreamento de atividades do dia a dia de desenvolvimento, adicionando os commits realizados
como comentários nas tasks do jira

## Pre-requisitos

- AWS cli
- Terraform cli
- Python v3.8
## Lista dos scripts disponiveis
 - api_gateway_proxy
 - codecommit_integration
## Deployment

Para realizar o deploy desta infraestrutura (IaaS do DEVOPS) basta executar o comando do Makefile passando
os parametros:

    - REGION;
    - API_STAGE; 
    - LAMBDA_UTILS_VERSION;
    - HTTP_UTILS_VERSION;
    - ATLASSIAN_URL;
    - USER_NAME;
    - API_TOKEN

**Exemplo do comando:**

    make REGION=us-east-1 API_STAGE=dsv LAMBDA_UTILS_VERSION=1 HTTP_UTILS_VERSION=1 ATLASSIAN_URL=https://neurotech.atlassian.net USER_NAME= usuário do jira API_TOKEN=token do jira

## Built With

* [Python](https://www.python.org/doc/) - The language used
* [Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) - The open-source infraestructure as code software tool

## Authors

* **Gabriel Lucas** - *Initial work* - [Gabriel](mailto:gabriel23costalima@outlook.com)
