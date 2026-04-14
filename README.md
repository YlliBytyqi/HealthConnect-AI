# HealthConnect AI 🏥

**HealthConnect AI** është një platformë "Full-Stack" mjekësore e krijuar për menaxhimin e klinikave dhe analizën prediktive të të dhënave shëndetësore. Ky projekt realizohet për lëndët **Laboratorike 2 (Programim)** dhe **Machine Learning Models** në UBT.

---

## 👥 Ekipi (Grupi)
* **Erdona Kadriolli**
* **Fatlum Syla**
* **Yll Bytyqi**

---

## 🚀 Përmbledhja e Projektit
Projekti integron zhvillimin softuerik me inteligjencën artificiale për të ofruar një sistem modern mjekësor.
* [cite_start]**Lab 2:** Zhvillimi i aplikacionit me arkitekturë të shtresëzuar, 24 tabela SQL, siguri JWT dhe komunikim në kohë reale[cite: 18, 25, 31, 51].
* **MM:** Zbatimi i algoritmeve të Machine Learning për parashikimin e sëmundjeve dhe grupimin e pacientëve.

---

## 🛠️ Teknologjitë (Kombinimi 5)
[cite_start]Sipas kërkesave teknike, projekti përdor këtë stack[cite: 14]:
* [cite_start]**Backend:** Python (FastAPI / Django)[cite: 14].
* [cite_start]**Frontend:** React + Vite[cite: 14].
* [cite_start]**Databaza SQL:** PostgreSQL (Minimum 24 tabela)[cite: 14, 18].
* [cite_start]**Databaza NoSQL:** MongoDB / Redis[cite: 14].
* [cite_start]**Real-Time:** WebSockets (Socket.IO)[cite: 53].

---

## 🗄️ Struktura e Databazës
[cite_start]Sistemi përmban 24 tabela në formën 3NF, ku 10 janë të detyrueshme[cite: 18, 21, 23]:
1. [cite_start]**Users** & **Roles** (Menaxhimi i llogarive)[cite: 21].
2. [cite_start]**AuditLogs** (Regjistrimi i veprimeve kritike)[cite: 21].
3. [cite_start]**Notifications** (Lajmërime live)[cite: 21].
4. **LabTests** (Të dhënat për Machine Learning).
5. [cite_start]**Appointments** (Menaxhimi i termineve)[cite: 22].
*(Dhe 14 tabela të tjera të domenit mjekësor).*

---

## 🧠 Moduli i Machine Learning (MM)
Në kuadër të lëndës MM, implementohen dhe krahasohen këto modele:
* **Klasifikimi:** 4 modele (k-NN, Random Forest, Logistic Regression, dhe MLP Neural Network).
* **Rrjetat Neurale:** Krahasimi i dy arkitekturave të ndryshme.
* **Clustering:** Grupimi i pacientëve me algoritmin K-Means.

---

## 📋 Si të ekzekutohet projekti

### 1. Klonimi
```bash
git clone https://github.com/erdonakadriolli/HealthConnect-AI.git
cd HealthConnect-AI
```

### 2. Backend (Python)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate për Windows
pip install -r requirements.txt
```

### 3. Frontend (React)
```bash
cd ../frontend
npm install
npm run dev
```

---

## 🛠️ Menaxhimi i Projektit
* [cite_start]**Git:** Commits individuale nga Erdona, Fatlumi dhe Ylli[cite: 38].
* [cite_start]**Bashkëpunimi:** Tasks të ndara në Jira/GitHub Projects (To Do, In Progress, Done)[cite: 42, 43].
* **Repository:** [HealthConnect-AI GitHub](https://github.com/erdonakadriolli/HealthConnect-AI.git)

---
