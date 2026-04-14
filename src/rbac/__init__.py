"""
Module rbac – Contrôle d'accès par rôles
==========================================
Responsable : Serigne Mame Sarr

Rôles disponibles :
  - admin   : gestion des utilisateurs, lecture/écriture tous secrets
  - user    : lecture/écriture de ses propres secrets
  - viewer  : lecture seule de secrets partagés

Ce module gère :
- L'attribution et la révocation des rôles
- La vérification des permissions avant chaque opération
- Le stockage chiffré des politiques d'accès
"""
