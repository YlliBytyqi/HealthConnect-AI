# 🏥 HealthConnect AI

Një platformë **Full-Stack** mjekësore për menaxhimin e klinikave dhe diagnostikimin prediktiv të sëmundjeve përmes Inteligjencës Artificiale.

> **Projekt akademik** — Laboratorike 2 (Programim) & Machine Learning Models (MM)  
> Universiteti për Biznes dhe Teknologji — UBT  
> Viti Akademik 2025-2026

---

## 👥 Ekipi

| Anëtari | Roli | Përgjegjësia |
|---------|------|--------------|
| **Erdona Kadriolli** | Data & ML Engineer | Dataset-et, Preprocessing, Modelet ML, API Docs |
| **Fatlum Syla** | Backend Developer | FastAPI, 24 Tabelat, JWT Auth, WebSockets |
| **Yll Bytyqi** | Frontend Developer | React + Vite, Dashboard, Real-Time Chat |

---

## 🧠 Çfarë bën ky sistem?

HealthConnect AI bashkon dy fusha:

1. **Menaxhim Klinike** — Mjekët, pacientët, takimet, recetat dhe historiku mjekësor menaxhohen dixhitalisht
2. **Diagnostikim me AI** — Modelet ML parashikojnë rrezikun e diabetit dhe sëmundjeve të zemrës bazuar në analizat laboratorike

---

## 🛠 Stack Teknologjik

| Shtresa | Teknologjia |
|---------|-------------|
| **Backend** | Python — FastAPI |
| **Frontend** | React + Vite |
| **Databaza SQL** | PostgreSQL |
| **Databaza NoSQL** | MongoDB / Redis |
| **ML** | scikit-learn, pandas, numpy |
| **Real-Time** | WebSockets |
| **Auth** | JWT (Access + Refresh Tokens) |

---

## 📁 Struktura e Projektit

```
HealthConnect-AI/
│
├── backend/                    # Fatlumi — FastAPI
│   ├── controllers/            # Route handlers
│   ├── services/               # Business logic
│   ├── repositories/           # Database queries
│   ├── models/                 # SQLAlchemy models
│   └── main.py                 # Entry point
│
├── frontend/                   # Ylli — React + Vite
│   ├── src/
│   │   ├── pages/              # Login, Dashboard, Patients, AI
│   │   ├── components/         # Komponente te riperdorshme
│   │   └── services/           # API calls
│   └── package.json
│
├── ml/                         # Erdona — Machine Learning
│   ├── 00_generate_datasets.py # Gjenerimi i dataseteve
│   ├── 01_inspect_datasets.py  # Inspektimi i dataseteve
│   ├── 02_preprocessing.py     # Pastrimi + skalimi + ndarja
│   ├── 03_train_models.py      # Trajnimi i 4 modeleve
│   ├── 04_kmeans_clustering.py # K-Means clustering
│   └── 05_predict.py           # Funksioni predict per backend
│
├── datasets/                   # Te dhenat
│   ├── diabetes.csv            # Pima Indians Diabetes (768 rreshta)
│   ├── heart.csv               # UCI Heart Disease (303 rreshta)
│   └── processed/              # Te dhenat e pastruara
│       ├── diabetes_train.csv
│       ├── diabetes_test.csv
│       ├── heart_train.csv
│       ├── heart_test.csv
│       └── scalers.pkl
│
├── models/                     # Modelet e trajnuara (.pkl)
│   ├── diabetes_random_forest.pkl
│   ├── diabetes_knn.pkl
│   ├── diabetes_logistic_regression.pkl
│   ├── diabetes_mlp_arkitektura_1.pkl
│   ├── diabetes_mlp_arkitektura_2.pkl
│   ├── heart_knn.pkl
│   ├── heart_random_forest.pkl
│   ├── heart_logistic_regression.pkl
│   ├── heart_mlp_arkitektura_1.pkl
│   ├── heart_mlp_arkitektura_2.pkl
│   ├── diabetes_kmeans.pkl
│   ├── results.csv
│   └── kmeans_results.csv
│
└── README.md
```

---

## ⚙️ Instalimi dhe Ekzekutimi

### Kërkesat paraprake

- Python 3.10+
- Node.js 18+
- PostgreSQL 14+
- Git

---

### 1. Klono Repository-n

```bash
git clone https://github.com/username/HealthConnect-AI.git
cd HealthConnect-AI
```

---

### 2. Backend (Fatlumi)

```bash
cd backend

# Krijo virtual environment
python -m venv venv

# Aktivo (Windows)
venv\Scripts\activate

# Aktivo (Mac/Linux)
source venv/bin/activate

# Instalo dependencies
pip install -r requirements.txt

# Konfiguro .env
cp .env.example .env
# Edito .env me kredencialet e databazës

# Ekzekuto migrimet
python manage.py migrate

# Starto serverin
uvicorn main:app --reload
```

Backend do të jetë aktiv në: `http://localhost:8000`  
Swagger UI: `http://localhost:8000/docs`

---

### 3. Frontend (Ylli)

```bash
cd frontend

# Instalo dependencies
npm install

# Starto serverin e zhvillimit
npm run dev
```

Frontend do të jetë aktiv në: `http://localhost:5173`

---

### 4. Machine Learning (Erdona)

```bash
cd ml

# Instalo dependencies
pip install pandas numpy scikit-learn

# Hapi 1: Inspekto dataset-et
python 01_inspect_datasets.py

# Hapi 2: Preprocessing
python 02_preprocessing.py

# Hapi 3: Trajno modelet (kNN, RF, LogReg, MLP x2)
python 03_train_models.py

# Hapi 4: K-Means Clustering
python 04_kmeans_clustering.py

# Hapi 5: Testo funksionin predict
python 05_predict.py
```

---

## 🤖 Modelet ML — Rezultatet

### Diabeti (Pima Indians Diabetes Database)

| Modeli | Accuracy | F1-Score |
|--------|----------|----------|
| **Random Forest** ⭐ | 85.71% | 0.7963 |
| kNN | 84.42% | 0.7692 |
| MLP Arkitektura 2 | 83.12% | 0.7679 |
| Logistic Regression | 75.32% | 0.6481 |
| MLP Arkitektura 1 | 74.68% | 0.5979 |

### Sëmundjet e Zemrës (UCI Heart Disease)

| Modeli | Accuracy | F1-Score |
|--------|----------|----------|
| **kNN** ⭐ | 85.25% | 0.8732 |
| Random Forest | 83.61% | 0.8649 |
| Logistic Regression | 81.97% | 0.8493 |
| MLP Arkitektura 2 | 81.97% | 0.8451 |
| MLP Arkitektura 1 | 62.30% | 0.5106 |

### K-Means Clustering (3 Grupe Rreziku)

| Grupi | Pacientë | % Diabetik |
|-------|----------|------------|
| Rrezik i Ulët | 322 (41.9%) | 8.1% |
| Rrezik Mesatar | 239 (31.1%) | 53.1% |
| Rrezik i Lartë | 207 (27.0%) | 55.6% |

---

## 🔌 API Endpoints (kryesorët)

### Autentifikimi
```
POST   /api/auth/register        # Regjistrim
POST   /api/auth/login           # Login — kthen JWT
POST   /api/auth/refresh         # Rifresko token-in
POST   /api/auth/logout          # Logout
```

### Pacientët
```
GET    /api/patients             # Lista e pacientëve
GET    /api/patients/{id}        # Detajet e pacientit
POST   /api/patients             # Shto pacient
PUT    /api/patients/{id}        # Edito pacient
DELETE /api/patients/{id}        # Fshi pacient
```

### Mjekët & Takimet
```
GET    /api/doctors              # Lista e mjekëve
GET    /api/appointments         # Takimet
POST   /api/appointments         # Rezervo takim
PUT    /api/appointments/{id}    # Ndrysho takim
```

### Machine Learning ⭐
```
POST   /api/predict/diabetes     # Parashiko diabetin
POST   /api/predict/heart        # Parashiko sëmundjen e zemrës
GET    /api/predict/history/{id} # Historiku i parashikimeve
```

### Raportet
```
GET    /api/reports/patient/{id}/pdf    # Eksporto PDF
GET    /api/reports/patient/{id}/excel  # Eksporto Excel
```

**Dokumentim i plotë:** `http://localhost:8000/docs` (Swagger UI)

---

## 🔒 Siguria

- **JWT Authentication** — Access Token (15 min) + Refresh Token (7 ditë)
- **RBAC** — Role-Based Access Control (Admin, Mjek, Pacient)
- **SQL Injection Protection** — ORM queries + input validation
- **Input Validation** — Pydantic models për të gjitha request-et
- **HTTPS** — i detyrueshëm në production

---

## 📡 Real-Time (WebSockets)

```
WS  /ws/notifications/{user_id}   # Njoftime live
WS  /ws/chat/{room_id}            # Chat mjek-pacient
```

---

## 📊 Databaza

**24 Tabela** të ndara në dy grupe:

**10 Tabelat e Detyrueshme (Auth & System):**
`Users, Roles, UserRoles, Permissions, RolePermissions, RefreshTokens, AuditLogs, Notifications, Settings, Files`

**14 Tabelat e Domenit (Mjekësor):**
`Patients, Doctors, Appointments, Specializations, MedicalRecords, LabTests, Prescriptions, Medications, Symptoms, SymptomReports, Clinics, Vaccinations, EmergencyContacts, InsurancePolicies`

ERD Diagram: shih dokumentacionin në `/docs/erd.png`

---

## 📋 Menaxhimi i Projektit

- **GitHub Projects** — To Do / In Progress / Done
- **Commits** — çdo anëtar bën commit individualisht
- **Branch strategy** — `main` (production), `dev` (zhvillim), `feature/*` (features)

---

## 📚 Datasetet

| Dataset | Burimi | Rreshta | Features |
|---------|--------|---------|----------|
| Pima Indians Diabetes | NIDDK, Smith et al. 1988 | 768 | 8 |
| UCI Heart Disease | Cleveland Clinic, Detrano et al. 1989 | 303 | 13 |

---

## 📄 Licenca

Projekt akademik — UBT 2025-2026. Të gjitha të drejtat e rezervuara.
