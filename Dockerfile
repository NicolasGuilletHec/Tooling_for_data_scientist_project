FROM python:3.11-slim
ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# Install runtime deps
COPY requirements.txt .
RUN python -m pip install -U pip && \
    pip install --only-binary=:all: -r requirements.txt

# ⬇️ Copy ALL files the app imports/uses at runtime
COPY app.py data_utils.py sample_data.csv ./
# (keep tests only if you want them inside the image)
# COPY tests ./tests

EXPOSE 8501
CMD ["streamlit","run","app.py","--server.port=8501","--server.address=0.0.0.0"]

