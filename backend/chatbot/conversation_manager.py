class ConversationManager:
    def __init__(self):
        # Store context in-memory dict: session_id -> context
        self.sessions = {}

    def get_context(self, session_id: str):
        return self.sessions.get(session_id, {"entities": {}})

    def update_context(self, session_id: str, new_entities: dict):
        if session_id not in self.sessions:
            self.sessions[session_id] = {"entities": {}}
            
        for k, v in new_entities.items():
            self.sessions[session_id]["entities"][k] = v

    def clear_context(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

conversation_manager = ConversationManager()
