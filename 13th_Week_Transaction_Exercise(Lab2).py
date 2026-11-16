import sqlite3

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL NOT NULL CHECK(balance >= 0)
)
""")

cursor.execute("SELECT COUNT(*) FROM accounts")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO accounts (id, name, balance) VALUES (?, ?, ?)",
        [(1, "Ahmad", 1000), (2, "Sara", 500)]
    )
    conn.commit()


def show_balances(title):
    print("\n" + title)
    cursor.execute("SELECT * FROM accounts")
    for account in cursor.fetchall():
        print(account)


def transfer(from_id, to_id, amount):
    try:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        conn.execute("BEGIN")

        cursor.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,))
        sender = cursor.fetchone()

        cursor.execute("SELECT balance FROM accounts WHERE id = ?", (to_id,))
        receiver = cursor.fetchone()

        if sender is None or receiver is None:
            raise ValueError("Account not found.")

        if sender[0] < amount:
            raise ValueError("Insufficient balance.")

        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_id)
        )
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_id)
        )

        conn.commit()
        print("Transfer completed successfully.")

    except (ValueError, sqlite3.Error) as error:
        conn.rollback()
        print("Transfer failed:", error)


show_balances("Balances before transfer:")
transfer(1, 2, 200)
show_balances("Balances after transfer:")

conn.close()
