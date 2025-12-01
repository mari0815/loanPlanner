# 💰 Darlehenstilgungsrechner

Eine vollständig selbstgehostete Web-App zur Berechnung und Verwaltung von Darlehens-Tilgungsplänen mit Sondertilgungen.

## Features

- ✅ Eingabe von Darlehenssumme, Zinssatz und monatlicher Rate
- ✅ **Startmonat der Tilgung** frei wählbar
- ✅ **Monatsrate je Monat anpassbar** (nicht nur Standardrate)
- ✅ **Sondertilgungen** pro Monat eingeben
- ✅ **Geräteübergreifend synchron** (Änderungen bleiben erhalten)
- ✅ Responsive Design (Desktop/Tablet/Mobile)
- ✅ Automatische Neuberechnung nach jeder Änderung
- ✅ Übersicht: Gesamtzinsen, Laufzeit, Gesamtkosten

## 🐳 Docker Compose Setup

```bash
# 1. Repository klonen
git clone https://github.com/mari0815/loan-calculator.git
cd loan-calculator

# 2. Persistente Daten-Ordner anlegen
mkdir -p plan-data

# 3. Container starten
docker compose up -d --build

# 4. Logs prüfen (sollte "Flask startet..." zeigen)
docker compose logs -f
```

**App läuft dann unter:** `http://localhost:8000`

## 🔧 Nginx Proxy Manager (optional)

- **Proxy Host:** `loan.deinedomain.de` → `http://<docker-ip>:8000`
- **SSL:** Let's Encrypt aktivieren
- **Force SSL:** ✅

## 📱 Verwendung

1. **Parameter eingeben:** Darlehenssumme, Zinssatz, Rate, Startmonat
2. **"Tilgungsplan berechnen"** klicken
3. **Rate/Sondertilgung ändern:** Direkt in der Tabelle eingeben
4. **Automatische Neuberechnung** für alle folgenden Monate
5. **Daten bleiben erhalten** (geräteübergreifend synchron)

## 🗄️ Datenpersistenz

- **Datei:** `./plan-data/plan.json`
- **Backup:** Einfach die Datei kopieren
- **Sicherung:** `.gitignore` schließt `plan-data/` aus

## 🔄 Updates

```bash
docker compose pull
docker compose up -d --build
```

## 📚 Struktur

```
├── app.py              # Flask Backend + API
├── Dockerfile          # Docker Image
├── docker-compose.yml  # Container Orchestrierung
├── static/
│   └── index.html      # Frontend (HTML+JS+CSS)
├── plan-data/          # Persistente Daten (NICHT im Git)
└── README.md           # Diese Datei
```

## ⚠️ Wichtige Hinweise

- **Persönliche Daten** bleiben nur lokal in `plan-data/plan.json`
- **Backup:** Kopiere regelmäßig `plan-data/` 
- **Port:** Standardmäßig `8000` (in `docker-compose.yml` änderbar)

## 🚀 Beispiel

Mit €20.000 Darlehen, 3% Zinsen, €350/Monat:
- **Gesamtzinsen:** ca. €1.543
- **Laufzeit:** ca. 61 Monate
- **Gesamtkosten:** ca. €21.543

---

**Von und für:** Selbsthosting-Enthusiasten 🐧✨
