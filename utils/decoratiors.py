def log_action(func):
      def wrapper(*args, **kwargs):
          print(f"Running: {func.__name__}")
          result = func(*args, **kwargs)
          print(f"Finished: {func.__name__}")
          return result
      return wrapper