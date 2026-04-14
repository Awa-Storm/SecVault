"""
Module audit – Journal d'audit signé
======================================
Responsable : Awa Niasse

Ce module gère :
- L'enregistrement horodaté de chaque action (création, lecture, suppression de secret)
- La signature HMAC-SHA256 de chaque entrée du journal (non-répudiation)
- La vérification de l'intégrité du journal
- L'export du journal pour consultation par l'administrateur
"""
