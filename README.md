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

	[hgamal@ygamal hm_calc_trans]$ ./calc_trafo 
	Potência (watts) ? 10
	Impedancia do primario (ohms) ? 8000
	Impedancia do secundario (ohms) ? 8
	Frequencia (Hz) ? 80
	Transformador PP ou SE ? pp
	Corrente de repouso (A) ? 0.06
	Secçao minima do nucleo: 3.57 cm2, perna central de  1.90 cm
	0 : model="sarlo:SP 08", type="STSR", leg=16.5 mm, stack=22.7 mm, thickness=2.0 mm
	1 : model="sarlo:SP 09", type="STSR", leg=16.0 mm, stack=27.3 mm, thickness=2.0 mm
	2 : model="sarlo:SP 10", type="STSR", leg=16.7 mm, stack=30.8 mm, thickness=2.0 mm
	3 : model="sarlo:SP 14", type="STSR", leg=20.0 mm, stack=20.0 mm, thickness=2.0 mm
	4 : model="sarlo:SP 15", type="STSR", leg=20.0 mm, stack=22.5 mm, thickness=2.0 mm
	5 : model="sarlo:SP 18", type="STSR", leg=23.0 mm, stack=23.0 mm, thickness=2.0 mm
	6 : model="sarlo:SP 47", type="STSR", leg=26.0 mm, stack=19.2 mm, thickness=2.0 mm
	7 : model="sarlo:SP 48", type="STSR", leg=26.0 mm, stack=20.5 mm, thickness=2.0 mm
	8 : model="sarlo:SP 35", type="PT", leg=16.8 mm, stack=23.0 mm, thickness=2.0 mm
	9 : model="sarlo:SP 38", type="PT", leg=20.0 mm, stack=22.0 mm, thickness=2.0 mm
	10 : model="sarlo:SP 44", type="PTCD", leg=16.8 mm, stack=22.9 mm, thickness=2.0 mm
	11 : model="sarlo:SP 45", type="PTCD", leg=20.2 mm, stack=22.2 mm, thickness=2.0 mm
	12 : model="lider:17x23", type="PT", leg=17.0 mm, stack=23.0 mm, thickness=2.0 mm
	13 : model="lider:20x20", type="STSR", leg=20.0 mm, stack=20.0 mm, thickness=2.0 mm
	14 : model="lider:20x22", type="PT", leg=20.0 mm, stack=22.0 mm, thickness=2.0 mm
	15 : model="lider:26x20", type="STSR", leg=26.0 mm, stack=20.0 mm, thickness=2.0 mm
	selecione o carretel a ser usado, da lista acima: 13
	Usando o carretel lider:20x20, Empilhamento = 2.0 (cm)
	0 : lider:2HS-190: leg=19.0 mm
	1 : lider:4HS-190: leg=19.0 mm
	2 : lider:4HS-200: leg=20.0 mm
	selecione o laminado a ser usado, da lista acima: 2
	Usando o laminado lider:4HS-200, Perna central = 2.00 (cm)
	Window Area = (40.00 -  10.00) * 10.00 = 300.00
	Copper Area = 104.82


	*** Resultados ***
	Secção usada 2.00 cm x 2.0 cm = 4.00 cm2
	Lamina:             lider:4HS-200
	Carretel:           lider:20x20
	Tensao primario:    282.8 V @ 0.069 A
	Tensao secundário:  8.9 V @ 1.118 A
	Espiras primario:   2737 fio AWG 33
	Espiras secundario: 86 fio AWG 21
	Construção impossível razão de áreas: 2.86
	11 camadas de 248.8 espiras fio AWG 33
	2 camadas de 43.0 espiras fio AWG 21

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