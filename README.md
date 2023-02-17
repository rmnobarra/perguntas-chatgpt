Script em python que gera pergunta baseado no assunto (variavel "Topic) utilizando como nível de complexidade da pergunta a taxinomia de bloom (primeiro nível como padrão) e um link externo também como referência:

Create a multiple choice question about {topic} at the first level of Bloom's Taxonomy of learning using this link for reference https://pt.wikipedia.org/wiki/Docker_(software)

Como utilizar?

1. Adicione a api key do open api em um arquivo .env (.env.sample como exemplo
   
2. Instalando pre reqs:

pip3 install -r requirements.txt

3. Executando:

python3 pergunta.py

4. O output esperado é algo similar:

```bash
➜ python3 pergunta.py

1. O que é o Docker?
a. Uma ferramenta de código aberto que automatiza o processo de implantação de aplicativos em contêineres
b. Uma ferramenta de código aberto que automatiza o processo de compilação de aplicativos
c. Uma ferramenta de código aberto que automatiza o processo de implantação de aplicativos em máquinas virtuais
d. Uma ferramenta de código aberto que automatiza o processo de gerenciamento de contêineres

2. Quais são as vantagens do uso do Docker?
a. Menor utilização de recursos
b. Menor tempo de implantação
c. Isolamento de aplicativos
d. Todas as alternativas são verdadeiras

3. Como o Docker funciona?
a. O Docker cria um ambiente isolado para cada aplicativo, permitindo que eles sejam executados de forma independente e sem interferência uns com os outros
b. O Docker cria um ambiente compartilhado para todos os aplicativos, permitindo que eles sejam executados de forma colaborativa
c. O Docker cria um ambiente virtualizado para todos os aplicativos, permitindo que eles sejam executados de forma independente e sem interferência uns com os outros
d. O Docker cria um ambiente físico para todos os aplicativos, permitindo que eles sejam executados de forma independente e sem interferência uns com os outros

4. Qual é a diferença entre um container e uma máquina virtual?
a. Uma máquina virtual é um ambiente completamente isolado, em que cada aplicativo tem seu próprio sistema operacional e seus próprios recursos de hardware, enquanto um container compartilha o mesmo sistema operacional e os mesmos recursos de hardware com outros aplicativos
b. Uma máquina virtual é um ambiente completamente isolado, em que cada aplicativo tem seu próprio sistema operacional, enquanto um container compartilha o mesmo sistema operacional com outros aplicativos
c. Uma máquina virtual é um ambiente virtualizado, em que cada aplicativo tem seu próprio sistema operacional, enquanto um container compartilha o mesmo sistema operacional com outros aplicativos
d. Uma máquina virtual é um ambiente físico, em que cada aplicativo tem seu próprio sistema operacional, enquanto um container compartilha o mesmo sistema operacional com outros aplicativos

5. Por que o Docker é considerado uma ferramenta de virtualização de aplicativos?
a. Porque o Docker cria um ambiente isolado para cada aplicativo, permitindo que eles sejam executados de forma independente e sem interferência uns com os outros
b. Porque o Docker cria um ambiente compartilhado para todos os aplicativos, permitindo que eles sejam executados de forma colaborativa
c. Porque o Docker cria um ambiente virtualizado para todos os aplicativos, permitindo que eles sejam executados de forma independente e sem interferência uns com os outros
d. Porque o Docker cria um ambiente físico para todos os aplicativos, permitindo que eles sejam executados de forma independente e sem interferência uns com os outros
```

