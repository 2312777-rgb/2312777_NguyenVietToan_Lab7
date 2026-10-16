# Lab 7 - YummyApp CI/CD - 2312777

Bai thuc hanh Mocking GPS, kiem thu ma khuyen mai va GitHub Actions.

## Chay

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
coverage run --source=yummy_app,gps_service -m unittest discover -s . -p "test_*.py"
coverage report -m
coverage html -d coverage_html
coverage report --fail-under=80
```

**Minh chung bat buoc**: can tu chay de tao logs/local_test.log, logs/git_history.log, logs/github_actions_run.log; scan 4 trang viet tay va lap bao cao PDF co link repo + anh Actions. Khong su dung file log gia.
