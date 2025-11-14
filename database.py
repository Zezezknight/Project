fake_users_db = {
    1: {"id": 1, "username": "john_doe", "role": "user", "password": "password123"},
    2: {"id": 2, "username": "jane_smith", "role": "admin", "password": "admin123"},
    3: {"id": 3, "username": "bob_wilson", "role": "user", "password": "password456"}
}

fake_documents_db = {
    1: {"id": 1, "title": "Project Report", "content": "Project details...", "category": "reports", "is_public": False, "created_by": 1, "created_at": "2025-06-01T10:00:00", "last_modified": "2025-06-01T11:00:00"},
    2: {"id": 2, "title": "Team Guidelines", "content": "Guidelines for team...", "category": "guidelines", "is_public": True, "created_by": 2, "created_at": "2025-06-01T09:00:00", "last_modified": "2025-06-01T10:00:00"},
    3: {"id": 3, "title": "Urgent Update", "content": "Important update...", "category": "urgent", "is_public": False, "created_by": 1, "created_at": "2025-06-01T12:00:00", "last_modified": "2025-06-01T12:00:00"}
}

fake_permissions_db = {
    1: [{"user_id": 1, "permission_level": "write"}, {"user_id": 2, "permission_level": "read"}],
    2: [{"user_id": 2, "permission_level": "write"}, {"user_id": 3, "permission_level": "read"}],
    3: [{"user_id": 1, "permission_level": "write"}]
}