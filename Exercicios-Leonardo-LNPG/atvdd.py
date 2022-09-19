def main():
    path = input("Link: ")

    def quantidade_palavras(path):
        try:
            file = open(path, 'r', encoding='utf-8')
            objects = file.read()
            linhas = objects.split("\n")
            file.close()
            palavras = []
            for lista in linhas:
                palavras.extend(lista.split(" "))

            return palavras
        except:
            pass

    def cinco_maiores_palavras(path):
        palavras = quantidade_palavras(path)
        tamanhos = [(len(p), p) for p in palavras]
        maiores = []

        for t in range(5):
            t = max(tamanhos)
            if t == max(tamanhos):
                maiores.append(t[1])
                tamanhos.remove(t)
        return maiores

    def vogal_que_mais_aparece(path):
        try:
            file = open(path, 'r', encoding='utf-8')
            r = file.read()
            a = r.count("a")
            e = r.count("e")
            i = r.count("i")
            o = r.count("o")
            u = r.count("u")
            file.close()
            maior_v = ""
            maior = 0
            if a > maior:
                maior = a
                maior_v = "a"
            if e > maior:
                maior = e
                maior_v = "e"
            if i > maior:
                maior = i
                maior_v = "i"
            if o > maior:
                maior = o
                maior_v = "o"
            if u > maior:
                maior = u
                maior_v = "u"
            print("Vogal que mais aparece: ", maior_v,
                  " - {} vezes".format(maior))
        except:
            pass

    def literal_cao(path):
        file = open(path, "r", encoding="utf-8")
        r = file.read().split("\n")
        pos = []
        for linha in r:
            if "ção" in linha:
                pos.append(r.index(linha))
        if len(pos) != 0:
            print("Primeira aparição do literal 'ção' é na linha ", min(pos)+1)
        else:
            print("Não tem nenhum literal 'ção' no texto")

    print("Quantidade de palavras no arquivo: ",
          len(quantidade_palavras(path)))

    print("Cinco maiores palavras: ", cinco_maiores_palavras(path))

    vogal_que_mais_aparece(path)

    literal_cao(path)


if __name__ == "__main__":
    main()
