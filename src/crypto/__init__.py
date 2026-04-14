"""
Module crypto – Chiffrement SecVault
=====================================
Responsable : Salimata Sène Diop

Ce module gère :
- La dérivation de clé depuis le mot de passe maître (Argon2id)
- Le chiffrement / déchiffrement AES-256-GCM des secrets
- La génération de nonces aléatoires sécurisés
- La vérification d'intégrité (MAC)
"""
