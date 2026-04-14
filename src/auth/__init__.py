"""
Module auth – Authentification SecVault
=======================================
Responsable : Awa Niasse

Ce module gère :
- L'enregistrement des utilisateurs (hachage Argon2id du mot de passe maître)
- La connexion avec vérification MDP + TOTP (2FA)
- La gestion des sessions (token de session en mémoire uniquement)
"""
