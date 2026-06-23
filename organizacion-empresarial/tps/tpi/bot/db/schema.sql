CREATE TABLE employees (
    id              SERIAL PRIMARY KEY,
    legajo          VARCHAR(20) UNIQUE NOT NULL,
    full_name       VARCHAR(100) NOT NULL,
    department      VARCHAR(50) NOT NULL,
    vacation_balance INTEGER NOT NULL CHECK (vacation_balance >= 0)
);

CREATE TABLE vacation_requests (
    id              SERIAL PRIMARY KEY,
    employee_id     INTEGER NOT NULL REFERENCES employees(id),
    start_date      DATE NOT NULL,
    end_date        DATE NOT NULL,
    days_requested  INTEGER NOT NULL CHECK (days_requested > 0),
    reason          TEXT,
    status          VARCHAR(20) NOT NULL
        CHECK (status IN ('PENDING', 'APPROVED', 'REJECTED', 'CANCELLED')),
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date >= start_date)
);

CREATE TABLE conversation_sessions (
    session_id      UUID PRIMARY KEY,
    employee_id     INTEGER REFERENCES employees(id),
    current_state   VARCHAR(50) NOT NULL,
    context         JSONB NOT NULL DEFAULT '{}',
    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_vacation_requests_employee ON vacation_requests(employee_id);
CREATE INDEX idx_conversation_sessions_employee ON conversation_sessions(employee_id);
