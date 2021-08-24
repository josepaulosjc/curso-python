lista_notas = [62, 57, 83, 91, 74, 63]

notas = list(map(int, lista_notas))
novas = [(lambda ng: ((int(ng/5)+1)*5) if ng > 60 and ((int(ng/5)+1)*5)
          - ng < 3 else ng)(ng) for ng in notas]
print(novas)
