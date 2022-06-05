def get_envs_from_file(env_file="local.env") -> None:
    """
    Open file and set the all env variables it contains.

    Example:

    # "./local.env" #
        ...
        # DB settings        -- will be ignored
        DB_HOST=foobar       -- will be set as "DB_HOST" environment variable with value "foobar"
        DB_PASS=span_eggs       os.environ["DB_HOST"] = "foobar"
        ...
    """
    with open(os.path.join(sys.path[0], env_file)) as env_file:
        for line in env_file:
            if line.strip().startswith("#"):
                continue
            try:
                key, value = line.strip().split("=", 1)
                if isinstance(value, str):
                    os.environ[key] = value
            # In case some comments exist in file
            except ValueError:
                continue