


def tous_presents(s1: str, s2: str) -> bool :
	""" 
	pre-cond:
	post-cond: retourne True ssi chaque caractère de s1 apparait au moins une fois dans s2
	"""
	i = 0
	while i < len(s1):
		#on cherche si s1[i] est présent dans s2
		est_present = False
		j = 0
		while j < len(s2) and not est_present:
			if s1[i] == s2[j]:
				est_present = True
			j += 1
		if not est_present:
			#le caractère s[i] n'est pas présent dans s2
			return False
		#sinon on continue : on va chercher le caractère s1[i+1]
		i += 1
	#si on n'a jamais retourné False, c'est que c'est bon
	return True
	
print(tous_presents("abc", "arbre"))
print(tous_presents("abc", "abracadabra"))
print(tous_presents("toto", "ta"))
print(tous_presents("tot", "tot"))
print("-----------------------------")

def caracteres_1_fois(chaine: str) -> bool:
	"""
	pre-cond:
	post-cond: retourne True ssi chaque caractère de chaine n'apparait qu'une seule fois
	"""
	i = 0
	while i < len(chaine):
		#on cherche si chaine[i] est présent une nouvelle fois à sa droite
		j = i+1
		while j < len(chaine):
			if chaine[i] == chaine[j]:
				#le caractère chaine[i] apparait au moins 2 fois
				return False
			j += 1
		i += 1
	#si on n'a jamais retourné False, c'est que c'est bon
	return True
	
	
print(caracteres_1_fois("confiné"))
print(caracteres_1_fois("python"))
print(caracteres_1_fois("divulgacherons"))
print("-----------------------------")
	
	
	
def alternance(s1: str, s2: str, n: int) -> str :
	"""
	pre-cond:
	post-cond: retourne une chaine composée de n alternances de s1 et s2
	"""
	res = ""
	i = 0
	while i < n:
		if i % 2 == 0:
			res += s1
		else:
			res += s2
		i += 1
	return res
	
print(alternance("to", "ta", 3))
print(alternance("ba", "bi", 5))
print(alternance("ba", "bi", 0))
print("-----------------------------")


def sous_chaine(ch: str, i: int, j : int) -> str:
	"""
	pre-cond:
	post-cond : retourne ch[i:j]
	"""
	if i > j or i < 0 or j >= len(ch):
		return ""
	#on commence par ajouter ch[i]
	res = ch[i]
	#puis on ajoute les autres
	x = i+1
	while x < j:
		res += ch[x]
		x += 1
	return res
	
print(sous_chaine("tarte aux pommes", 3, 8))
print(sous_chaine("tarte aux pommes", 8, 8))
print(sous_chaine("tarte aux pommes", 10, 3))
print("-----------------------------")


def bien_parenthesee(ch: str) -> bool:
	"""
	pre-cond : ch est une chaine parenthésée
	post-cond: retourn True ssi ch est bien parenthésée
	"""
	nb_ouvrantes = 0
	nb_fermantes = 0
	i = 0
	while i < len(ch):
		if ch[i] == "(":
			nb_ouvrantes += 1
		else:
			nb_fermantes += 1
		#on retourne faux si à un moment donné, le nombre de parenthèses ouvrantes est strictement inférieur au nombre de parenthèses fermantes
		if nb_ouvrantes < nb_fermantes:
			return False
		i += 1
	#à la fin, on retourne vrai ssi le nombre de parenthèses ouvrantes est égal au nombre de parenthèses fermantes
	return nb_ouvrantes == nb_fermantes
	
print(bien_parenthesee("(()())"))
print(bien_parenthesee("()()()"))
print(bien_parenthesee("()())"))
print(bien_parenthesee("(()()))(()"))
print("-----------------------------")

	
def nieme_mot(chaine: str, n: int) -> str :
	"""
	pre-cond:
	post-cond: retourne le nième mot de la chaine
	"""
	nb_mots = 0
	i = 0
	#tant qu'on n'a pas atteint le nombre de mots voulus, on parcourt notre chaîne en comptant les mots
	while nb_mots < n and i < len(chaine)-1:
		if chaine[i] == " " and chaine[i+1] != " ":
			nb_mots += 1
		i += 1
	#à la fin, si on est bien sortis de la boucle car on a atteint le nombre de mots voulus (première condition du while), alors on recopie notre mot
	res = ""
	if nb_mots == n:
		while i < len(chaine) and chaine[i] != " ":
			res += chaine[i]
			i += 1
	return res
	
print(nieme_mot("nous sommes tous confinés", 0))
print(nieme_mot("nous sommes tous confinés", 2))
print(nieme_mot("nous sommes tous confinés", 3))
print(nieme_mot("nous sommes tous confinés", 16))

	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
