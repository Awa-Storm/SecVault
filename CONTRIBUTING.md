# Guide de contribution – SecVault

## 🌿 Convention de branches

| Branche | Usage |
|---------|-------|
| `main` | Code stable – **merge via Pull Request uniquement** |
| `feature/auth` | Module authentification (Awa) |
| `feature/crypto` | Module chiffrement (Salimata) |
| `feature/rbac` | Module RBAC & CLI (Serigne) |
| `feature/audit` | Module journal d'audit (Awa) |
| `feature/cli` | Interface CLI (Serigne) |

## ✅ Règles de commit

Format : `type(scope): description courte`

Types autorisés :
- `feat` – nouvelle fonctionnalité
- `fix` – correction de bug
- `test` – ajout/modification de tests
- `docs` – documentation uniquement
- `refactor` – refactoring sans nouvelle fonctionnalité
- `security` – correctif de sécurité

**Exemples :**
```
feat(crypto): implémenter le chiffrement AES-256-GCM des secrets
fix(auth): corriger la vérification du code TOTP
test(audit): ajouter les tests de vérification HMAC
security(rbac): corriger l'élévation de privilège sur secret list
```

## 🔀 Processus de Pull Request

1. Créer une branche depuis `main` : `git checkout -b feature/mon-module`
2. Développer et tester localement : `pytest tests/ -v`
3. Vérifier la sécurité : `bandit -r src/`
4. Ouvrir une Pull Request vers `main`
5. **Revue de code obligatoire** par au moins un autre membre
6. Merge uniquement si la CI est verte ✅

## 🔒 Règles de sécurité absolues

- **Ne jamais commit** de clé, secret, mot de passe ou fichier `.db`
- **Ne jamais commit** directement sur `main`
- Toujours vérifier le `.gitignore` avant `git add .`
