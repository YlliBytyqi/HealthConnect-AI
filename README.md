# HealthConnect AI 🏥

**HealthConnect AI** është një platformë "Full-Stack" mjekësore e krijuar për menaxhimin e klinikave dhe analizën prediktive të të dhënave shëndetësore. Ky projekt realizohet për lëndët **Laboratorike 2** dhe **Machine Learning Models** në UBT.

---

## 👥 Ekipi (Grupi)
* **Erdona Kadriolli**
* **Fatlum Syla**
* **Yll Bytyqi**

---

## 🚀 Përmbledhja e Projektit
Projekti integron zhvillimin softuerik me inteligjencën artificiale për të ofruar një sistem modern mjekësor.
* **Lab 2:** Zhvillimi i aplikacionit me arkitekturë të shtresëzuar, 24 tabela SQL, siguri JWT dhe komunikim në kohë reale.
* **MM:** Zbatimi i algoritmeve të Machine Learning për parashikimin e sëmundjeve dhe grupimin e pacientëve.

---

## 🛠️ Teknologjitë (Kombinimi 5)
Sipas kërkesave teknike, projekti përdor këtë stack:
* **Backend:** Python (FastAPI / Django).
* **Frontend:** React + Vite.
* **Databaza SQL:** PostgreSQL (Minimum 24 tabela).
* **Databaza NoSQL:** MongoDB / Redis.
* **Real-Time:** WebSockets (Socket.IO).

---

## 🗄️ Struktura e Databazës
Sistemi përmban 24 tabela në formën 3NF, ku 10 janë të detyrueshme:
1. **Users** & **Roles** (Menaxhimi i llogarive).
2. **AuditLogs** (Regjistrimi i veprimeve kritike).
3. **Notifications** (Lajmërime live)
4. **LabTests** (Të dhënat për Machine Learning).
5. **Appointments** (Menaxhimi i termineve).
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
* **Git:** Commits individuale nga Erdona, Fatlumi dhe Ylli
* **Bashkëpunimi:** Tasks të ndara në Jira/GitHub Projects (To Do, In Progress, Done)
* **Repository:** [HealthConnect-AI GitHub](https://github.com/erdonakadriolli/HealthConnect-AI.git)

---
