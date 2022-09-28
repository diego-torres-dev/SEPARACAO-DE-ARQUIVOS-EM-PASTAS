# Separação de Arquivos em Pastas

A pasta `Arquivos_Lojas` possuia arquivos de extensão `.csv` com os dados de vendas trimestrais para os anos de 2018 a 2020 de lojas nos estados do Amazonas, Goiás, Minas Gerais, Rio de Janeiro e São Paulo.

A referida pasta era um contêiner para os arquivos, sem nenhuma subpasta.

A fim de organizar melhor estes arquivos, este programa criou uma estrutura de pastas com subpastas para poder armazenar os arquivos de forma mais organizada.

Eis a estrutura final desejada (as demais subpastas e arquivos não foram exibidas na estrutura abaixo):

```txt
Estados/
├─ AM/
│  ├─ 2018/
│  │  ├─ 01/
│  │  ├─ 02/
│  │  |  ├─ 201802_Amazonas Shopping_AM.csv
│  │  ├─ 03/
│  │  ├─ 04/
│  ├─ 2019/
│  ├─ 2020/
├─ GO/
├─ RJ/
├─ SP/
```

Dado que os nomes dos arquivos têm um padrão, foi possível usar essa informação a fim de destinar cada arquivo para a pasta em que ele deveria ser armazenado.
