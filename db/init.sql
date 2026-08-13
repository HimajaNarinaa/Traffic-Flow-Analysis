-- PostgreSQL schema for processing logs
CREATE TABLE IF NOT EXISTS processing_logs (
    id SERIAL PRIMARY KEY,
    video_key TEXT NOT NULL,
    bucket TEXT NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT now(),
    finished_at TIMESTAMP,
    status TEXT,
    metrics_path TEXT,
    details JSONB
);
