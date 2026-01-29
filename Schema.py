SCHEMA = """

Database Schema:
- pipeline_config: id, name, description, created_at
- stage_logs: id, stage_id, status, start_time, end_time
- config_params: id, config_id, key, value
- users: id, username, email_address, phone_number

"""