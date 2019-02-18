# Botty

**Un petit bot pour Travian**

Ce bot à été créé pour une utilisation en lien avec Travian

---

[![GitHubrealease](https://img.shields.io/github/release/Easyghost195/botty.svg?colorB=blue&style=flat)](https://github.com/Easyghost195/botty)
[![Discord](https://discordapp.com/api/guilds/129489631539494912/widget.png?style=shield)](https://discordapp.com/api/oauth2/authorize?client_id=373909446755090434&permissions=8&scope=bot)

---
## Préparation

Copier le fichier example_options.py en option.py et modifier les variables pour son propre serveur (Token, Owner_Id, Channels ...)

## Commandes
```
!serverinfo
```
Donne quelques informations sur le serveur où se situe le bot
```
!sign
```
Permet de s'inscrire sur le serveur grâce à la commande !sign < pseudo >  
La commande vérifie si le pseudo existe vraiment et renomme l'utilisateur si c'est le cas  
De plus, la commande check l'alliance du joueur et l'associe au rôle de son alliance pour avoir accès aux salons de son alliance.
```
!mm
```
Pour envoyer un message alliance. Une demande de def se fera par !mm def x y heure quantité_troupe nourrir(yes ou no).
Pour une demande de push !mm push x y heure quantité
Pour une demande de nourrir les troupes !mm crops x y
Le message ira dans un salon spécial message IG et un autre avec la même demande mais pour discord
```
!info
```
Permet d'afficher L’URL relative aux informations sur un joueur et son alliance  avec !info < joueur >
