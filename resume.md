# Exercice récapitulatif : Heroes Vs Monsters

Bienvenue dans la forêt de « Shorewood », forêt enchantée du pays de « Stormwall ».

Dans cette forêt, se livre un combat acharné entre les héros d'une part et les monstres d'autre part. Notre rôle est de donner vie à cette forêt au travers d'un programme écrit en console reprenant tous les concepts orientés objets vu au cours.

## Description du monde

Nous retrouvons deux familles de personnages :
- Les héros : Humain ou nain
- Les monstres : Loup, Orque ou dragonnet

### Caractéristiques des personnages

Chaque personnage possède différentes caractéristiques :
- Endurance (End)
- Force (For)
- Points de vie (PV)

#### Calcul des caractéristiques
- La force et l'endurance sont calculées à la création du personnage en lançant, pour chacune d'elles, quatre dé 6 faces et en n'en reprenant que les 3 meilleurs.
- Les points de vie sont déterminés par l'endurance additionnée avec le modificateur basé sur l'endurance.

### Action : Frappe

Lorsqu'un personnage frappe sur un autre, les dégâts sont déterminés par le jet d'un dé à 4 faces auquel on ajoute un modificateur basé sur la caractéristique de Force. Une fois calculé, les dégâts sont retirés des points de vies de la cible.

### Héros

Les héros en tuant les monstres vont les dépouiller de leur richesse (Or et/ou Cuir), qu'ils vont stocker sans limite. Après chaque combat les héros se reposent et restaurent leurs points de vie et affronte le monstre suivant jusqu'à leur mort.

Types de héros :
- Humains : +1 aux caractéristiques de Force et d'Endurance
- Nains : +2 en Endurance

### Monstres

Types de monstres :
1. Loups :
   - Peuvent être dépecés (donne du cuir)
2. Orques :
   - +1 en force
   - Ont de l'or
3. Dragonnets :
   - +1 en endurance
   - Ont de l'or
   - Peuvent être dépecés (donne du cuir)

## Règles supplémentaires

1. Le modificateur se base sur le score de la caractéristique pour ajouter un bonus ou un malus :
   - Si la caractéristique est inférieure à 5 : -1
   - Si elle est inférieure à 10 : 0
   - Si elle est inférieure à 15 : +1
   - Sinon : +2

2. L'or et le cuir sont calculés à la création du monstre :
   - Or : calculé sur base d'un dé 6 faces
   - Cuir : calculé sur base d'un dé 4 faces

3. Tout personnage meurt lorsque ses points de vies sont <= à 0.

4. La classe « Random » devrait vous aider.

## Contraintes

- La force et l'endurance sont des propriétés en lecture seule.
- La propriété PV est :
  - (Si les délégués ont été vu) « private » aussi bien en lecture et en écriture.
  - (sinon) en lecture seule.
- Les bonus d'endurance et de force offerts par les classes (Humain, Nain, Orque et Dragonnet) ne doivent pas modifier la caractéristique de base du personnage.
- La classe dé contient deux propriétés en lecture seule Minimum et Maximum ainsi qu'une méthode Lance qui retourne un entier aléatoire.

## Exercice supplémentaire

Prévoir une zone de jeu de 15 sur 15, contenant une 10aine de monstres espacés d'au moins de 2 cases (horizontale et verticale) les uns des autres.

### Modifications pour l'exercice supplémentaire

- Ajouter aux personnages deux propriétés X et Y qui vont déterminer la position de chaque personnage sur le plateau. Leur position est connue à la création.
- Les monstres sont cachés et n'apparaissent qu'une fois le combat commencé.
- Le combat commencera automatiquement lorsque le héros se positionnera à côté, horizontalement ou verticalement, d'un monstre.
- Affichage :
  - Héro : H
  - Loup : L
  - Orque : O
  - Dragonnet : D

Le jeu s'arrête lorsqu'il n'y a plus de monstres sur la carte ou que le héros meurt.