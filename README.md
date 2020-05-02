# Programa Handmades para cálculo de transformadores de Áudio

http://www.handmades.com.br/forum/index.php?topic=11647


## Obtendo o código

	hgamal@ygamal ~]$ git clone https://github.com/hgamal/hm_calc_trans
	Cloning into 'hm_calc_trans'...
	remote: Enumerating objects: 24, done.
	remote: Counting objects: 100% (24/24), done.
	remote: Compressing objects: 100% (19/19), done.
	remote: Total 24 (delta 5), reused 18 (delta 2), pack-reused 0
	Unpacking objects: 100% (24/24), done.

## Excutando

	[hgamal@ygamal ~]$ cd hm_calc_trans
	[hgamal@ygamal hm_calc_trans]$ ./calc_trafo 
	Potência (watts) ? 5
	Impedancia do primario (ohms) ? 5000
	Impedancia do secundario (ohms) ? 8
	Frequencia (Hz) ? 40
	Transformador PP ou SE ? se
	Secçao minima do nucleo: 3.57cm2, perna central de 1.9 cm
	0 : lider:2HS-190: leg=19.0 mm
	1 : lider:4HS-190: leg=19.0 mm
	2 : lider:4HS-200: leg=20.0 mm
	selecione o laminado a ser usado, da lista acima: 1
	Usando o laminado lider:4HS-190: leg=19.0 mm, Perna central = 1.9 (cm)
	0 : model="sarlo:SP 14", type="STSR", leg=20.0 mm, stack=20.0 mm, thickness=2.0 mm
	1 : model="sarlo:SP 15", type="STSR", leg=20.0 mm, stack=22.5 mm, thickness=2.0 mm
	2 : model="sarlo:SP 16", type="STSR", leg=20.2 mm, stack=30.7 mm, thickness=2.0 mm
	3 : model="sarlo:SP 38", type="PT", leg=20.0 mm, stack=22.0 mm, thickness=2.0 mm
	4 : model="sarlo:SP 39", type="PT", leg=20.0 mm, stack=30.8 mm, thickness=2.0 mm
	5 : model="sarlo:SP 45", type="PTCD", leg=20.2 mm, stack=22.2 mm, thickness=2.0 mm
	6 : model="santarita:#16", type="SR", leg=19.9 mm, stack=19.8 mm, thickness=2.0 mm
	7 : model="santarita:#17", type="CR", leg=20.0 mm, stack=22.7 mm, thickness=2.0 mm
	8 : model="santarita:#18", type="PT", leg=20.0 mm, stack=22.3 mm, thickness=2.0 mm
	9 : model="santarita:#19", type="CR", leg=20.1 mm, stack=22.3 mm, thickness=2.0 mm
	10 : model="santarita:#20", type="CRCD", leg=20.1 mm, stack=22.3 mm, thickness=2.0 mm
	selecione o carretel a ser usado, da lista acima: 0
	Usando o carretel model="sarlo:SP 14", type="STSR", leg=20.0 mm, stack=20.0 mm, thickness=2.0 mm, Empilhamento = 2.0 (cm)
	*** Resultados ***
	Secção usada 1.9cm x 2.0 cm = 3.8cm2
	Lamina: lider:4HS-190: leg=19.0 mm
	Carretel: model="sarlo:SP 14", type="STSR", leg=20.0 mm, stack=20.0 mm, thickness=2.0 mm
	Tensao primario:158.1V @ 0.055A
	Tensao secundário:6.3V @ 0.791A
	Espiras primario:5154 fio AWG 34
	Espiras secundario:206 fio AWG 22
	Gap: 0.29 mm na perna central e laterais

## Tabelas

- cores.ods - tabela em Libre Office com algumas lâminas obtíveis no brasil
- cores.csv - esta é a mesma tabela acima mas de forma legível pelo programa. Se alterar a tabela acima, esta deve ser regerada
- reels.ods - tabela em Libre Office com algums carretéis obtíveis no brasil
- reels.csv - esta é a mesma tabela acima mas de forma legível pelo programa. Se alterar a tabela acima, esta deve ser regerada

## Código

- Cores.py - Objeto de manutenção e manipulação de lâminas
- CoilForm.py - Objeto de manutenção e manipulação de carretéis
- calc_trafo - programa principal

## Imagens

- core_dimensions.png - imagem descrevendo os campos de cores.ods