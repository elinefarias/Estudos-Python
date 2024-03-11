
class Restaurante:
  nome = ''
  categoria = ''
  ativo = False
  
restaurante_sertao_veredas = Restaurante()
restaurante_sertao_veredas.nome = 'Sertao Veredas'
restaurante_sertao_veredas.categoria = 'Brasileira'
restaurante_sertao_veredas.ativo = True
 
 
print(dir(restaurante_sertao_veredas.nome)) 
print(vars(restaurante_sertao_veredas))


class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
