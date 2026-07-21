# 🐦 Twitter Sentiment Analysis Microservice

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

End-to-end микросервисное решение для анализа тональности твитов. Проект включает полную цепочку обработку данных (ETL из PostgreSQL), построение эмбеддингов с помощью Hugging Face Transformers, классификацию на базе XGBoost, а также REST API и веб-интерфейс, упакованные в мультиконтейнерную архитектуру **Docker Compose**.

---

## 🏗 Архитектура и Этапы Разработки

```text
[Kaggle Dataset] ──> [PostgreSQL DB] ──> [Pandas ETL] ──> [Hugging Face Embeddings]
                                                                  │
                                                                  ▼
[Streamlit UI] <──HTTP Requests──> [FastAPI Service] <─── [XGBoost Classifier]