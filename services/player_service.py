from database import db

class PlayerService:
    def get_hot_players(self, limit=10):
        conn, cursor = db.get_cursor()
        cursor.execute("""
            SELECT id, web_name, team_id, now_cost, form, total_points
            FROM players
            WHERE status = 'a'
            ORDER BY form DESC
            LIMIT %s
        """, (limit,))
        players = cursor.fetchall()
        conn.close()
        return players
    
    def get_injury_news(self):
        conn, cursor = db.get_cursor()
        cursor.execute("""
            SELECT web_name, team_id, status, news
            FROM players
            WHERE status IN ('i', 'd', 'u')
        """)
        injuries = cursor.fetchall()
        conn.close()
        return injuries