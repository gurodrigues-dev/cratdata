# CratData

## 🇧🇷 PT-BR 

A system for sending data and also for voting, with high performance in scale and speed.

Compreendendo a vontade de possuir um sistema de votação que tivesse larga escala e que recebesse por volta de 50 milhões de requisições de uma vez e mesmo assim não caísse.

> Como fazer isso então?

- Bem, respondendo a esta pergunta, entramos em uma série de julgamentos sobre diversos softwares presentes no mercado. Mas, imagine que você cria uma votação entre `Golden State Warriors` e `Cavaliers`. E você admite que cerca de 50 milhões de requisições será feito em cerca de 48 horas. Então dividiriamos este mesmo valor por 24, posteriormente por 60, depois 60 novamente, então chegamos a um número de cerca de 3 mil requisições por segundo. Lembramos então que:

> Sempre que uma votação estiver aberta, é necessário que o sistema de APIs verifique se a votação está aberta, posteriormente votar e ainda ter que fazer a requisição para o banco de contagem. Três contagens de uma vez. ou seja as três mil requisições se tornariam nove mil. O que não é o ideal. 

Então partindo do inicío. Para não sobrecarregar a aplicação teríamos mais de uma máquina como API e na frente delas um Load Balancer, balanceando por peso de máquina. Essas máquinas seriam monitoradas por sistemas Prometheus e Grafana para garantirem sua integridade.

Seguindo com a requisição, com a intenção de não estressar tanto o banco, ao invès de fizermos três requisições, requisições que conseguem ser facilmente gravadas, como por exemplo a votação em aberta, pode ter um cache de memória alocado em um Redis Cloud. Ou seja consultando diretamente na API, verificando se a votação está aberta de fato, confirmado este parâmetro, pegaríamos o endpoint chamado pelo usuário, onde o resultado da sua votação estaria alocada, e já retornaríamos que o voto foi computado. - Sim, mesmo sem ele ter sido contado. 

Nos bastidores (uma espécie de por trás, dos panos) a requisição irá para uma fila de RabbitMQ que fará estas requisições gradativamente para o Postgre, onde lá existem diversas tabelas relacionais, que contam os dados. 

Em primeira instância, todos os códigos serão desenvolvidos localmente.

## 🇺🇸 EN-US 

A system for sending data and also for voting, with high performance in scale and speed.

Understanding the desire to have a voting system that had a large scale and that received around 50 million requests once it didn't go down.

> How to do it then?

- Well, answering this question, we enter into a series of judgments about various software present in the market. But, imagine that you create a poll between `Golden State Warriors` and `Cavaliers`. And you support that about 50 million requests will be done in about 48 hours. So we divide that same value by 24, later by 60, then 60 again, we get a number of about 3000 requests per second. We then remember that:
Whenever an acquisition is open, it is necessary that the APIs system is still confirmed, the voting bank and having to make a count request. Three counts at once. that is, the three thousand requests would become nine thousand. Which is not ideal.

> So starting from the beginning. for one more balancing machine, the application would have more machine as API and forward a balancing weight These machines are monitored by Prometheus systems and systems to secure in your network.

Following the request, with the intention of not stressing, both the bank that seeks to allocate the facilities and requests, such as the choice of open memory in a Redis Cloud, can have a memory cache. In other words, being directly in the API, checking if the vote is open, confirmed for this parameter, we will call the result of your calculation estimate, and we will already verify that the vote has been computed. - Yes, even without it being counted.

Behind the scenes (a kind of behind the scenes) the request will go to a RabbitMQ queue that will make these requests gradually to Postgre, where there are several relational tables, which count the data.

In the first instance, all code will be developed locally.

![votation2](https://user-images.githubusercontent.com/83222330/189469736-9202a4f9-1319-4849-aaf2-753f7ddabc7b.png)

