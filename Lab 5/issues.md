# Static Code Analysis — Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Unsafe use of `eval()` | Security — Medium | 92 | `eval()` can execute arbitrary Python expressions. Bandit flags this as B307. | Remove the unsafe demo or replace it with a direct, safe function call. |
| Broad exception with empty handler | Error handling — Low | 24–25 | A bare `except` followed by `pass` silently hides errors. Bandit flags this as B110. | Catch the specific expected exception, such as `KeyError`, and handle it explicitly. |
| Long lines | Formatting | 10, 14, 63, 71, 79, 80 | Lines exceed the configured limits: Pylint's 100 characters or Flake8's 79 characters. | Split long statements across multiple lines. |
| Missing docstrings | Code quality | 1, 10, 20, 29, 34, 45, 51, 58, 66, 70, 77 | The module and several functions lack explanatory docstrings. | Add a module docstring and concise function docstrings. |
| Mutable default argument | Code quality / potential bug | 10 | `audit_log=[]` creates a shared list that can persist across calls. | Use `None` as the default and create a list when needed. |
| Too many function arguments | Maintainability | 10 | `create_ticket()` has six parameters, exceeding Pylint's default limit. | Simplify the function interface or group related options. |
| Unused argument | Code quality | 20 | The `notify` argument is declared but never used. | Implement the intended behavior or remove the argument if unnecessary. |
| Incorrect `None` comparison | Code quality | 37 | `status != None` does not follow recommended Python style. | Use `status is not None`. |
| File handling issues | Reliability / code quality | 46, 53 | Files are opened without an explicit encoding or a context manager. | Use `with open(..., encoding="utf-8")` for automatic file closure. |
| Global statement | Maintainability | 52 | `load_tickets()` modifies the global `TICKETS` variable. | Consider returning the loaded data and assigning it at the caller. |
| Non-idiomatic empty check | Code quality | 60 | `len(TICKETS)` is used to check whether the dictionary is empty. | Use `if not TICKETS:`. |
| Invalid naming style | Code quality | 66 | `closeTicket()` uses camelCase instead of snake_case. | Rename it to `close_ticket()` and update its call. |
| Simplifiable conditional | Code quality | 71 | `is_open()` uses an unnecessary `if/else` to return a Boolean. | Return the Boolean condition directly. |
| Unused variable | Code quality | 84 | The variable `count` is assigned but never used. | Remove the unused variable. |
| Unused imports | Code quality | 4–5 | `sys` and `random` are imported but never used. | Remove the unused imports. |
| Logging formatting | Code quality | 85 | An f-string is used in a logging call instead of lazy logging formatting. | Use `logging.info("Tickets created: %s", len(TICKETS))`. |
| String formatting | Code quality | 16 | `%` formatting is used where Pylint recommends an f-string. | Use an f-string for the audit message. |
| Unnecessary `else` after `return` | Code quality | 71–74 | The `else` branch is unnecessary after a `return`. | Remove the `else` and simplify the function. |
| Trailing whitespace | Formatting | 84 | Extra whitespace appears at the end of a line. | Remove the trailing spaces. |